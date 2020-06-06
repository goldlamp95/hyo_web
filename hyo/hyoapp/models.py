from django.db import models
from django.contrib.auth.models import User

class Family(models.Model):
    family_name = models.CharField(max_length =100)
    family_password= models.CharField(max_length = 50)

    def __str__(self):
        return self.family_name

class Member(models.Model):
    name= models.CharField(max_length = 50, null=True)
    individual_id= models.ForeignKey(User, db_column= 'username', on_delete= models.CASCADE, related_name='user_id')
    individual_password= models.ForeignKey(User, db_column= 'password', on_delete= models.CASCADE, related_name='user_password')
    family_password = models.ForeignKey(Family, db_column='family_password', on_delete = models.CASCADE, related_name='passwords')
    birthday = models.DateTimeField(null=True)
    profile = models.TextField(null=True)
    point = models.TextField(null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image= models.TextField()
    content= models.TextField(null=True)
    image_author= models.ForeignKey(Member, on_delete = models.CASCADE, related_name ='images')
    
    def __str__(self):
        return self.image

class Comment(models.Model):
    post= models.ForeignKey(Image, on_delete= models.CASCADE, related_name ='comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comments')
    content = models.TextField(null = True)

    def __str__(self):
        return self.content

