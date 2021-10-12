from django import forms
from .models import Note
from django.forms import ModelForm

class DTinput(forms.DateTimeInput):
    input_type='datetime-local'
    
class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title','due_date','label')
        widgets = {
            'due_date':DTinput(),
        }