from django.db import models


class File(models.Model):
    username = models.CharField(max_length=200)
    repository = models.CharField(max_length=300)
    path = models.CharField(max_length=1000)

    def type(self):
        return "type"
