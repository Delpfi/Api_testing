from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import re

def test_list_users():
    res = api.list_users()
    user_not_found = api.single_user_not_found()
    print("json",res.json())
    print('\n')
    print('text',res.text)
    assert res.status_code == HTTPStatus.OK
    assert  user_not_found.status_code == HTTPStatus.NOT_FOUND
    assert res.headers['Cache-Control'] == 'max-age=14400'
    Assert.validate_schema(res.json())
    print(res.headers)


def test_single_user():
    single_user = api.single_user()
    res_body = single_user.json()
    print(res_body)
    assert single_user.status_code == HTTPStatus.OK
    assert res_body["data"]["first_name"] == 'Janet'
    assert re.fullmatch("\w+", res_body['data']["last_name"])
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body

def test_create():
    name = 'Boris'
    job = 'Tester'
    res = api.create(name, job)
    #res1 = res.create(name,job)
    assert re.fullmatch(r'\d{1,4}', res.json()['id'])

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job

    assert  api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT

def test_register():
    password = 'pistol2'
    res = api.register(password)
    print(res.json(), res.status_code)
    assert res.status_code == HTTPStatus.OK
    #print(res.raise_for_status())

def test_bad_register():

    res_bad_request = api.register_bad_request()
    print(res_bad_request.json(), res_bad_request.status_code)
    assert res_bad_request.status_code == HTTPStatus.BAD_REQUEST
    example = {
            "error": "Missing password"
    }
    #print(res_bad_request.raise_for_status()) #Если мы сделали неверный запрос (ошибка клиента 4XX или ответ об ошибке сервера 5XX), мы можем поднять его с помощью
    assert res_bad_request.json() == example
    Assert.validate_schema(res_bad_request.json())





