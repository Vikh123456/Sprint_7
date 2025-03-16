from urllib.parse import urljoin

import requests


class YandexScooterApi:

    base_url = 'https://qa-scooter.praktikum-services.ru'

    def create_courier(self, data):
        create_url = urljoin(self.base_url, "/api/v1/courier")
        return requests.post(create_url, data=data)

    def login_courier(self, data):
        create_url = urljoin(self.base_url, "/api/v1/courier/login")
        return requests.post(create_url, data=data)

    def delete_courier(self, courier_id):
        delete_url = urljoin(self.base_url, f"/api/v1/courier/{courier_id}")
        return requests.delete(delete_url)

    def create_order(self, data):
        order_url = urljoin(self.base_url, "/api/v1/orders")
        return requests.post(order_url, json=data)

    def get_orders(self):
        order_url = urljoin(self.base_url, "/api/v1/orders")
        return requests.get(order_url)

