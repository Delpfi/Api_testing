import requests
from http import HTTPStatus
def test_1_status():
    url ="https://reqres.in/api/users?page=2"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.status_code == HTTPStatus.OK