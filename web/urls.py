from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView,UpdateRideStatusAPIView ,CreateRideAPIView, RideDetailsAPIView, ListRidesAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register_user'),
    path('login/', UserLoginAPIView.as_view(), name='login_user'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('rides/create/', CreateRideAPIView.as_view(), name='create_ride'),
    path('rides/<int:pk>/', RideDetailsAPIView.as_view(), name='ride_details'),
    path('rides/', ListRidesAPIView.as_view(), name='list_rides'),
    path('rides/<int:pk>/update-status/', UpdateRideStatusAPIView.as_view(), name='update_ride_status'),
]
