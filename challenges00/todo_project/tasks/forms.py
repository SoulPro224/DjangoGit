from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'complete','category']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'priority': forms.Select(choices=[(1, 'Faible'), (2, 'Moyenne'), (3, 'Haute')])
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obligatoire. Entrez une adresse email valide.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']