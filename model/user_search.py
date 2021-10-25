"""
'id': integer
'name': string
'email': string
'gender': 'male' or 'female'
'status': 'active' or 'inactive'
'page': integer
"""


class UserSearch:

    def __init__(self, user=None, id=None, name=None, email=None, gender=None, status=None, page=None):
        if user:
            if user.id:
                self.id = user.id
            if user.name:
                self.name = user.name
            if user.email:
                self.email = user.email
            if user.gender:
                self.gender = user.gender
            if user.status:
                self.status = user.status
        else:
            if id:
                self.id = id
            if name:
                self.name = name
            if email:
                self.email = email
            if gender:
                self.gender = gender
            if status:
                self.status = status
        if page:
            self.page = page

    def get_search_parameters_string(self):
        params_string = "?"
        fields = self.__dict__
        for field in fields:
            params_string += field + "=" + str(fields[field]) + '&'
        return params_string[:-1]  # if string should be empty it will cut '?', otherwise it will cut last added '&'

    def test(self):
        print(self.__dict__)
