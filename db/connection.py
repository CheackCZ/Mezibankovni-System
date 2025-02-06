from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from src.config import config
from src.logger import setup_logger

class Connection:
    """
    Class for managing database connections and ensuring a single engine instance.
    """

    logger = setup_logger()
    _engine = None  

    @classmethod
    def get_engine(cls, echo=False):
        """
        Returns a single shared database engine instance.
        """
        if cls._engine is None:
            try:
                DB_URL = (f"mysql+mysqlconnector://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}")
                cls._engine = create_engine(DB_URL, echo=echo)

                cls.logger.info("Database engine initialized successfully.")

            except OperationalError as e:
                cls.logger.error(f"[!] Database connection failed: {e}")
                raise ConnectionError(f"[!] Database connection failed: {e}")

        return cls._engine 

    @classmethod
    def get_session(cls):
        """
        Creates and returns a new session using the shared engine.
        """
        try:
            engine = cls.get_engine()
            Session = sessionmaker(bind=engine)
            
            cls.logger.info("Database session created successfully.")
            return Session()
        
        except Exception as e:
            cls.logger.error(f"Error creating database session: {e}")
            raise ConnectionError(f"[!] Error creating database session: {e}")