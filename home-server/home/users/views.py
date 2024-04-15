from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User



class UserLoginView(TitleMixin, LoginView):

    template_name = "users/login.html"
    form_class = UserLoginForm
    title = 'Home - Авторизация'



class UserProfileView(TitleMixin, UpdateView):

    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Home - Личный кабинет'

    def get_success_url(self):

        return reverse_lazy('users:profile', args=(self.object.id,))
    

    

class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):

    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    title = 'Home - Регистрация'
    success_url = reverse_lazy('users:login')
    success_message = 'Для окончания регистрации, перейдите по ссылке, отправленной вам на почту!'

