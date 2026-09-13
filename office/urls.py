from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/amf-at-a-glance/', views.amfAtaGlance, name='amfAtaGlance'),
    path('about/vision-and-mission/', views.visionAndMission, name='visionAndMission'),
    path('about/our-values/', views.ourValues, name='ourValues'),
    path('about/founder-message/', views.founderMessage, name='founder'),
    path('services/', views.services, name='services'),
    path('services/financial-services/', views.financialServices, name='financialServices'),
    path('services/advisory-services/', views.advisoryServices, name='advisoryServices'),
    path('services/transaction-services/', views.transactionServices, name='transactionServices'),
    path('services/taxation-services/', views.taxationServices, name='taxationServices'),
    path('services/liquidation-services/', views.liquidationServices, name='liquidationServices'),
    path('supportservices/', views.supportservices, name ='supportservices'),
    path('faqs-library/', views.faqsLibrary, name='faqsLibrary'),
    path('faqs/', views.faqs, name='faqs'),
    path('recommended-links/', views.recommendendLinks, name='recommendendLinks'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('ifrs/', views.ifrsUpdates, name='ifrsUpdates'),
    path('taxnewletters/', views.taxNewsletters, name='taxNewsletters'),
    path('qatarlaws/', views.qatarLaws, name='qatarLaws'),
    path('terms-of-conditions/', views.termsOfConditions, name='termsOfConditions'),
    path('privacy-policy/', views.privacyPolicy, name='privacyPolicy'),
]