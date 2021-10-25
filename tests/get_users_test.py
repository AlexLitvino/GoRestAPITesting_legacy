from statuses import Status
from utils.Api import Api
from model.user_search import UserSearch
from allure_commons._allure import step
import os

# {'meta': {'pagination': {'total': 1510, 'pages': 76, 'page': 1, 'limit': 20,
# 'links': {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1', 'next': 'https://gorest.co.in/public/v1/users?page=2'}}},
# 'data': [{'id': 67, 'name': 'Chandraayan Kakkar', 'email': 'kakkar_chandraayan@tillman.org', 'gender': 'male', 'status': 'active'},


class TestGetUsers:

    @staticmethod
    def setup():
        response = Api.get_users()
        response_content = response.json()
        total_users = response_content["meta"]["pagination"]["total"]
        total_pages = response_content["meta"]["pagination"]["pages"]



    @staticmethod
    def test_get_users_first_page():
        response = Api.get_users()

        response.json()["data"]

        assert Status.OK == response.status_code
        assert response.json()["meta"]["pagination"]["total"] > 0  # TODO: get number from site and compare

    @staticmethod
    def test_get_users_page_greater_than_max():
        with step("Get users for non-existing page"):
            us = UserSearch(page=800)
            response = Api.get_users(us)
            assert [] == response.json()["data"]




