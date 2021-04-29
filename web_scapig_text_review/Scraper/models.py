from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Domain(models.Model):
    select = models.CharField(max_length=150)

    def __str__(self):
        return self.select


class Input(models.Model):
    input = models.CharField(max_length=500)
    category = models.ForeignKey(Domain, on_delete=CASCADE)


def my_default():
    return {'foo': ['bar', 'hello'], 'zoo': ['ll', 'pp']}


class Review_Details(models.Model):
    json_data = models.JSONField(default=my_default)
    domain_name = models.CharField(max_length=100)
