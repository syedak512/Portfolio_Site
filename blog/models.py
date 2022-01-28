from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Blog(models.Model):
# a class named blog
    title = models.CharField(max_length=150)
    # a character field named title to input title
    description = models.TextField()
    # a Text field named description to input description
    date = models.DateField()
    # a Date field to input date
    
    def __str__(self):
        return self.title