from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import (ContactMessage,Intro,About,Service,Education,Experience,Skill,Profile,ContactInfo,Testimonial,
		Media,Portfolio,Category,Certificate
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
    portfolios = Portfolio.objects.all()
    certificates = Certificate.objects.all()
    category = []
    
    all_category = [portfolio for portfolio in Category.objects.all()]
    if all_category:
        for count in range(10):
            item = random.choice(all_category)
            if item not in category:
                category.append(item)

    

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

def category_portfolio_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Portfolio.objects.filter(category=category).order_by('-id')
    return render(request, 'portfolio.html', {
        'data': data,
    })
    
class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter()
class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"