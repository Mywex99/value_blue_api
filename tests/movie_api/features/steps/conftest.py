import os
from collections import namedtuple

import pytest
from dotenv import load_dotenv
from helpers import MovieAPI


load_dotenv()
Env = namedtuple("Env", "host")

HOSTS = {
    "test": "https://movie-database-alternative.p.rapidapi.com",
    "dev": "https://movie-database-alternative.p.rapidapi.com/",
    "prod": "https://movie-database-alternative.p.rapidapi.com/",
    "local": "",
}

def get_env():
    env_type = os.environ.get("ENV")
    if env_type not in HOSTS:
        raise ValueError()

    return Env(host=os.environ.get("HOST", HOSTS[env_type]))

@pytest.fixture(scope="session")
def movie_api_rest() -> MovieAPI:
    return MovieAPI(get_env().host)
