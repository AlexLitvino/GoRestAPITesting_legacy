"""
'id': integer
'name': string
'email': string
'gender': 'male' or 'female'
'status': 'active' or 'inactive'
"""
import random


class User:

    def __init__(self, name, email, gender, status, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    def __eq__(self, other, ignore_id=False):
        if not isinstance(other, User):
            return False

        comparison = self.name == other.name and self.email == other.email and \
                     self.gender == other.gender and self.status == other.status  # result of comparison without id

        if not ignore_id:
            comparison = comparison and (self.id == other.id)

        return comparison

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\nemail: {self.email}\ngender: {self.gender}\nstatus: {self.status}"


def create_random_user():
    random_names = [
        "Epifania Ornellas",
        "Derrick Heuer",
        "Sandi Hellard",
        "Grisel Waynick",
        "Francis Crimmins",
        "Kathline Villanveva",
        "Chara Brunt",
        "Eddy Fulmore",
        "Naida Peaslee",
        "Rupert Ginsberg"
    ]
    name = random.choice(random_names)
    first_name, last_name =name.split()
    email = first_name + '.' + last_name + str(random.randint(10000, 99999)) + "@test.com"
    gender = random.choice(["male", "female"])
    status = random.choice(["active", "inactive"])
    return User(name, email, gender, status)


def create_user_from_response(response):
    users = []
    users_dict = response.json()["data"]
    for user_item in users_dict:
        id = user_item["id"]
        name = user_item["name"]
        email = user_item["email"]
        gender = user_item["gender"]
        status = user_item["status"]
        users.append(User(name, email, gender, status, id))

    return users
