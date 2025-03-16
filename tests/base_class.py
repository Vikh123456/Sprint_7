from api.http_api import YandexScooterApi


class BaseTestClass:

    @property
    def courier_api(self):
        return YandexScooterApi()
