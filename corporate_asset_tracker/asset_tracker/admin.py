from django.contrib import admin
from .models import Company, Employee, Device, Checkout

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone_number')
    search_fields = ('name', 'location', 'email', 'phone_number')
    list_filter = ('location', 'email', 'phone_number')
    ordering = ('location', 'email')
    readonly_fields = ('name', 'location')




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',  'company')
    search_fields = ('first_name', 'last_name', 'company__name')
    list_filter = ('company', )
    ordering = ('-date_joined',)



@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'company')
    search_fields = ('name', 'serial_number', 'company__name')
    list_filter = ('company', )
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    empty_value_display = 'No data available'
    autocomplete_fields = ('company',)


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'checked_out_date', 'checked_in_date')
    list_filter = ('device', 'employee')
    readonly_fields = ('checked_out_date',)
    autocomplete_fields = ('device', 'employee')
    ordering = ('checked_out_date',)
    date_hierarchy = 'checked_out_date'
    search_fields = ('device__name', 'employee__name')
    

    

    

    



