from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=50)
    schools = models.ManyToManyField(School,blank=True)
    def __str__(self):
        return self.name
class Circle(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class FormKuModel(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    camera = models.BooleanField()
    content = models.TextField()
    def __str__(self):
        return self.title

class FormKgModel(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    camera = models.BooleanField()
    content = models.TextField()
    def __str__(self):
        return self.title

class FormDuModel(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    camera = models.BooleanField()
    content = models.TextField()
    def __str__(self):
        return self.title

class FormRuModel(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    camera = models.BooleanField()
    content = models.TextField()
    def __str__(self):
        return self.title
