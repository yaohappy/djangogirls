from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)


    def __str__(self):
        return self.title
