from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    ip_address = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=50)
    cookie = models.CharField(max_length=10000)
    referer = models.CharField(max_length=50)
    payload = models.CharField(max_length=50)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.username


    #TODO: Is there anything else?
