from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def amfAtaGlance(request):
    return render(request, 'amf-at-a-glance.html')

def visionAndMission(request):
    return render(request, 'visionandmission.html')

def ourValues(request):
    return render(request, 'our-values.html')

def founderMessage(request):
    return render(request, 'founder-message.html')

def services(request):
    return render(request, 'services.html')

def supportservices(request):
    return render(request, 'supportservices.html')

def careers(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saves directly to the database
            return redirect('home')
    else:
        messages.error(request, 'All fields are required')
        form = CareerForm()
    return render(request, 'careers.html',  {'form': form})

def faqs(request):
    return render(request, 'faqs.html')

def faqsLibrary(request):
    return render(request, 'faqs-library.html')

def recommendendLinks(request):
    return render(request, 'recommended-links.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def enquiry(request):
    if request.method == 'POST':
            form = EnquiryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = EnquiryForm()        
    return render(request, 'enquiry.html', {'form': form})


def financialServices(request):
    return render(request, 'financial-services.html')

def advisoryServices(request):
    return render(request, 'advisory-services.html')

def transactionServices(request):
    return render(request, 'transaction-services.html')

def taxationServices(request):
    return render(request, 'taxation-services.html')

def liquidationServices(request):
    return render(request, 'liquidation-services.html')

def ifrsUpdates(request):
    return render(request, 'ifrs.html')

def taxNewsletters(request):
    return render(request, 'taxnewletters.html')

def qatarLaws(request):
    return render(request, 'qatarlaws.html')

def privacyPolicy(request):
    return render(request, 'privacypolicy.html')

def termsOfConditions(request):
    return render(request, 'termsofconditions.html')

