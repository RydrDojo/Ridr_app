from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = :user_id"
        data = {
            "user_id": user_id
        }
        user = self.db.get_one(query, data)
        if user:
            return {'status': True, 'user': user}
        return {'status': False}
