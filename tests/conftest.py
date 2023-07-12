import os

import pytest
from dotenv import find_dotenv, load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    env_file = find_dotenv(dotenv_path)
    load_dotenv(env_file)