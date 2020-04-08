from django import forms
from .models import *

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ('content','name', 'image',)
