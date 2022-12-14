from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    host = "http:/google.pl"

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/search?q=andrzej")
