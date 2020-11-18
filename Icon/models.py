from django.db import models
from django.contrib.auth.models import User


# EVALUATION_CHOICES = [('good','good'),('bad','bad')]
# class ReviewModel(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     images = models.ImageField(upload_to='')
#     useful_review = models.IntegerField(null=True,blank=True,default=0)
#     useful_review_record =models.TextField()
#     evaluation = models.CharField(max_length=10,choices=EVALUATION_CHOICES)


class Map(models.Model):
    map_name = models.CharField(max_length=50)

    def __str__(self):
        return self.map_name


class User(models.Model):
    user_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id


class Icon(models.Model):
    icon_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    lat = models.IntegerField(null=False, default=0)
    lon = models.IntegerField(null=False, default=0)
    memo = models.TextField(null=True)
    # user = models.ForeignKey(User, verbose_name='user', null=False,on_delete=models.CASCADE)
    # map = models.ForeignKey(Map, verbose_name='map', null=False,on_delete=models.CASCADE)
    favorite = models.IntegerField(null=False, default=0)



class Table(models.Model):
    """テーブル一覧"""
    name = models.CharField(max_length=100)

class Column(models.Model):
    """カラム定義（物理名格納）"""
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)



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
