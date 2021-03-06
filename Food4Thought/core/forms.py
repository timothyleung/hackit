from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from core.models import *
from django.forms.widgets import RadioSelect
from django.forms.extras.widgets import SelectDateWidget

class UserAuthForm(AuthenticationForm):
    error_css_class = 'error'
    username = forms.CharField(label = '',
                            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    password = forms.CharField(max_length=200,
                              label='',
                              widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class RequestForm(forms.ModelForm):
    class Meta:
        model=Request
        fields = '__all__'
        exclude = {'lat', 'lon', 'uid'}
        widgets = {
            'order' : forms.TextInput(attrs={'class':'form-control',
                                                     'placeholder': 'Order'}),
            'info' : forms.TextInput(attrs={'class':'form-control',
                                                    'placeholder': 'Info'}),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields = "__all__"
        exclude = {'rid', 'uid', 'stateid', 'read', 'approve'}
        widgets = {
            'offer' : forms.TextInput(attrs={'class':'form-control',
                                                     'placeholder': 'offer'})
        }

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length = 20, 
                                 label = '',
                                 widget = forms.TextInput(attrs={'class':'form-control firstname', 'placeholder':'Full Name'}))

    phone_number = forms.CharField(max_length = 20, 
                                label='',
                                widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Phone Number'}))

    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                             error_messages={'required':'Please enter an email','invalid':'Please enter a valid email address'})

    password1 = forms.CharField(max_length = 200,
                                label = '',
                                widget = forms.PasswordInput(attrs=
{'class':'form-control','placeholder':'Password'}))

    password2 = forms.CharField(max_length = 200,
                                label = '',
                                widget = forms.PasswordInput(attrs=
{'class':'form-control','placeholder':'Confirm Password'}))

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError("Password did not match.")
        return cleaned_data


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__exact=email):
            raise forms.ValidationError("email is already taken.")
        return email


                                                         