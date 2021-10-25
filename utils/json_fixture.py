class JSONFixture:

    @staticmethod
    def get_headers(token):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": "Bearer " + token}
        return headers
