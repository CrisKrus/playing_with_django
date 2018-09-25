import requests

from django.db import models


class File(models.Model):
    username = models.CharField(max_length=200)
    repository = models.CharField(max_length=300)
    path = models.CharField(max_length=1000)
    __data = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = requests.get('https://api.github.com/repos/Criskrus/juego-saber/readme')
        self.__data = request.json()

    def type(self):
        return self.__data['type']
