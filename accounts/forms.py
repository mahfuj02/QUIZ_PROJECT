from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate

class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()
       # exclude = ('first_name',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='username')
    password = forms.CharField(label='password', widget=forms.TextInput(
        attrs={'type':'password'}
        )
    )
    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
        
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Incorrect username or password')
        return super(UserLoginForm , self ).clean(*args, **kwargs)
