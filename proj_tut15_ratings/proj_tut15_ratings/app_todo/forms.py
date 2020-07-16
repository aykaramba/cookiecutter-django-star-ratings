from django import forms
from .models import Task


class FormTaskCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task',)

class FormTaskUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task', 'complete',)
        
