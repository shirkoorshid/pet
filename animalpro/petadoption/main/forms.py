from django import forms
from .models import BlogPost



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='שם')
    email = forms.EmailField(label='אימייל')
    message = forms.CharField(widget=forms.Textarea, label='הודעה')

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='תגובה')
