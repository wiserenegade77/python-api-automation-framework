import pytest

def test_api(api_client):
    data =api_client.get("https://www.google.com")
    print(data.status_code)