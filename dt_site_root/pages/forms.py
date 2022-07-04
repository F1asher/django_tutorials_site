from django import forms


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your email address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

