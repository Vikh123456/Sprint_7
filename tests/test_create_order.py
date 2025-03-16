import allure
import pytest

from tests.base_class import BaseTestClass


@allure.feature("Проверка создания заказа по эндпоинту /api/v1/orders")
class TestCreateOrder(BaseTestClass):

    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GRAY'],
        []
    ])
    @allure.title('Создание заказа')
    @allure.description('Проверка создания заказа (код - 201 и track в ответе)')
    def test_create_order(self, color):
        with allure.step("Подготовка данных"):

            payload = {
                "firstName": "Sergey",
                "lastName": "Samarov",
                "address": "Sovetskaya, 67",
                "metroStation": 1,
                "phone": "+7 800 555 35 35",
                "rentTime": 6,
                "deliveryDate": "2025-03-15",
                "comment": "Posvinite zaranee",
                "color": color
            }

        with allure.step("Вызов api /api/v1/orders"):
            response = self.courier_api.create_order(payload)

        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert 'track' in response.json()
