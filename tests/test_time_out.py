from http import HTTPStatus

from api.http_bin_app  import http_bin_api

def test_time_out():
    time_out = http_bin_api.time_out(11)

    assert time_out.status_code == HTTPStatus.OK
    time_out.raise_for_status()


    time_out_two_sec = http_bin_api.time_out(2)
    assert not time_out_two_sec[0]