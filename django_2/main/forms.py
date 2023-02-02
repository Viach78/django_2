from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст задачи'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время'
            }),
        }


