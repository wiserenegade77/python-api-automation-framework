import requests
import pytest
from clients.api_client import APIClient
from config import BASE_URL

@pytest.fixture(scope= "session")
def http_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="session")
def api_client(http_session):
    return APIClient(
    base_url = BASE_URL,
    session = http_session
    )

