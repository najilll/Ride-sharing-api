from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User

class RideAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password', usertype='rider')
        self.driver = User.objects.create_user(username='testdriver', email='driver@example.com', password='password', usertype='driver')

    def test_create_ride_invalid_data(self):
        url = reverse('create_ride') 
        invalid_data = {
            'rider': self.user.id,  
            'driver': self.driver.id,  
            'pickup_location': 'Location C',
            'dropoff_location': 'Location D',
            'status': 'requested'
        }
        self.client.force_authenticate(user=self.user) 
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)