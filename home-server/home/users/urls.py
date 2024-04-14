from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserProfileView, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
]
