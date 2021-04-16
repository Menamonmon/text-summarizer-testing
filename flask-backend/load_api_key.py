import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def load_api_key(keyname="API_KEY"):
    return os.environ[keyname]
