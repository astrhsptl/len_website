from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm, forms.Form):
    username = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={      
            'class': 'form_line',
            'placeholder': 'Никнейм'
        }))

    first_name = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Имя'
        }))

    middle_name = forms.CharField(
        max_length=30, label=None, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Отчество',
            'for': 'id_avatar'
        }))

    last_name = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Фамилия'
        }))

    email = forms.EmailField(
        label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Почта'
        }))

    avatar = forms.ImageField(
        required=True, label='Загрузить фото',
        widget=forms.FileInput(attrs={
            'for': 'profile',
            'class': 'main_button form_button',
            'placeholder': 'Загрузить фото',

        }))

    taxpayer = forms.IntegerField(
        min_value=1, max_value=99999999999999, required=True, label=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form_line',
                'placeholder': 'ИНН'
            }))

    password1 = forms.CharField(label=None, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form_line'}))
    password2 = forms.CharField(label=None, widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'form_line'}))


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].label = "Загрузить фото"
        print(self.fields['avatar'].label)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name','middle_name', 'last_name', 'email', 'avatar', 'taxpayer',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
