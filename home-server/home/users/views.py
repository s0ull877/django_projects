from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm
from users.models import User



class UserLoginView(TitleMixin, LoginView):

    template_name = "users/login.html"
    form_class = UserLoginForm
    title = 'Home - Авторизация'



class UserProfile(TitleMixin, UpdateView):

    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Home - Личный кабинет'
    

