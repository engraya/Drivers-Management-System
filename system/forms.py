from django import forms
from .models import Driver
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class DriverForm(forms.ModelForm):
    age = forms.CharField(max_length=100)
    maritalStatus = forms.CharField(max_length=100)
    class Meta:
        model = Driver
        fields = '__all__'
        exclude = ['driverID']
        labels = {
            'driverID' : 'Drivers ID',
            'firstName' : 'First Name',
            'lastName' : 'Last Name',
            'gender' : 'Gender',
            'state' : 'State of Origin',
            'age' : 'Age',
            'phoneNumber' : 'Phone Number',
            'maritalStatus' : 'Marital Status',
            'email' : 'Email Address',
            'homeAddress' : 'Home Address',
            'vehicleID' : 'Vehicle ID',
            'facebook' : 'Facebook',
            'linkedin' : 'Linkedin',
            'instagram' : 'Instagram',
            'twitter' : 'Twitter',
        }
        widgets = {
            'driverID' : forms.TextInput(attrs={'class' : 'form-control'}),
            'firstName' : forms.TextInput(attrs={'class' : 'form-control'}),
            'lastName' : forms.TextInput(attrs={'class' : 'form-control'}),
            # 'gender' : forms.ChoiceField(attrs={'class' : 'form-control'}),
            'state' : forms.TextInput(attrs={'class' : 'form-control'}),
            'age' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phoneNumber' : forms.NumberInput(attrs={'class' : 'form-control'}),
            # 'maritalStatus' : forms.ChoiceField(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'homeAddress' : forms.TextInput(attrs={'class' : 'form-control'}),
            'vehicleID' : forms.TextInput(attrs={'class' : 'form-control'}),
            'facebook' : forms.TextInput(attrs={'class' : 'form-control'}),
            'linkedin' : forms.TextInput(attrs={'class' : 'form-control'}),
            'instagram' : forms.TextInput(attrs={'class' : 'form-control'}),
            'twitter' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'type' : 'text',
            'name' : 'first_name',
            'class' : 'form-control',
            'placeholder' : 'Enter your First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'type' : 'text',
            'name' : 'last_name',
            'class' : 'form-control',
            'placeholder' : 'Enter your Last Name'
        })
        self.fields['username'].widget.attrs.update({
            'type' : 'text',
            'name' : 'username',
            'class' : 'form-control',
            'placeholder' : 'Choose your Username Name'
        })
        self.fields['email'].widget.attrs.update({
            'type' : 'text',
            'name' : 'email',
            'class' : 'form-control',
            'placeholder' : 'Enter your Email Address here'
        })
        self.fields['password1'].widget.attrs.update({
            'type' : 'text',
            'name' : 'password',
            'class' : 'form-control',
            'data-type' : 'password',
            'placeholder' : 'Enter your Password here'
        })
        self.fields['password2'].widget.attrs.update({
            'type' : 'text',
            'name' : 'password',
            'class' : 'form-control',
            'data-type' : 'password',
            'placeholder' : 'Confirm your Password here'
        })
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'user', 'type' : 'text', 'class':'input','placeholder': 'Enter Your Username here'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'user', 'type' : 'text', 'class': 'input', 'data-type' : 'password', 'placeholder': 'Enter Your Password here'}))



