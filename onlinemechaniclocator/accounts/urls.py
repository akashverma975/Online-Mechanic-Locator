from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import OwnerSignUpView, MechanicSignUpView, GarageSignUpView, LoginAfterPasswordChange

urlpatterns = [
    path('password/change/', LoginAfterPasswordChange.as_view(), name='account_change_password'),
    path('', include('allauth.urls')),
    path('signup/', TemplateView.as_view(template_name='accounts/choose.html'), name='signup'),
    path('signup/owner/', OwnerSignUpView.as_view(), name='owner_signup'),
    path('signup/mechanic/', MechanicSignUpView.as_view(), name='mechanic_signup'),
    path('signup/garage/', GarageSignUpView.as_view(), name='garage_signup'),
]
