from django.contrib import admin
from . models import (
    ContactMessage,
    Intro,
    About,
    Project,
    Education,
    Experience,
    Skill,
    Profile,
    ContactInfo,
    Testimonial,
    Images,
    Portfolio,
    Category,
    Certificate,
    )

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'institution', 'course')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'organisation')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'title')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','update_at','status']
    readonly_fields = ('name','email','message','ip')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', 'phone')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name','role', 'is_active')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class PortfolioImageInline(admin.TabularInline):
	model = Images
	extra = 1
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','client')
    inlines = [PortfolioImageInline]
    readonly_fields = ('slug',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','title')
    
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')


admin.site.register(ContactMessage,ContactMessageAdmin)