from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class LogUsuarioForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditForm(forms.Form):
    username = forms.CharField(label="Usuario")
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Modificar Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1",
                  "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'genero', 'descripcion',
                  'contenido', 'imagen')

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'usuario_id', 'type': 'hidden'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': RichTextField(forms.Textarea(attrs={'class': 'form-control'})),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'genero', 'descripcion',
                  'contenido', 'imagen')

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'usuario_id', 'type': 'hidden'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': RichTextField(forms.Textarea(attrs={'class': 'form-control'})),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
