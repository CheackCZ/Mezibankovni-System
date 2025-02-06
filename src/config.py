import os
import sys
import re
from dotenv import load_dotenv
import mysql.connector

class Config:
    """
    Validates and loads all required environment variables.
    """

    def __init__(self):
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
        Validates environment variables.

        :param var_name: Name of the environment variable.
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