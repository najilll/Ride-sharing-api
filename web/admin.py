# admin.py
from django.contrib import admin
from .models import Ride

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('rider__username', 'driver__username', 'pickup_location', 'dropoff_location')
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return self.readonly_fields + ('rider', 'driver')  
        return self.readonly_fields

