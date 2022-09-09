from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import (
		ContactMessage,
		Intro,
		About,
		Service,
		Education,
		Experience,
		Skill,
		UserProfile,
		Testimonial,
		Media,
		Portfolio,
		Certificate,
		Blog
	)

from django.views import generic
from django.views.generic import FormView
from .forms import ContactForm





class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		intros = Intro.objects.filter()
		abouts = About.objects.filter()
		services = Service.objects.filter()
		educations = Education.objects.filter()
		experiences = Experience.objects.filter()
		skills = Skill.objects.filter()
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["intros"] = intros
		context["abouts"] = abouts
		context["services"] = services
		context["educations"] = educations
		context["experiences"] = experiences
		context["skills"] = skills
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context



    

class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"


def ContactView(request):
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
            return HttpResponseRedirect('/contact')
            
    form = ContactForm
    return render(request, "main/contact.html", {'form':form})