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
        events = events['events']
        if events:
            for event in events:
                event['ride_date'] = event['ride_date'].strftime("%x")
        return self.load_view('events.html', events=events)

    # routes['/event/<event_id>'] = "Events#show_event"
    def show_event(self, event_id):
        event = self.models['Event'].get_event(event_id)
        return self.load_view('event.html', event=event)

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
    def delete(self, event_id):
        status = self.models['Event'].delete_event(event_id)
        if status['status']:
            flash('Event removed!', 'success')
        return redirect('/')

    # routes['POST']['/event/new/process'] = "Events#new_process"
    def new_process(self):
        event = self.models['Event'].add_event(request.form)
        if event['status']:
            # event doesn't yet exist
            event = self.models['Event'].add_event_process(request.form, session['user']['id'], session['user'][
                'user_info']['user_id'])
            return redirect('/event/'+str(event['event']['event_id']))
        # event exists
        return redirect('/event/'+str(event['event']['event_id']))

    # routes['POST']['/event/new/list/process'] = "Events#new_list_process"

    # routes['POST']['/event/new/create/process'] = "Events#new_create_process"
