from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label=" Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label=" Confirm Password")
    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Passwords no son iguales x_x')
        return self.data['password']
    def clean(self,*args, **kwargs):
        #self.clean_email()
        self.clean_password()
        return super(UserForm, self).clean(*args, **kwargs)

    class Meta:
        model = User
        #fields = ['username', 'password', 'email', 'first_name', 'last_name']
        fields = ['username', 'password','email',]
        widgets = {
            'password': forms.PasswordInput(),
            #'password1': forms.PasswordInput(),
        }

