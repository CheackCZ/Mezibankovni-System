import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection():
    """
    Class for managing database connections and validating configuration values.
    [!] - Reused file from the RDBMS project we did before.
    """
    
    def get_engine(echo=False):
        load_dotenv()

        DB_URL = (
            f"mysql+mysqlconnector://"
            f"{Connection.validation(os.getenv('DB_USER'))}:"
            f"{Connection.validation(os.getenv('DB_PASSWORD'))}@"
            f"{Connection.validation(os.getenv('DB_HOST'))}:"
            f"{Connection.port_validation(os.getenv('DB_PORT'))}/"
            f"{Connection.validation(os.getenv('DB_NAME'))}"
        )

        return create_engine(DB_URL, echo=echo)

    def get_session():
        engine = Connection.get_engine()
        Session = sessionmaker(bind=engine)
        return Session()
    

    def validation(value):
        """
        Validates string configuration values, ensuring they are not empty or invalid.
        
        :param value (str): The configuration value to validate.
        
        :return str: The validated and stripped configuration value.
        """
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Invalid configuration -> Update its value inside the .env file.")
        return value.strip()

    def port_validation(port):
        """
        Validates the database port, ensuring it is a valid integer within the range 1-65535.

        :param port (str): The port value to validate.
        
        :return int: The validated port as an integer.
        """
        if not port.isdigit() or not (65525 <= int(port) <= 65535):
            raise ValueError("Invalid configuration for port -> Update its value inside the .env file.")
        return int(port)  