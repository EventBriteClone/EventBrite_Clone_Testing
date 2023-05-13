from locust import HttpUser, task, between
import random, string

######################################################################################
################################### GLOBAL VARIABLES #################################
######################################################################################

authtoken = "b103cc46d84963ddb4c6ba5609c2a1335fdf055ceff715680c5684adf621c63e"
headers = {"Authorization": f"CustomToken {authtoken}"}
id = "129"
EventIDs = ["7333", "3862"] 

######################################################################################
################################### HELPER FUNCTIONS #################################
######################################################################################

def createEmail():
    # Generate a random string of letters and digits for the username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add a domain name
    email = username + '@gmail.com'
    return email

def createPassword():
    char_set = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(char_set) for i in range(12))
    return password


class EventbriteUser(HttpUser):
    wait_time = between(1, 5)
    
    ###################################################################################
    ################################## GET TASKS ######################################
    ###################################################################################

    @task
    def browse_events(self): #Khalsan
        self.client.get("events/ALL/")

    @task
    def browse_events(self): #Khalsan
        self.client.get("events/free-events/")

    @task
    def search_event(self): #Khalsan
        self.client.get("events/search/gg")

    @task
    def view_event(self): #khalsan
        self.client.get(f"events/ID/{random.choice(EventIDs)}/")

    @task
    def liked_events(self): #khalsan
        self.client.get("events/liked/", headers=headers)

    @task
    def dashboard_get(self): #khalsan
        self.client.get(f"dashboard/user/{id}/")

    @task
    def creator_events(self): #khalsan
        self.client.get("eventmanagement/creatorevents/", headers=headers)

    @task
    def prices(self): #khalsan
        self.client.get(f"events/TicketsPrice/{random.choice(EventIDs)}/", headers=headers)    
    ###################################################################################
    ################################# POST TASKS ######################################
    ###################################################################################
    
    @task #needs auth, khalsan
    def create_event(self):
        data = {'Title': 'LocustTestEvent',
        'organizer': 'Yusuy',
        'ST_DATE': '2023-05-10',
        'END_DATE': '2023-05-10',
        'ST_TIME': '04:00:00',
        'END_TIME': '06:00:00',
        'online': 'True',
        'CAPACITY': '5000',
        'STATUS': 'Draft'}
        self.client.post("events/create/", data=data, headers=headers)


    @task #needs no auth, khalsan
    def login(self):
        data = {
        "email": "youssss@gmail.com",
        "password": "Yusuy_2000"
        }
        self.client.post("user/login/", data=data)

# RUN THIS INTO THE TERMINAL: locust -f LocustMain2.py --host=https://event-us.me:8000/
# this line is a Git Test