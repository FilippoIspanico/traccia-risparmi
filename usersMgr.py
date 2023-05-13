from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required


class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return str(self.id)

