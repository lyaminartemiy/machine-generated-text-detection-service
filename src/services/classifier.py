import requests

from src.config.config import config


def classify_text(input_media: str):
    """
    Classify text using an API.

    Sends a POST request to the configured API URL with the input media and returns the response JSON.

    Parameters
    ----------
    input_media : str
        The input media to classify.

    Returns
    -------
    dict
        Response JSON from the API.
    """
    headers = {"Authorization": f"Bearer {config.API_TOKEN}"}
    response = requests.post(config.API_URL, headers=headers, json=input_media)
    return response.json()
