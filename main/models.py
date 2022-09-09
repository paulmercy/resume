from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.forms import ModelForm
from django.forms import TextInput, Textarea

class Intro(models.Model):
    class Meta:
        verbose_name_plural = 'Intros'
        verbose_name = 'Intro'
    greet = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    intro1 = models.CharField(max_length=50, blank=True, null=True)
    intro2 = models.CharField(max_length=50, blank=True, null=True)
    intro3 = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    bg = models.ImageField(blank=True, null=True, upload_to="bg")

class About(models.Model):
    class Meta:
        verbose_name_plural = 'Abouts'
        verbose_name = 'About'
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    description =RichTextField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    

class Service(models.Model):
    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = 'Service'
    
    title = models.CharField(max_length=20, blank=True, null=True)
    desc = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Education(models.Model):
    class Meta:
        verbose_name_plural = 'Educations'
        verbose_name = 'Education'
    institution = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=11, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

class Experience(models.Model):
    class Meta:
        verbose_name_plural = 'Experiences'
        verbose_name = 'Experience'
    title = models.CharField(max_length=50, blank=True, null=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=11, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True,max_length=50)
    message = models.TextField(blank=True,max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True,max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','message']
        widgets = {
            'name'  : TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
            'email'  : TextInput(attrs={'class': 'input','placeholder':'Email'}),
            'message'  : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }


class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
