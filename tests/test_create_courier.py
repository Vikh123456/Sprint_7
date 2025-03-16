import allure

from data.courier_data import generation_new_data_courier
from tests.base_class import BaseTestClass


@allure.feature("Проверка создания курьера по эндпоинту /api/v1/courier/login")
class TestCreateCourier(BaseTestClass):

    @allure.title('Создание курьера')
    @allure.step('Проверка создания курьера (код - 201 и текст - "ok": True')
    def test_create_courier(self, registered_courier_data):
        with allure.step("Создаём payload для вызова api"):
            data = generation_new_data_courier()
            data.pop("firstName")

        with allure.step("Вызов /api/v1/courier"):
            response = self.courier_api.create_courier(data)

        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}, "Неверное содержимое ответа."

        with allure.step("Вызов api с информацией по курьеру"):
            login_payload = {
                "login": data["login"],
                "password": data["password"]
            }
            login_response = self.courier_api.login_courier(login_payload)

        with allure.step("Проверка ответа"):
            assert login_response.status_code == 200, "Login failed."

        courier_id = login_response.json().get("id")
        assert courier_id is not None, "Courier ID not found in login response."

        with allure.step("Удаляем курьера"):
            delete_response = self.courier_api.delete_courier(courier_id)

        with allure.step("Проверка ответа"):
            assert delete_response.status_code == 200, "Failed to delete courier."


    @allure.title('Проверка невозможности создать курьера. дублирующие креды')
    @allure.description('Проверка, что нельзя создать курьера с уже существующеми кредами')
    def test_create_courier_duplicate_login(self, registered_courier_data):
        with allure.step("Создаём дубль курьера"):
            payload = registered_courier_data

        with allure.step("Вызываем api"):
            response = self.courier_api.create_courier(payload)

        with allure.step("Првоерка ответа"):
            assert response.status_code == 409
            assert response.json() == {"code": 409,
                                       "message": "Этот логин уже используется. Попробуйте другой."}, "Неверное содержимое ответа."


    @allure.title('Проверка невозможности создать курьера. Не все обязательные поля')
    @allure.description(
        'Проверка заполнения не всех обязательных полей. Курьер не создан (код - 400 и текст - "message": "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_password(self):
        with allure.step("Создаём нового курьера"):
            data = generation_new_data_courier()

        with allure.step("Вызываем api"):
            payload = {
                "login": data["login"],
                "firstName": data["firstName"]
            }
            response = self.courier_api.create_courier(payload)

        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json() == {"code": 400,
                                       "message": "Недостаточно данных для создания учетной записи"}, "Неверное содержимое ответа."
