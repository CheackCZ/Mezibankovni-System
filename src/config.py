import os
import sys
import re
from dotenv import load_dotenv
import mysql.connector

class Config:
    """
    Validates and loads all required environment variables for the application.
    Ensures database connectivity and correct configuration settings.
    """

    def __init__(self):
        """
        Initializes the Config class by loading environment variables and validating them.
        """
        load_dotenv()  

        # Database configuration
        self.DB_HOST = self._validate_host("DB_HOST")
        self.DB_USER = self._validate_env_variable("DB_USER")
        self.DB_PASSWORD = self._validate_env_variable("DB_PASSWORD")
        self.DB_NAME = self._validate_env_variable("DB_NAME")
        self.DB_PORT = self._validate_port("DB_PORT", min_value=1, max_value=65524)

        self._validate_db_connection()

        # Socket configuration
        self.HOST = self._validate_host("HOST")
        self.PORT = self._validate_port("PORT", min_value=65525, max_value=65535) 
        self.FORMAT = self._validate_env_variable("FORMAT", allowed_values=["utf-8", "ascii"])

        # Logging level configuration
        self.LOG_LEVEL = self._validate_env_variable("LOG_LEVEL", allowed_values=["debug", "info", "warning", "error", "critical"])

        # Timeout configuration
        self.TIMEOUT = self._validate_timeout("TIMEOUT")


    def _validate_host(self, var_name):
        """
        Validates that the provided HOST or DB_HOST value is a valid IPv4 or 'localhost'.

        :param var_name (str): Name of the environment variable containing the host.
        :return: Validated host string.

        :raises ValueError: If the value is missing or not a valid host.
        """
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"[!] Missing required environment variable: {var_name}")

        ipv4_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        localhost_pattern = r"^localhost$"

        if not re.match(ipv4_pattern, value) and not re.match(localhost_pattern, value):
            raise ValueError(f"[!] Invalid IP address format for {var_name}: {value}")
        
        return value

        
    def _validate_port(self, var_name, min_value, max_value):
        """
        Validates that the provided port is an integer within the allowed range.

        :param var_name (str): Name of the environment variable containing the port.
        :param min_value (int): Minimum allowed value for the port.
        :param max_value (int): Maximum allowed value for the port.

        :return: Validated port number as an integer.
        """
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"[!] Missing required environment variable: {var_name}")
        
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"[!] {var_name} must be an integer.")

        if not min_value <= value <= max_value:
            raise ValueError(f"[!] Invalid {var_name} value: {value}. Must be between {min_value} and {max_value}.")
        
        return value


    def _validate_timeout(self, var_name):
        """
        Validates the timeout value from the environment.

        :param var_name (str): Name of the environment variable containing the timeout value.

        :return: Validated timeout value as an integer.
        """
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"[!] Missing timeout variable: {var_name}")
        
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"[!] {var_name} must be an integer.")
        
        if not 1 <= value <= 60:
            raise ValueError(f"[!] Invalid {var_name} value: {value}. Must be between 1 and 60.")
        
        return value


    def _validate_env_variable(self, var_name, allowed_values=None):
        """
        Validates an environment variable to ensure it is present and optionally checks for allowed values.

        :param var_name (str): Name of the environment variable.
        :param allowed_values (list, optional): List of allowed values for the variable.

        :return: Validated environment variable value as a string.
        """
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"[!] Missing required environment variable: {var_name}")
        
        if allowed_values and value.lower() not in allowed_values:
            raise ValueError(f"[!] Invalid value for {var_name}: {value}. Must be one of {allowed_values}.")
        
        return value
    

    def _validate_db_connection(self):
        """
        Checks if the database credentials are valid by attempting a connection.
        """
        try:
            connection = mysql.connector.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME
            )
            connection.close()

        except mysql.connector.Error as err:
            raise ValueError(f"[!] Database connection failed: {err}")


try:
    config = Config()
except ValueError as ve:
    print(f"{ve}")
    sys.exit(1)