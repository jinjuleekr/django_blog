from django.db import models
from django.conf import settings

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name