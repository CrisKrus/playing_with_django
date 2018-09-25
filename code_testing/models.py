import base64

import requests
from django.db import models


class GithubFile(models.Model):
    username = models.CharField(max_length=200)
    repository = models.CharField(max_length=300)
    path = models.CharField(max_length=1000)
    __data = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: extract to github client
        url = 'https://api.github.com/repos/' + \
              self.username + '/' + \
              self.repository + '/' + \
              self.path
        request = requests.get(url)
        self.__data = request.json()

    def type(self):
        return self.__data['type']

    def content(self):
        return base64.b64decode(self.__data['content'])
