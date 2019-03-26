from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(label='subject', max_length=100)
	message = forms.CharField(label='message', widget=forms.Textarea)
	sender = forms.EmailField(label='sender', )
	cc_myself = forms.BooleanField(label='cc', required=False)