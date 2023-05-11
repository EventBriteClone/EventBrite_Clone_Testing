from locust import HttpUser, task, between
import random

class EventbriteUser(HttpUser):
    wait_time = between(1, 5)

    ###################################################################################
    ################################## GET TASKS ######################################
    ###################################################################################

    @task
    def index_page(self): #Khalsan
        self.client.get("/")

    @task(1)
    def browse_events(self): #Khalsan
        self.client.get("/events/ALL/")

    @task(2)
    def browse_events(self): #Khalsan
        self.client.get("/events/free-events/")

    @task(3)
    def search_event(self): #Khalsan
        self.client.get("/events/search/", params={"q": "test"})

    @task(4)
    def view_event(self):
        EventIDs = ["7333%7D", "9463%7D", "3862"] #ask backend for valid events
        event_id = 1  # replace with a valid event ID
        self.client.get(f"/events/ID/{random.choice(EventIDs)}")

    ###################################################################################
    ################################# POST TASKS ######################################
    ###################################################################################
    
    @task(5)
    def create_event(self):
        data = {
            "title": "Test Event",
            "description": "This is a test event.",
            "location": "Test Location",
            "date": "2023-03-17T10:00",
            "ticket_price": "10.00",
            "ticket_quantity": "100"
        }
        self.client.post("/create_event", data=data)

# RUN THIS INTO THE TERMINAL: locust -f LocustMain2.py --host=https://event-us.me/
# this line is a Git Test