import re

from api.http_bin_app  import http_bin_api
from http import HTTPStatus
from utils.assertions import Assert

def test_list_html():
   bin_api = http_bin_api.list_html()
   assert bin_api.status_code == HTTPStatus.OK
   assert bin_api.headers['Content-Type'] == "text/html; charset=utf-8"


def test_robots():

    res = http_bin_api.get_robots()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    print(res.content.splitlines())
    x = re.fullmatch(r'User-agent: \*.*Disallow: /deny.*',res.text,flags=re.DOTALL)
    print(x)
    assert re.fullmatch(r'User-agent: \*.*Disallow: /deny.*',res.text,flags=re.DOTALL)

def test_ip():

    res = http_bin_api.get_ip()
    res_body = res.json()
    assert res.status_code == HTTPStatus.OK
    if res.headers['Content-Type'] == 'application/json':
        Assert.validate_schema(res_body)
        value = res_body['origin']
        print(value)
        assert re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', value)
