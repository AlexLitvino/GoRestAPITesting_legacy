from status_codes import Status
from utils.api import Api
from model.user_search import UserSearch
from allure_commons._allure import step


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




