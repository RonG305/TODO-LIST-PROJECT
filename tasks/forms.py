from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
         
        ]

        # labels = {
        #     'title': 'Title',
        #     'date': 'Date'
            
        # }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            
        }