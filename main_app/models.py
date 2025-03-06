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
    
# class Veggie(models.Model):
#     company_name = models.CharField(max_length=50)
#     todo = models.CharField(max_length=100)
#     percent = models.CharField(max_length=50)
#     def __str__(self):
#         return self.company_name
    
class Logistic(models.Model):
    icon= models.CharField(max_length=100)
    mode= models.CharField(max_length=100)
    content= models.CharField(max_length=100)
    def __str__(self):
        return self.mode