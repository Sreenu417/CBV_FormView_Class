from django.db import models


from django.core import validators
# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100, validators=[validators.MaxLengthValidator(10)])
    Sid=models.IntegerField(primary_key=True)
    Saddress=models.TextField(max_length=300,validators=[validators.MinLengthValidator(50)])


    def __str__(self):
        return self.Sname
    
