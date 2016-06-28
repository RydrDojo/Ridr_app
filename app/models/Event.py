from system.core.model import Model

class Event(Model):
    def __init__(self):
        super(Event, self).__init__()

    def get_event(self, event_id):
        query = "SELECT * FROM events WHERE event_id = :event_id"
        data = {
            "event_id": event_id
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
            query = "DELETE FROM events WHERE event_id = :event_id"
            self.db.query_db(query, data)
            return {'status': True, 'event': event}
        return {'status': False}