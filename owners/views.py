from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .forms import OwnerSignUpForm


class OwnerSignUpView(CreateView):
    model = CustomUser
    form_class = OwnerSignUpForm
    template_name = 'owner_signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)
