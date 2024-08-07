

from django import forms
from .models import Appointment
# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['lawyer', 'date', 'reason']

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['lawyer', 'date', 'reason', 'contact_number']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # To select date and time
            'reason': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Reason for appointment...'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter your contact number'}),
        }



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Remove user_type field from the registration form
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')  # Exclude user_type

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'client'  # Default user type is client
        if commit:
            user.save()
        return user

class LawyerCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Exclude user_type

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.user_type = 'lawyer'  # Set user type to lawyer
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#new code 
from django import forms
from .models import CustomUser  # Your custom user model

class AdminLawyerCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    specialization = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser  # Adjust this if you're using a different user model
        fields = ['username', 'email', 'password', 'name', 'specialization']  # Include all necessary fields

#ends