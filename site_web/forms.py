from django import forms
import django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Profile


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Mot de passe :', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'mot de passe'}))
    password2 = forms.CharField(label="Confirmation du mot de passe :", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmer mot de passe'}))
    email = forms.CharField(label = "E-mail", required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Adresse mail'}))
    last_name = forms.CharField(label = "Nom",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre nom'}))
    first_name = forms.CharField(label = "Prenoms",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre prenom'}))
    class Meta:
        model = User
        fields = ['username','last_name','first_name', 'email','password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Utilisateur'})}
  
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("Mot de passe :"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Ancien mot de passe"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True, 'class':'form-control', 'placeholder':'Ancien mot de passe'}))
    new_password1 = forms.CharField(label=("Nouveau mot de passe"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Nouveau mot de passe'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirmer le mot de passe"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Confirmer le mot de passe'}))
    

class AjoutProForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['user','website','biography','telephone','photo']