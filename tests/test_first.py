import pytest

@pytest.mark.parametrize(
    "user_id,status",
    [pytest.param(1,200),pytest.param(2,200),pytest.param(9999,404)]
)
def test_api(api_client,user_id,status):
    api_response =api_client.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")

    assert api_response.status_code == status

    if api_response.status_code == 200:
        dict_data = api_response.json()
        assert dict_data['id'] == user_id
        assert dict_data['email']
        assert isinstance(dict_data['email'],str) and '@' in dict_data['email']