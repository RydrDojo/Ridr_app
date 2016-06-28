from system.core.controller import *
import facebook

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    # routes['/'] = "Users#index"
    def index(self):
        return self.load_view('index.html')

    # routes['/login'] = "Users#login"
    def login(self):
        if 'user' in session:
            return redirect('/')
        return self.load_view('login.html')

    # routes['/logout'] = "Users#logout"
    def logout(self):
        if 'user' in session:
            session.clear()
            session['user'] = False
            flash('You have successfully logged out','success')
        return redirect('/')

    # routes['/user/<user_id>'] = "Users#show_user"
    def show_user(self, user_id):
        if 'user' in session:
            user = self.models['User'].get_user(user_id)
            if user:
                return self.load_view('user.html', user=user)
            return redirect('/')
        return redirect('/')

    # routes['/user/inbox'] = "Users#show_inbox"
    def show_inbox(self):
        if 'user' in session:
            return self.load_view('inbox.html')
        return redirect('/')

    # routes['POST']['/login/process'] = "Users#login_process"
    def login_process(self):
        if 'user' in session:
            return redirect('/')

        result = get_user_from_cookie