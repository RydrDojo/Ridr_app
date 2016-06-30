from system.core.controller import *
from rauth import OAuth2Service
from flask import redirect, request
import urllib2
import json
from time import strftime

facebook = OAuth2Service(
    name='facebook',
    base_url='https://graph.facebook.com/',
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    client_id='259154491127882',
    client_secret='c5b9a2e1e25bfa25abc75a9cd2af450a',
)

app_id = "259154491127882"
redirect_uri = 'http://carmarider.com/'

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
        self.load_model('Event')
        self.db = self._app.db

    # routes['/'] = "Users#index"
    def index(self):
        if 'user' in session:
            print session['user']['user_info']
            user_rides = self.models['Event'].get_events_by_user(session['user']['user_info']['user_id'])
            if user_rides['status']:
                for ride in user_rides['events']:
                    ride['ride_date'] = ride['ride_date'].strftime('%x')
                return self.load_view('index.html', user_rides=user_rides['events'])
        return self.load_view('index.html')

    # routes['/login'] = "Users#login"
    def login(self):
        if 'user' in session:
            return redirect('/')
        return self.load_view('login.html')

    # routes['/logout'] = "Users#logout"
    def logout(self):
        if 'user' in session:
            flash('You have successfully logged out', 'success')
        session.clear()
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
        return redirect("https://www.facebook.com/dialog/oauth?client_id="+app_id+"&redirect_uri=http://localhost"
                                                                                  ":5000/oauth-authorized/")

    def oauth_authorized(self):
        code = request.args.get('code')
        json_str = urllib2.urlopen("https://graph.facebook.com/v2.3/oauth/access_token?client_id=" +
                                   app_id + "&redirect_uri=http://localhost:5000/oauth-authorized/&client_secret"
                                    "=c5b9a2e1e25bfa25abc75a9cd2af450a&code=" + code).read()
        token = json.loads(json_str)
        token = token['access_token']
        fb_session = facebook.get_session(token)
        register_data = fb_session.get('/me?fields=id,first_name,last_name,email', params={'format': 'json'}).json()
        user_picture = fb_session.get('/me?fields=picture', params={'format': 'json'}).json()
        if register_data:
            user = self.models['User'].add_user(register_data)
            if user['status']:
                # just registered
                session['new_user'] = True
            # already registered
        session['user'] = register_data
        session['user']['user_info'] = self.models['User'].get_user_by_fbid(session['user']['id'])['user']
        session['user']['picture'] = user_picture['picture']['data']['url']
        return redirect('/')

    def register_process(self):
        user = self.models['User'].register(request.form, session['user']['id'])
        if user['status']:
            # they were updated
            session.pop('new_user')
            session['user']['city'] = user['user']['city']
            return redirect('/')
        # they weren't updated
        flash('There was a problem with your inputs, please try again')
        return redirect('/')