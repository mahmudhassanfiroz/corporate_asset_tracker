from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Company, Employee, Device, Checkout, Subscriber
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, CheckoutSerializer, SubscriberSerializer


# Create your views here.

# Create a view set all the companies
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# Create a view set all the employees of a company   
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create a view set all the devices of a company
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
# Create a view set all the checkout of a company
class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Create a new subscriber and perform payment/subscription logic
        new_subscriber = serializer.save()
        # Process payment and subscription logic here
        
        if new_subscriber:  # Assuming the subscription was successful
            return Response({"message": "Subscriber created successfully."}, status=201)
        else:
            return Response({"message": "Failed to create subscriber."}, status=400)
