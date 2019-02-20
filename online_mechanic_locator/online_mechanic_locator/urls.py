

from django.contrib import admin
from django.urls import path, include
from owner import views as owner_view

urlpatterns = [
    path('', owner_view.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', owner_view.signup, name='signup'),
    path('owner/', owner_view.owner_page, name='owner_page'),
    path('owner2/', owner_view.OwnerPage.as_view(), name='owner_page2'),
    path('admin/', admin.site.urls),
]
