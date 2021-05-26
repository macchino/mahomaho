from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100,  required=False)
    sender = forms.EmailField(label='Email', required=False)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea,  required=False)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)