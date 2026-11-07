import requests
import pytest

@pytest.fixture
def api_client(scope= "session"):
    session = requests.Session()
    yield session
    session.close()

