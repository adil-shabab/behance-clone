from django.db import models
from accounts.models import Profile

# Create your models here.

class Work(models.Model):
    profile= models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField('tags', blank=True)
    tools_used = models.ManyToManyField('Tools_used', blank=True)
    cover = models.ImageField(upload_to='media', null=True, blank=True)
    imageone = models.ImageField(upload_to='media', null=True, blank=True)
    imagetwo = models.ImageField(upload_to='media', null=True, blank=True)


    def __str__(self):
        return self.title
        


class Tags(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Tools_used(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text