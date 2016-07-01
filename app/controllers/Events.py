from system.core.controller import *
from time import strftime

class Events(Controller):
    def __init__(self, action):
        super(Events, self).__init__(action)
        self.load_model('Event')
        self.db = self._app.db

    # routes['/events'] = "Events#index"
    def index(self):
        events = self.models['Event'].get_events()
        if events['status']:
            events = events['events']
            for event in events:
                event['ride_date'] = event['ride_date'].strftime("%x")
            return self.load_view('events.html', events=events)
        return self.load_view('events.html')

    # routes['/event/<event_id>'] = "Events#show_event"
    def show_event(self, ride_id):
        session['rides_in'] = []
        ride = self.models['Event'].get_event(ride_id)
        ride = ride['ride']
        ride[0]['ride_id'] = ride[0]['ride_id']
        rides_in = self.models['Event'].get_events_by_user(session['user']['user_info']['user_id'])
        for ride_in in rides_in['events']:
            session['rides_in'].append(int(ride_in['rides_ride_id']))
        my_fb_user_id = session['user']['id']
        return self.load_view('event.html', ride=ride, rides_in=session['rides_in'], my_fb_user_id=my_fb_user_id)

    # routes['/event/new'] = "Events#new"
    def new(self):
        return self.load_view('new.html')

    # routes['/event/new/list'] = "Events#new_list"
    def new_list(self, events):
        return self.load_view('new.html', events=events)

    # routes['/event/new/create'] = "Events#new_create"
    def new_create(self, event):
        return self.load_view('new.html', event=event)

    # routes['/event/<event_id>/delete'] = "Events#delete"
    def delete(self, ride_id):
        status = self.models['Event'].delete_event(ride_id, session['user']['user_info']['user_id'])
        if status['status']:
            flash('Event removed!', 'success')
        return redirect('/')

    # routes['POST']['/event/new/process'] = "Events#new_process"
    def new_process(self):
        ride = self.models['Event'].add_event_process(request.form, session['user']['id'], session['user']['user_info']['user_id'])
        return redirect('/event/'+str(ride['ride']['ride_id']))

    def ride_join(self, ride_id):
        self.models['Event'].add_user_to_ride(ride_id, int(format(session['user']['user_info']['user_id'], 'x')))
        session['rides_in'].append(ride_id)
        return redirect('/event/'+str(ride_id)+'#top')

    def ride_leave(self, ride_id):
        self.models['Event'].remove_user_from_ride(ride_id, int(format(session['user']['user_info']['user_id'], 'x')))
        return redirect('/event/'+str(ride_id)+'#top')
