from rest_framework import serializers
from accounts.models import User
from rest_framework import generics
from django.contrib.auth import authenticate
from .models import Ride
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','usertype', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    
class UserSerializerr(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at']

class RideListSerializer(serializers.ModelSerializer):
    rider = UserSerializerr()
    driver = UserSerializerr()
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'driver','pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at']

class RideStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']

class UpdateRideLocationAPIView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

