from django.db import models
from django.contrib.auth.models import User


class ItemForBarter(models.Model):
    INCHES = 'Inches'
    FEET = 'Feet'
    YARDS = 'Yards'
    MILES = 'Miles'
    MILLIMETERS = 'Millimeters'
    CENTIMETERS = 'Centimeters'
    METERS = 'Meters'
    KILOMETERS = 'Kilometers'
    Length_Unit_Choices = (
        (INCHES, 'in'),
        (FEET, 'ft'),
        (YARDS, 'yd'),
        (MILES, 'mi'),
        (MILLIMETERS, 'mm'),
        (CENTIMETERS, 'cm'),
        (METERS, 'm'),
        (KILOMETERS, 'km'),
    )
    OUNCES = 'Ounces'
    POUNDS = 'Pounds'
    GRAMS = 'Grams'
    KILOGRAMS = 'Kilograms'
    Weight_Unit_Choices = (
        (OUNCES, 'oz'),
        (POUNDS, 'lbs'),
        (GRAMS, 'g'),
        (KILOGRAMS, 'kg'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    length = models.FloatField()
    length_units = models.CharField(max_length=3, choices=Length_Unit_Choices)
    width = models.FloatField()
    width_units = models.CharField(max_length=3, choices=Length_Unit_Choices)
    height = models.FloatField()
    height_units = models.CharField(max_length=3, choices=Length_Unit_Choices)
    weight = models.FloatField()
    user_id = models.ForeignKey(User)
