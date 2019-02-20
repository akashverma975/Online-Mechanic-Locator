from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
#from django.contrib import messages


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #messages.info(request, "Thanks for Registering. You're now logged in.")
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def owner_page(request):
    return render(request, 'owner_page.html')


class OwnerPage(LoginRequiredMixin, TemplateView):
    template_name = 'owner_page.html'
