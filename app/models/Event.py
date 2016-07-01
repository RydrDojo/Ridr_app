from system.core.model import Model
from dateutil import parser

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

    def get_event(self, ride_id):
        query = "SELECT * FROM users " \
                "JOIN users_rides ON users.user_id = users_rides.users_user_id " \
                "JOIN rides ON rides.ride_id = users_rides.rides_ride_id " \
                "WHERE rides.ride_id = :ride_id"
        data = {
            "ride_id": ride_id
        }
        ride = self.db.query_db(query, data)
        if ride:
            return {'status': True, 'ride': ride}
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
        query = "INSERT INTO rides (origin, destination, ride_date, ride_time, driver_id, ride_description, " \
                "max_passengers) VALUES (:origin, :destination, :ride_date, :ride_time, :driver_id, " \
                ":ride_description, :max_passengers)"
        data = {
            "origin": form['origin'],
            "destination": form['destination'],
            "ride_date": parser.parse(form['date']),
            "ride_time": form['time'],
            "ride_description": form['ride_description'],
            "max_passengers": form['max_passengers'],
            "driver_id": driver_id
        }
        self.db.query_db(query, data)

        # Get ride from rides table
        query = "SELECT * FROM rides WHERE driver_id = :driver_id ORDER BY ride_id DESC"
        data = {
            "driver_id": driver_id
        }
        ride = self.db.query_db(query, data)

        # Check intermediary table for ride
        query = "SELECT * FROM users_rides WHERE users_user_id = :user_id AND rides_ride_id = :ride_id"
        data = {
            'user_id': user_id,
            'ride_id': ride[0]['ride_id']
        }
        result = self.db.query_db(query, data)
        if not result:
            # Insert into intermediary table
            query = "INSERT INTO users_rides (users_user_id, rides_ride_id) VALUES (:user_id, :ride_id)"
            data = {
                'user_id': user_id,
                'ride_id': ride[0]['ride_id']
            }
            self.db.query_db(query, data)

        if ride:
            return {'status': True, 'ride': ride[0]}
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

    def add_user_to_ride(self, ride_id, user_id):
        query = "SELECT * FROM users_rides WHERE users_user_id = :user_id AND rides_ride_id = :ride_id"
        data = {
            "user_id": user_id,
            "ride_id": ride_id
        }
        result = self.db.query_db(query, data)
        if not result:
            query = "INSERT INTO users_rides (users_user_id, rides_ride_id) VALUES (:user_id, :ride_id)"
            self.db.query_db(query, data)
        return {'status': True, 'result': result}

    def remove_user_from_ride(self, ride_id, user_id):
        query = "SELECT * FROM users_rides WHERE users_user_id = :user_id AND rides_ride_id = :ride_id"
        data = {
            "user_id": user_id,
            "ride_id": ride_id
        }
        result = self.db.query_db(query, data)
        if result:
            query = "DELETE FROM users_rides WHERE users_user_id = :user_id AND rides_ride_id = :ride_id"
            self.db.query_db(query, data)
            return {'status': True}
        return {'status': False}