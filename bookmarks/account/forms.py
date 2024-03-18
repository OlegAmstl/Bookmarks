from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Форма для входа в систему."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    """Форма для регистрации пользователя."""

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ('username', 'first_name', 'email')

        def clean_password(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Пароли не совпадают.')
            return cd['password2']
