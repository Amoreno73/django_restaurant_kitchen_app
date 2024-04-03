from django.db import models
from django.contrib.auth.models import User

#look at slide 323 for menu image
MEAL_TYPE = (
    # the first word = used by django
    # second word = used by frontend in website
    ("starters","Starters")
    ("salads","Salads")
    ("main_dishes","Main Dishes")
    ("desserts","Desserts")
)

class Item(models.Model):
    meal = models.CharField(max_length = 1000, unique=True)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(decimal_places=2)
    meal_type = models.CharField(choice = MEAL_TYPE)
    author = models.ForeignKey(User)
    # the author field is associated with User table, provided by django
    # it will be a many:1 relationship
    
#left off on slide 327