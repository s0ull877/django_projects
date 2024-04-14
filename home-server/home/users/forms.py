from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш пароль',
    }))


    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
        "is_not_veryfied":_("This account is not verifyed. Check your email."),
    }


    def confirm_login_allowed(self, user):

        if not user.is_verified:
            raise ValidationError(
                self.error_messages["is_not_veryfied"],
                code="is_not_veryfied",
            )

        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )


    class Meta:

        model = User
        fields = ('username','password')


class UserProfileForm(UserChangeForm):

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': "form-control mt-3",
        'accept': "image/*"
    }), required=False)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'readonly': True
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'readonly': True
    }))


    class Meta:

        model = User
        fields = ('image','first_name','last_name','username','email')



class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вашу фамилию',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя пользователя',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш адрес эл. почты',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш пароль',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль',
    }))


    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
