from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]