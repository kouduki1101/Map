from django.db import models
from django.views.generic import ListView


# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()


CATEGORY = (('health', '健康')), (('life', '生活')),(('sdgs','関西SDGs'))


class MapModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.title
