from django.db import models

# Create your models here.

class Driver(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    MARITALSTATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Seperated', 'Seperated'),
        ('Divorced', 'Divorced'),
    ]

    driverID = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='Male')
    state = models.CharField(max_length=100)
    age = models.IntegerField()
    phoneNumber = models.PositiveIntegerField()
    maritalStatus = models.CharField(max_length=100, choices=MARITALSTATUS_CHOICES, default='Single')
    email = models.EmailField(max_length=200)
    vehicleID = models.CharField(max_length=200)
    homeAddress = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='static/images/avatar.svg')

    def __str__(self):
        return self.firstName

