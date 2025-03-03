import time 
from locust import HttpUser, task, between

class ApiUser(HttpUser):    

    # optional 
    wait_time = between(1, 3)


    @task
    def getUserList(self):
        self.client.get('/v1/users' , headers={'Auth':"True"})