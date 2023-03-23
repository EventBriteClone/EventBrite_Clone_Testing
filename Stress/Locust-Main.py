from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def view_homepage(self):
        self.client.get("/")
        
    @task(2)
    def search_events(self):
        self.client.get("/d/online--events/")
        self.client.get("/d/california--san-francisco/events/")
        
    @task(3)
    def view_event(self):
        event_id = "12345" # Replace with a valid event ID
        self.client.get(f"/event/{event_id}/")
        
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)