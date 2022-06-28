import requests
from helpers.data_test import authorization_dev

class Base():

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url, auth=(authorization_dev['login'], authorization_dev['pass']))

    def get_status_code(self):
        return self.response.status_code

    def get_data(self):
        return self.response.json()
