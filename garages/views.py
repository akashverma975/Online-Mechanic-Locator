from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .forms import GarageSignUpForm


class GarageSignUpView(CreateView):
    model = CustomUser
    form_class = GarageSignUpForm
    template_name = 'garage_signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'garage'
        return super().get_context_data(**kwargs)
