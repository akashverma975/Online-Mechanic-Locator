from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView


class LoginAfterPasswordChange(PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('account_login')
