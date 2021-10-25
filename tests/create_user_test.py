from statuses import Status
from utils.api import Api
from model.user import create_random_user
from model.user_search import UserSearch


class TestCreateUser:

    @staticmethod
    def test_create_user_nominal_status():
        user = create_random_user()
        response = Api.create_user(user)

        assert Status.CREATED == response.status_code

    @staticmethod
    def test_create_user_nominal():
        user = create_random_user()
        print(user)
        response = Api.create_user(user)

        id = response.json()["data"]["id"]
        us = UserSearch(id=id)
        response = Api.get_users(us)
        print(response.json()['data'][0])





# TODO: test with the same email -> 422
# TODO: check tht user is saved (get by id)