class Post:

    def __init__(self, id, user_id, title, body):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body

    def __str__(self):
        return f"id: {self.id}\nuser_id: {self.user_id}\ntitle: {self.title}\nbody: {self.body}"
