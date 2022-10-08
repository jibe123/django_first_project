from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

'''
# one to one relationship
class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Capital(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# one to many relationship
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# many to many relationship
class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    teacher = models.ManyToManyField(Teacher)
    title = models.CharField(max_length=255)
    
'''