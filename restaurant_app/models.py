from django.db import models
# importing user class from django
from django.contrib.auth.models import User

# by the command python manage.py migrate.
# This command will go through files in the migrate.execute the code of  0001.
# That was a file that was generated by the makemigrations commands.
# That file will now be executed by the migrate command.

# a tuple of tuples. And each tuple will have two strings.
MEAL_TYPE= (
    ('starters','Starters'),
    ('main_course', 'Main Course'), 
    ('desserts', 'Desserts'))

STATUS = (
    (0,"Unavailable"),
    (1,"Available")
)
# these are the data is display on the website
class Item(models.Model):
    # instructing Django to create a column in the table of our database.
    # maximum length off 1000 characters. unique is preventing duplicate values
    meal = models.CharField(max_length=1000, unique =True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    meal_type = models.CharField(max_length=200,choices =MEAL_TYPE)
    # not be able to delete the user since it is protected
    author= models.ForeignKey(User, on_delete = models.PROTECT)
    status = models.IntegerField(choices=STATUS, default = 1)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meal