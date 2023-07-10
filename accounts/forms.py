from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm, forms.Form):
    username = forms.CharField(
        max_length=30, label='Имя', required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Имя'
        }))

    first_name = forms.CharField(
        max_length=30, label='Фамилия', required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Фамилия'
        }))

    last_name = forms.CharField(
        max_length=30, label='Отчество', required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Отчество'
        }))

    email = forms.EmailField(
        label='Почта', required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Почта'
        }))

    avatar = forms.FileField(
        required=False, label='Загрузить фото',
        widget=forms.FileInput(attrs={
            'for': 'profile',
            'class': 'main_button form_button',
            'placeholder': 'Загрузить фото'
        }))

    taxpayer = forms.IntegerField(
        min_value=10, max_value=12, required=False, label='ИНН',
        widget=forms.TextInput(
            attrs={
                'class': 'form_line',
                'placeholder': 'НИИ'
            }))
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'avatar', 'taxpayer',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
