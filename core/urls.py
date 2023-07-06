from django.urls import path
from . import views
from .forms import LoginForm

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:index'), name='logout'),

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]