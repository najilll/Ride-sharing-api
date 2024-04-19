from django.db import models
from accounts.models import User
# Create your models here.

class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    rider = models.ForeignKey(User, limit_choices_to={"usertype": "rider"},on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(User, limit_choices_to={"usertype": "driver"},on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Ride #{self.pk} - {self.rider.username} {self.pickup_location} to {self.dropoff_location} ({self.status})"
