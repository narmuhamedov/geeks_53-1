from django.db import models

class Driver(models.Model):
  name = models.CharField(max_length=100)
  license_number = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Car(models.Model):
  driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
  brand = models.CharField(max_length=100)
  date_created = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.brand