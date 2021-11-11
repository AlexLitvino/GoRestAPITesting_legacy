from status_codes import Status
from utils.api import Api
from utils.headers import HEADERS_WITHOUT_AUTHORIZATION
from model.user import create_random_user, create_users_from_response
from model.user_search import UserSearch
from resources import Resources


class TestCreateUser:

    @staticmethod
    def test_nominal_user_is_saved():
        user = create_random_user()
        response = Api.create_user(user)
        assert Status.CREATED == response.status_code
        id = response.json()["data"]["id"]
        us = UserSearch(id=id)
        response = Api.get_users(us)
        users_from_response = create_users_from_response(response)
        assert 1 == len(users_from_response)
        assert user.compare(users_from_response[0], ignore_id=True)

    @staticmethod
    def test_create_two_users_and_verify_id_increments():
        # TODO: this test might be flaky because someone's request for user creation will be sent between creation user1 and user2
        user1 = create_random_user()
        user2 = create_random_user()
        response1 = Api.create_user(user1)
        response2 = Api.create_user(user2)
        id1 = response1.json()["data"]["id"]
        id2 = response2.json()["data"]["id"]
        assert id2 == id1 + 1

    @staticmethod
    def test_user_is_not_created_without_authentication():
        user = create_random_user()
        body = user.get_json()
        response = Api.create_user_generic(body, headers=HEADERS_WITHOUT_AUTHORIZATION)
        assert Status.UNAUTHORIZED == response.status_code
        response = Api.get_users(UserSearch(user))
        assert [] == response.json()["data"]

    @staticmethod
    def test_user_is_not_created_without_name():
        user = create_random_user()
        body = user.get_json()
        del body["name"]
        response = Api.create_user_generic(body)
        assert Status.UNPROCESSABLE_ENTITY == response.status_code
        assert Resources.MISSING_NAME_ERROR == response.json()["data"]
        response = Api.get_users(UserSearch(user))
        assert [] == response.json()["data"]

    @staticmethod
    def test_user_is_not_created_without_email():
        user = create_random_user()
        body = user.get_json()
        del body["email"]
        response = Api.create_user_generic(body)
        assert Status.UNPROCESSABLE_ENTITY == response.status_code
        assert Resources.MISSING_EMAIL_ERROR == response.json()["data"]
        response = Api.get_users(UserSearch(user))
        assert [] == response.json()["data"]

    @staticmethod
    def test_user_is_not_created_without_gender():
        user = create_random_user()
        body = user.get_json()
        del body["gender"]
        response = Api.create_user_generic(body)
        assert Status.UNPROCESSABLE_ENTITY == response.status_code
        assert Resources.MISSING_GENDER_ERROR == response.json()["data"]
        response = Api.get_users(UserSearch(user))
        assert [] == response.json()["data"]

    @staticmethod
    def test_user_is_not_created_without_status():
        user = create_random_user()
        body = user.get_json()
        del body["status"]
        response = Api.create_user_generic(body)
        assert Status.UNPROCESSABLE_ENTITY == response.status_code
        assert Resources.MISSING_STATUS_ERROR == response.json()["data"]
        response = Api.get_users(UserSearch(user))
        assert [] == response.json()["data"]

    @staticmethod
    def test_user_is_not_created_with_already_registered_email():
        user1 = create_random_user()
        response = Api.create_user(user1)
        assert Status.CREATED == response.status_code
        user2 = create_random_user()
        user2.email = user1.email
        response = Api.create_user(user2)
        assert Status.UNPROCESSABLE_ENTITY == response.status_code
        assert Resources.DUPLICATED_EMAIL_ERROR == response.json()["data"]
