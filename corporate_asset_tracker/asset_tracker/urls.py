
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from asset_tracker.views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, CheckoutViewSet, SubscriberViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'checkouts', CheckoutViewSet)
router.register(r'subscriber', SubscriberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
