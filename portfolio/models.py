from django.db import models

# Create your models here.
class Project(models.Model):
# a class named project
    title = models.CharField(max_length=100)
     # a character field named title to input title
    description = models.CharField(max_length=200)
    # a Text field named description to input description
    image = models.ImageField(upload_to='portfolio/images/')
    # a field to get image file; saves the image in media folder
    url = models.URLField(blank=True)
    # a field for URL
    
    def __str__(self):
        return self.title