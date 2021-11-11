import requests
from utils.config_parser import BASE_URL
from utils.headers import HEADERS_WITH_AUTHORIZATION


class Api:

    GET_USERS_URL = BASE_URL + "/public/v1/users"
    CREATE_USER_URL = BASE_URL + "/public/v1/users"

    @staticmethod
    def get_users(user_search=None):  # TODO: add other params, how?
        # https://gorest.co.in/public/v1/users
        params = ""
        if user_search:
            params = user_search.get_search_parameters_string()
        response = requests.get(Api.GET_USERS_URL + params)
        return response

    @staticmethod
    def get_posts(page=None):
        # https://gorest.co.in/public/v1/posts
        pass

    @staticmethod
    def get_comments(page=None):
        # https://gorest.co.in/public/v1/comments
        pass

    @staticmethod
    def get_todos(page=None):
        # https://gorest.co.in/public/v1/todos
        pass

    @staticmethod
    def create_user_generic(body, headers=HEADERS_WITH_AUTHORIZATION):
        # POST /public/v1/users
        response = requests.post(url=Api.CREATE_USER_URL,
                                 json=body,
                                 headers=headers)
        return response

    @staticmethod
    def create_user(user):
        # POST /public/v1/users
        body = {"name": user.name,
                "email": user.email,
                "gender": user.gender,
                "status": user.status}

        response = requests.post(url=Api.CREATE_USER_URL,
                                 json=body,
                                 headers=HEADERS_WITH_AUTHORIZATION)
        return response

    @staticmethod
    def get_user_details():
        # GET /public/v1/users/123
        pass

    @staticmethod
    def update_user_details():
        # PUT|PATCH /public/v1/users/123
        pass

    @staticmethod
    def delete_user():
        # DELETE /public/v1/users/123
        pass

    @staticmethod
    def get_user_posts():
        # GET /public/v1/users/123/posts	Retrieves user posts
        pass

    @staticmethod
    def get_post_comments():
        # GET /public/v1/posts/123/comments	Retrieves post comments
        pass

    @staticmethod
    def get_user_todos():
        # GET /public/v1/users/123/todos	Retrieves user todos
        pass

    @staticmethod
    def create_user_posts():
        # POST /public/v1/users/123/posts	Creates a user post
        pass

    @staticmethod
    def create_post_comment():
        # POST /public/v1/posts/123/comments	Creates a post comment
        pass

    @staticmethod
    def create_user_todo():
        # POST /public/v1/users/123/todos	Creates a user todo
        pass

    # TODO: add parameters for search into GET methods
