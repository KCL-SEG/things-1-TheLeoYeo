from django.db import models
from django.forms import ValidationError



class Thing(models.Model):
    def quantity_validator(value):
        if value > 100 or value < 0:
            raise ValidationError("value is not in the interval [0, 100]")
        
    name = models.CharField(max_length=30, unique=True) 
    description = models.CharField(blank=True, max_length=120)
    quantity = models.PositiveIntegerField(validators=[quantity_validator])
    
    
