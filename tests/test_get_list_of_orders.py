import allure
from tests.base_class import BaseTestClass


@allure.feature("Проверка получения списка заказов по эндпоинту /api/v1/orders")
class TestGetListOfOrders(BaseTestClass):

    @allure.title('Получение списка заказов')
    @allure.description('Получение списка заказов')
    def test_get_list_of_orders(self):
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
                "color": "BLACK"
            }

        with allure.step("Вызов api /api/v1/orders"):
            self.courier_api.create_order(payload)
            response = self.courier_api.get_orders()

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert 'orders' in response.json()
