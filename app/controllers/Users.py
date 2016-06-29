from system.core.controller import *
from rauth import OAuth2Service
from flask import redirect, request
import urllib2
import json

facebook = OAuth2Service(
    name='facebook',
    base_url='https://graph.facebook.com/',
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    client_id='259154491127882',
    client_secret='c5b9a2e1e25bfa25abc75a9cd2af450a',
)

app_id = "259154491127882"
redirect_uri = 'http://52.52.22.127/'

params = {
    'scope': 'read_stream',
    'response_type': 'code',
    'redirect_uri': redirect_uri
}

url = facebook.get_authorize_url(**params)

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
        return redirect("https://www.facebook.com/dialog/oauth?client_id="+app_id+"&redirect_uri=http://52.52.22.127/oauth-authorized/")

    def oauth_authorized(self):
        code = request.args.get('code')
        json_str = urllib2.urlopen("https://graph.facebook.com/v2.3/oauth/access_token?client_id="+app_id
                                 +"&redirect_uri=http://52.52.22.127/oauth-authorized/&client_secret"
                                  "=c5b9a2e1e25bfa25abc75a9cd2af450a&code="+code).read()
        token = json.loads(json_str)
        token = token['access_token']
        user_info = urllib2.urlopen("graph.facebook.com/bgolub?fields=id,first_name,last_name,email&"+token)
        if user_info:
            session['fb_user'] = user_info
        return self.load_view('index.html')