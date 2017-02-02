from django import forms
from .models import Notes

class NoteForm(forms.Form):
	title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder':'Insert note title here...'}), label="")

