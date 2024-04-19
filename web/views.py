from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import logout
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Ride
from .serializers import RideSerializer,RideStatusUpdateSerializer,RideListSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful", "user": UserSerializer(user).data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})

class CreateRideAPIView(generics.CreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [AllowAny]

class RideDetailsAPIView(generics.RetrieveAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class ListRidesAPIView(generics.ListAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideListSerializer

class UpdateRideStatusAPIView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class UpdateRideStatusAPIView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideStatusUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
