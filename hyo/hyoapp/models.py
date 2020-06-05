from django.db import models

class Member(models.Model):
    name= models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    birthday = models.DateTimeField()
    img = models.TextField()

    def __str__(self):
        return self.name

class Family(modles.Model):
    family= models.ForeignKey(Member, on_delete = models.CASCADE, related_name='passwords')
