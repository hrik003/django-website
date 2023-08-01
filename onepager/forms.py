import email
from tkinter.tix import Form
from turtle import width
from django import forms

class usersForm(forms.Form):
    name1 = forms.CharField(label="Value 1", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    name2 = forms.CharField(label="Value 2", required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    
class contactForm(forms.Form):
    name = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class':"email-bt",'placeholder':"Your Name"}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class':"email-bt",'placeholder':"Your Email"}))
    phone = forms.IntegerField(label="", required=True, widget=forms.NumberInput(attrs={'class':"email-bt",'placeholder':"Your Phone Number"}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':"email-bt",'placeholder':"Your Message"}))