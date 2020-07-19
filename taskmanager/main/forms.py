from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "text"]
        widgets = {'title': TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter title'}),
                   'text': Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Enter description'})}
