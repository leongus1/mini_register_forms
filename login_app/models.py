from django.db import models
from django.core.exceptions import ValidationError
import re


#Validators
def validateGreaterThanTwo(value):
    if len(value)<2:
        raise ValidationError(
            '{} must be longer than 2 characters'.format(value)
        )

def validateGreaterThanEight(value):
    if len(value)<8:
        raise ValidationError(
            '{} must be longer than 8 characters'.format(value)
        )

def validateEmail(value):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(value):
        raise ValidationError(
            '{} email format is not valid'
        )
        
    

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255, validators=[validateGreaterThanTwo])
    last_name=models.CharField(max_length=255, validators=[validateGreaterThanTwo])
    email= models.EmailField(validators=[validateEmail])
    password=models.CharField(max_length=100, validators=[validateGreaterThanEight])
    # confirm_password= models.CharField(max_length=100, validators=[validateGreaterThanEight])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
        
    


