from django.urls import path
from .views import login_view, register_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_user, name="authentication-register"),
    path('', login_view, name="authentication-login"),
    path('', auth_views.LogoutView.as_view(template_name='8. user/login.html'), name='authentication-logout'),
]