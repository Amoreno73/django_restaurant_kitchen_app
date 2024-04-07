from django.db import models
# a part of django's object-relational mapper
# allows you to define data models entirely in python
from django.contrib.auth.models import User
# built-in authentication system
# provides a fully functional user class for managing user accounts

#look at slide 323 for menu image
MEAL_TYPE = (
    # the first word = used by django
    # second word = used by frontend in website
    ("starters","Starters"),
    ("salads","Salads"),
    ("main_dishes","Main Dishes"),
    ("desserts","Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Item(models.Model):
    meal = models.CharField(max_length = 1000, unique=True)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    meal_type = models.CharField(max_length = 200, choices = MEAL_TYPE)
    # the author field is associated with User table, provided by django
    # it will be a many:1 relationship
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # CASCADE = delete everything for the associated user
    # PROTECT = you will not be able to delete the user and the meals are protected as well
    # SET_NULL = will set foreign key to null
    status = models.IntegerField(choices=STATUS, default = 1)
    # if the status is 0, the selection will be crossed out
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # timestamp is recorded for new/update entries of an item

    def __str__(self):
        return self.meal
    # whenever an object from the class is created, we can see the print of the meal

