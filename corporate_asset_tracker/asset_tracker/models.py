from django.db import models
from django.core.validators import RegexValidator
from .constants import COUNTRIES 



# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=COUNTRIES)

# Create a model for a company
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, validators=[RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )], help_text="Enter the phone number of the employee.")    
    address = models.TextField(blank=True)
    description = models.TextField(max_length=255, blank=True)

    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

# Create a model for an employee
class Employee(models.Model):
    first_name = models.CharField(max_length=50, help_text="Enter the first name of the employee.")
    last_name = models.CharField(max_length=50, help_text="Enter the last name of the employee.")
    email = models.EmailField(unique=True, help_text="Enter the email address of the employee.")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', help_text="Select the company the employee belongs to.")
    phone_number = models.CharField(max_length=20, blank=True, validators=[RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )], help_text="Enter the phone number of the employee.")
    address = models.TextField(blank=True, null=True, help_text="Enter the address of the employee.")
    date_joined = models.DateField(auto_now=True, help_text="The date the employee joined the company.")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create a model for a device
class Device(models.Model):
    name = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices')
    serial_number = models.CharField(max_length=50, blank=True, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

# Create a model for a checkout
class Checkout(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='checkouts')
    checked_out_date = models.DateTimeField()
    checked_in_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"{self.device} - Checked Out: {self.checked_out_date}, Returned: {self.checked_in_date}"


class Subscriber(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='subscribers')
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )])
    address = models.TextField(blank=True)
    subscribed_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
