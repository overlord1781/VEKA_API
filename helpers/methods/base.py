import requests
from helpers.data_test import authorization_dev

class Base():

    def __init__(self, url):
        self.url = url

    @staticmethod
    def status_code(url):
        response = requests.get(url, auth=(authorization_dev['login'], authorization_dev['pass']))
        return response
