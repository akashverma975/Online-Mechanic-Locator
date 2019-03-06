from django.urls import path, include
from .views import LoginAfterPasswordChange

urlpatterns = [
    path('password/change/', LoginAfterPasswordChange.as_view(), name='account_change_password'),
    path('', include('allauth.urls')),
]
