import logging
from http.client import HTTPConnection

from locust import HttpUser, task, run_single_user


class HelloWorldUser(HttpUser):
    host = "http://google.pl"

    @task
    def hello_world(self):
        self.client.get("/")
        # self.client.get("/search?q=andrzej")


def set_up_configuration():
    HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


if __name__ == "__main__":
    run_single_user(HelloWorldUser)
