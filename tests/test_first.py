import pytest
from config import BASE_URL

@pytest.mark.parametrize(
    "user_id,status",
    [
    (1,200),
    (2,200),
    (10,200),
    (9999,404)
    ]
)
def test_get_user(api_client,user_id,status):
    api_response =api_client.get(BASE_URL+'/users/'+f"{user_id}",
    timeout = 10)

    # print(api_response.json())
    assert api_response.status_code == status

    if api_response.status_code == 200:                
        header = api_response.headers
        assert header['Content-Type'].split(";")[0].strip().lower() == "application/json"
        dict_data = api_response.json()
        assert dict_data['id'] == user_id
        assert dict_data['email']
        assert isinstance(dict_data['email'],str)
        assert '@' in dict_data['email']
        assert isinstance(dict_data['address'],dict)
        assert 'city' and 'zipcode' in dict_data['address']
        print(dict_data['address'])

        
