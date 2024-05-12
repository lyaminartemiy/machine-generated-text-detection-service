import os
from dotenv import load_dotenv


def init_env():
    """
    Initialize environment variables.

    Loads environment variables from a .env file.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    load_dotenv()


class Config:
    """
    Configuration class.

    Attributes
    ----------
    API_TOKEN : str
        The API token.
    API_URL : str
        The API URL.
    """

    def __init__(self):
        """
        Initialize configuration.

        Sets up environment variables upon instantiation.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        init_env()
        self.API_TOKEN = os.getenv("API_TOKEN", "")
        self.API_URL = os.getenv("API_URL", "")


config = Config()
