from django.db import models
from django.contrib.auth.models import User

class HomeType(models.Model):
  home_type = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.home_type

class propertie(models.Model):
  PROPERTY_CHOICES = (
    ('S', 'Sale'),
    ('R', 'Rent'),
  )

  address = models.CharField(max_length=100)
  bedroom = models.IntegerField(default=0)
  bathroom = models.IntegerField(default=0)
  zipcode = models.CharField(max_length=5)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  square_feet = models.IntegerField(default=0)
  unit = models.CharField(max_length=20)
  property_type = models.CharField(max_length=1, choices=PROPERTY_CHOICES, default="S")
  description = models.CharField(max_length=200)
  longitude = models.FloatField(default=0)
  latitude = models.FloatField(default=0)
  property_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  home_type_id = models.ForeignKey(HomeType, on_delete=models.CASCADE, default=None, verbose_name="Home Type")
  rooms = models.IntegerField(default=0)
  contact_number = models.CharField(max_length=50)

  def __str__(self):
    return self.address


  class Meta:
    verbose_name = 'Property'
    verbose_name_plural = 'Properties'