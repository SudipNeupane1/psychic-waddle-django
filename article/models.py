from django.db import models



class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    

class Categories:
    pass

class Tags:
    pass

class comments:
    pass