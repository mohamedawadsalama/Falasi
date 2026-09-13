from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class CustomUser(AbstractUser):
    pass 

def generate_alphanumeric_code():
    # Generates a random 10-character string containing letters and numbers
    return get_random_string(length=10)


class Career(models.Model):
    name = models.CharField('Full Name',max_length=100)
    email = models.EmailField('Email Address', unique=True)
    position = models.CharField('Position',max_length=100)
    phone = models.CharField('Contact Number',max_length=20)
    cover_letter = models.TextField('Cover Letter', max_length=1000)
    cv = models.FileField('Attach CV',upload_to='documents/CVs/')
    date = models.DateTimeField(auto_now_add=True)
    random = models.CharField('Validation Code', max_length=10, default=generate_alphanumeric_code,
                              help_text="This code is used for validation purposes. Please keep it safe.")
    

    def __str__(self):
        return f"{self.name} {self.email} {self.position} {self.date} {self.random}"
    

class Contact(models.Model):
    name = models.CharField('Full Name',max_length=100)
    email = models.EmailField('Email Address')
    subject = models.CharField('Subject',max_length=150)
    message = models.TextField('Message', max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.subject} {self.date}"
    

services_choices=[
    ('Consulting Service', 'Consulting Service'),
    ('Accounting Service', 'Accounting Service'),
    ('Audit Service', 'Audit Service'),
    ('Financial Service', 'Financial Service'),
    ('Advisory Service', 'Advisory Service'),
    ('Transaction Service', 'Transaction Service'),
    ('Taxation Service', 'Taxation Service'),
    ('Liquidation & Insolvency Service', 'Liquidation & Insolvency Service'),
    ('bookkeeping', 'Bookkeeping'),
    ('payroll_services', 'Payroll Services'),
    ('business_valuation', 'Business Valuation'),
    ('forensic_accounting', 'Forensic Accounting'),
    ('management_accounting', 'Management Accounting'),
]

class Enquiry(models.Model):
    name = models.CharField('Full Name',max_length=100)
    email = models.EmailField('Email Address')
    phone = models.CharField('Contact Number',max_length=20)
    service = models.CharField('Service', max_length=50, choices=services_choices)
    details = models.TextField('Details', max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.service} {self.phone} {self.date}"