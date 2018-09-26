import base64

import requests
from django.db import models


class GithubFile(models.Model):
    username = models.CharField(max_length=200)
    repository = models.CharField(max_length=300)
    path = models.CharField(max_length=1000)

    def type(self):
        return self.get_data()['type']

    def content(self):
        return base64.b64decode(self.get_data()['content']).decode('UTF-8')

    def get_data(self):
        url = self.format_url()
        request = requests.get(url)
        return request.json()

    def format_url(self):
        url = 'https://api.github.com/repos/' + \
              self.username.__str__() + '/' + \
              self.repository.__str__() + '/' + \
              'contents/' + \
              self.path.__str__()
        return url
