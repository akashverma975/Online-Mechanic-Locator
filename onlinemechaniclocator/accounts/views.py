from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import OwnerSignUpForm, MechanicSignUpForm, GarageSignUpForm


class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'owners/owner_signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)


class MechanicSignUpView(CreateView):
    model = User
    form_class = MechanicSignUpForm
    template_name = 'mechanics/mechanic_signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'mechanic'
        return super().get_context_data(**kwargs)


class GarageSignUpView(CreateView):
    model = User
    form_class = GarageSignUpForm
    template_name = 'garages/garage_signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'garage'
        return super().get_context_data(**kwargs)
