from django import forms
from mysite.useraccount.models import UserProfile


class RegisterForm(forms.ModelForm):
    confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm',
                  'birth_date']

    def clean_confirm(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2
