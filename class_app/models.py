from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=50)
    types = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50)
    clubs = models.ManyToManyField(Club)

    def __str__(self):
        return self.name


class Circle(models.Model):
    name = models.CharField(max_length=50)
    tweet_link = models.CharField(max_length=200,null=True,blank=True)
    inst_link = models.CharField(max_length=200,null=True,blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Zoom_list(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.school.name