from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'color']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note title...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your sticky note...'}),
        }
