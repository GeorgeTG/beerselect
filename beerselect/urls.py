from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('beers.urls')),
    path('', include('django.contrib.auth.urls')),
    path('profile', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'), 
]