
from django import forms

from userprofile.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            return forms.ValidationError('两次输入的密码不一致，请重新输入！')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)
