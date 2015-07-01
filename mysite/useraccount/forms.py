from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField


class RegisterForm(forms.ModelForm):
    confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'confirm',
                  'birth_date', 'avatar']

    def clean_confirm(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2


class ChangePassForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    confirm = forms.CharField(widget=forms.PasswordInput, min_length=6)

    def clean_confirm(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2


class EditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'email', 'avatar']