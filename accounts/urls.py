from django.urls import path, include
from django.views.generic.base import TemplateView
from owners.views import OwnerSignUpView
from mechanics.views import MechanicSignUpView
from garages.views import GarageSignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', TemplateView.as_view(template_name='choose.html'), name='signup'),
    path('signup/owner/', OwnerSignUpView.as_view(), name='owner_signup'),
    path('signup/mechanic/', MechanicSignUpView.as_view(), name='mechanic_signup'),
    path('signup/garage/', GarageSignUpView.as_view(), name='garage_signup'),
]
