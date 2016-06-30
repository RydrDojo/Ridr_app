from system.core.model import Model
from datetime import datetime

class Event(Model):
    def __init__(self):
        super(Event, self).__init__()

    def get_events(self):
        query = "SELECT * FROM rides JOIN users on users.fb_user_id = rides.driver_id"
        events = self.db.query_db(query)
        if events:
            return {'status': True, 'events': events}
        return {'status': False}

    def get_events_by_user(self, user_id):
        query = "SELECT * FROM users JOIN users_rides ON users.user_id = users_rides.users_user_id JOIN rides ON " \
                "rides.ride_id = users_rides.rides_ride_id WHERE users.user_id = :user_id"
        data = {
            "user_id": user_id
        }
        events = self.db.query_db(query, data)
        if events:
            return {'status': True, 'events': events}
        return {'status': False}

    def get_event(self, event_id):
        query = "SELECT * FROM rides WHERE event_id = :event_id"
        data = {
            "event_id": event_id
        }
        event = self.db.query_db(query, data)
        if event:
            return {'status': True, 'event': event}
        return {'status': False}

    def add_event(self, form):
        query = "SELECT * FROM rides WHERE origin = :origin AND destination = :destination"
        data = {
            "origin": form['origin'],
            "destination": form['destination']
        }
        events = self.db.query_db(query, data)
        if events:
            return {'status': False}
        return {'status': True}

    def add_event_process(self, form, driver_id, user_id):
        # Insert into rides table
        query = "INSERT INTO rides (origin, destination, ride_date, ride_time, driver_id) VALUES (:origin, " \
                ":destination, :ride_date, :ride_time, :driver_id)"
        data = {
            "origin": form['origin'],
            "destination": form['destination'],
            "ride_date": form['date'],
            "ride_time": form['time'],
            "driver_id": driver_id
        }
        self.db.query_db(query, data)

        # Insert into intermediary table
        query = "INSERT INTO users_rides (users_user_id, rides_ride_id) VALUES (:user_id, :ride_id)"
        data = {
            'user_id': user_id
        }
        self.db.query_db(query, data)

        # Get ride from rides table
        query = "SELECT * FROM rides WHERE driver_id = :driver_id"
        data = {
            "driver_id": driver_id
        }
        event = self.db.query_db(query, data)
        if event:
            return {'status': True, 'event': event}
        return {'status': False}

    def delete_event(self, event_id):
        query = "SELECT * FROM events WHERE event_id = :event_id"
        data = {
            "event_id": event_id
        }
        event = self.db.query_db(query, data)
        if event:
            query = "DELETE FROM rides WHERE event_id = :event_id"
            self.db.query_db(query, data)
            return {'status': True, 'event': event}
        return {'status': False}