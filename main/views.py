from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import (ContactMessage, Images,Intro,About,Service,Education,Experience,Skill,Profile,ContactInfo,Testimonial,Portfolio,Category,Certificate
	)

from django.views import generic
from django.views.generic import FormView
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # save message to database
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Your message has been sent. Thank you for your interest")
            # send an Email Notication
            subject = "Website Inquiry" 
            body = {
			'name': form.cleaned_data['name'], 
			'email': form.cleaned_data['email'], 
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@paulmeric.com', ['admin@paulmeric.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('')
            
    form = ContactForm
    intros = Intro.objects.filter()
    abouts = About.objects.filter()
    profiles = Profile.objects.filter()
    services = Service.objects.filter()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    contactinfos = ContactInfo.objects.all()
    testimonials = Testimonial.objects.all()
    portfolios = Portfolio.objects.filter()
    certificates = Certificate.objects.all()
    category = []

    context = {
        'intros': intros,
        'abouts': abouts,
        'profiles': profiles,
        'services': services,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'contactinfos': contactinfos,
        'testimonials': testimonials,
        'certificates': certificates,
        'portfolios': portfolios,
        'categories': category,
        'form':form  
    }
    return render(request, 'main/index.html', context)


def portfolio_detail(request,  slug):
    portfolios = Portfolio.objects.get(slug=slug)
    category = Category.objects.all()
    image = Images.objects.filter(item__slug=slug)

    context = {
        "portfolios": portfolios,
        "category": category,
        "images": image,
          }
    return render(request, "main/portfolio-details.html", context)
