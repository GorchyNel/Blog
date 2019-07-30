from django import forms
from .models import Publication, Tag, Rubric
import datetime

class PublicationForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Text = forms.CharField(widget=forms.Textarea)
    Image = forms.FileField()
    IsVisible = forms.BooleanField()
    DelayedPosting = forms.DateField()
