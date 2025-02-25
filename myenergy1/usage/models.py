from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Building(models.Model):
    address = models.CharField(max_length=255)
    housetype = models.CharField(max_length=255)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

class Reading(models.Model):
    timeslot = models.DateTimeField()
    duration= models.CharField(max_length=10, default='HOURLY')
    reading = models.FloatField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.datetime} - {self.reading}"
    
'''
from usage.models import Customer, Building, Reading
from django.utils import timezone
from datetime import timedelta

customer = Customer(firstname='Emil', lastname='Refsnes')
customer.save()
member1 = Customer(firstname='Tobias', lastname='Refsnes')
member2 = Customer(firstname='Linus', lastname='Refsnes')
member3 = Customer(firstname='Lene', lastname='Refsnes')
member4 = Customer(firstname='Stale', lastname='Refsnes')
member5 = Customer(firstname='Jane', lastname='Doe')
members_list = [member1, member2, member3, member4, member5]
for x in members_list:
  x.save()

Customer.objects.all().values()
customer = Customer.objects.get(id=1)

building = Building(address='3rd house', housetype='Small',owner=customer)
building.save()
Building.objects.all().values()

timeslots = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18","19", "20", "21","22", "23", "00"]

for x in timeslots:
    reading =Reading(building_id=1, reading=100, datetime='2025-02-18 '+ x +':00:00.000000') 
    reading.save()
Reading.objects.all().values()

'''