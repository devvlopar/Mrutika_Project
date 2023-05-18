from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.email


class Blog(models.Model):
    l1 = [('beauty', 'beauty'), 
          ('fashion', 'fashion'), 
          ('food', 'food'), 
          ('lifestyle', 'lifestyle'), ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=150, choices=l1)
    pic = models.FileField(upload_to= 'blog_photos', default= 'ladki.jpeg')

    def __str__(self) -> str:
        return self.title