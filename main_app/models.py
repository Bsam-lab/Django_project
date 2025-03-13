from django.db import models

# Create your models here.
class Heading(models.Model):
    address = models.CharField(max_length=200)
    email = models.URLField()
    def __str__(self):
        return self.address
    
class Title(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Downbase(models.Model):
    social_handle = models.URLField()
    def __str__(self):
        return self.social_handle
    
class Vegie(models.Model):
    name = models.CharField(max_length=50)
    offer = models.CharField(max_length=100)
    rate = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Logistic(models.Model):
    icon= models.CharField(max_length=100)
    mode= models.CharField(max_length=100)
    content= models.CharField(max_length=100)
    def __str__(self):
        return self.mode
    
class Testimony(models.Model):
    testimony= models.CharField(max_length=200)
    image_testimony = models.ImageField(upload_to='img/')
    testimony_name= models.CharField(max_length=100)
    profession= models.CharField(max_length=100)