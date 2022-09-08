from django.contrib import admin
from . models import (
    Intro,
    About,
    Service,
    Education,
    Experience,
    Skill,
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Certificate,
    Blog
    )

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'institution')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)
    
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)