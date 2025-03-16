import pytest

from api.http_api import YandexScooterApi
from data.courier_data import register_new_courier_and_return_login_password


@pytest.fixture
def delete_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    yield {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    courier_api = YandexScooterApi()
    response = courier_api.login_courier(login_pass)
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            courier_api.delete_courier(courier_id)

@pytest.fixture
def registered_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    return {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }
