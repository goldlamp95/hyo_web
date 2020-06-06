from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    family_name = models.CharField(max_length =100)
    family_password= models.CharField(max_length = 50)


class Member(models.Model):
    name= models.CharField(max_length = 50)
    individual_id= models.CharField(max_length = 50)
    individual_password= models.CharField(max_length =50)
    family_password = models.ForeignKey(Family, db_column= 'family_password', on_delete = models.CASCADE, related_name ='passwords')
    birthday = models.DateTimeField()
    profile = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    image= models.TextField()
    content= models.TextField(null=True)
    image_author= models.ForeignKey(User, on_delete = models.CASCADE, related_name ='images')

class Comment(models.Model):
    post= models.ForeignKey(Image, on_delete= models.CASCADE, related_name ='comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comments')
    content = models.TextField(null = True)

class Todolist (models.Model):
    task = models.CharField(max_length = 100)
    due = models.DateTimeField()
    list_author = models.ForeignKey(User, on_delete = models.CASCADE, related_name ='lists')
    tag = models.ForeignKey(User, on_delete = models.CASCADE, related_name='lists')

    def __str__(self):
        return self.task

