from system.core.model import Model


class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = :user_id LIMIT 1"
        data = {
            "user_id": user_id
        }
        user = self.db.get_one(query, data)
        if user:
            return {'status': True, 'user': user}
        return {'status': False}

    def add_user(self, user_data):
        query = "SELECT * FROM users WHERE fb_user_id = :fb_user_id"
        data = {
            "fb_user_id": user_data['id']
        }
        user = self.db.query_db(query, data)
        if not user:
            query = "INSERT INTO users (fb_user_id, first_name, last_name) VALUES (:fb_user_id, :first_name," \
                    " :last_name)"
            data = {
                "fb_user_id": user_data['id'],
                "first_name": user_data['first_name'],
                "last_name": user_data['last_name']
            }
            self.db.query_db(query, data)
            return {'status': True}
        return {'status': False}

    def update_user(self, form, user_id):
        if form['new_user'] == 1:
            query = "UPDATE users SET email = :email, username = :username WHERE fb_user_id = :fb_user_id"
            data = {
                'email': form['email'],
                'username': form['username'],
                'fb_user_id': user_id
            }
            status = self.db.query_db(query, data)
            if status:
                return {'status': True}
            return {'status': False}