# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Имя"}))
    from_email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Тема"}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Сообщение"}), required=True)
