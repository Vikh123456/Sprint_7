import allure
from data.courier_data import register_new_courier_and_return_login_password
from tests.base_class import BaseTestClass


@allure.feature("Проверка логина курьера по эндпоинту /api/v1/courier/login")
class TestLoginCourier(BaseTestClass):
    @allure.title('Авторизация курьера')
    @allure.description('Проверка получения ID курьера при авторизации с корректным login и password (код - 200 и ID')
    def test_get_courier_id(self, delete_courier_data):
        with allure.step("Подготовка данных"):
            payload = delete_courier_data

        with allure.step("Вызов api /api/v1/courier/login"):
            response = self.courier_api.login_courier(payload)

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert 'id' in response.json()

    @allure.title('Авторизация курьера не пройдена при отправке неверного password')
    @allure.description('Проверка отправки неверного password при автроизации курьера (код - 404 и "message": "Учетная запись не найдена"')
    def test_get_courier_id(self):
        with allure.step("Подготовка данных"):
            login_pass = register_new_courier_and_return_login_password()

        with allure.step("Вызов api /api/v1/courier/login"):
            payload = {
                "login": login_pass[0],
                "password": login_pass[0]
            }
            response = self.courier_api.login_courier(payload)

        with allure.step("Проверка ответа"):
            assert response.status_code == 404
            assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}, "Неверное содержимое ответа."

    @allure.title('Авторизация курьера не пройдена при отправке не всех обязательных полей')
    @allure.description(
        'Проверка авторизации курьера без обязательного поля- password (код - 400 и "message": ""message":  "Недостаточно данных для входа"')
    def test_login_courier_without_password(self):
        with allure.step("Подготовка данных"):
            login_pass = register_new_courier_and_return_login_password()

        with allure.step("Вызов api /api/v1/courier/login"):
            payload = {
                "login": login_pass[0],
                "password": ""
            }
            response = self.courier_api.login_courier(payload)

        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}
