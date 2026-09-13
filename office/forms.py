from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox



class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        # Explicitly define fields to avoid security vulnerabilities
        fields = ['name', 'email', 'position', 'phone', 'cover_letter', 'cv', 'random']
        

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'captcha']
    
        
class EnquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 
    
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'service', 'details', 'captcha']