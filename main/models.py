from django.db import models
from django.utils.html import mark_safe
from django.template.defaultfilters import slugify
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea

class Intro(models.Model):
    class Meta:
        verbose_name_plural = '2. Intros'
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
        verbose_name_plural = '3. Abouts'
        verbose_name = 'About'
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    

class Project(models.Model):
    class Meta:
        verbose_name_plural = '4. Projects'
        verbose_name = 'Project'
    
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="Project")
    
    def __str__(self):
        return self.title

class Education(models.Model):
    class Meta:
        verbose_name_plural = '6. Educations'
        verbose_name = 'Education'
    institution = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=11, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Experience(models.Model):
    class Meta:
        verbose_name_plural = '7. Experiences'
        verbose_name = 'Experience'
    title = models.CharField(max_length=80, blank=True, null=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=11, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    class Meta:
        verbose_name_plural = '8. Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=80, blank=True, null=True)
    score = models.IntegerField(default=60, blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Profile(models.Model):

    class Meta:
        verbose_name_plural = '1. Profiles'
        verbose_name = 'Profile'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics/',blank=True, null=True, default='profile_pics/default.png')
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)


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

class ContactInfo(models.Model):
    class Meta:
        verbose_name_plural = '9. ContactInfos'
        verbose_name = 'ContactInfo'
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    tel = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    dribbble = models.URLField(max_length=500, blank=True, null=True)
    twitter = models.URLField(max_length=500, blank=True, null=True)
    linkedin = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    github = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.email

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

class Category(models.Model):
    title=models.CharField(max_length=100)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    
    class Meta:
        verbose_name_plural='Portfolios Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('category', kwargs={'slug':self.slug})

class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'
        ordering = ["client"]
    title = models.CharField(max_length=50, blank=True, null=True)
    projectdesc = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    technologies = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    projecturl = models.URLField(max_length=500, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("portfolio_detail", kwargs={'slug': self.slug})


    def __str__(self):
        return self.title
    
class Images(models.Model):
    class Meta:
        verbose_name_plural = 'Images'
        verbose_name = 'Image'
    item = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/')
        
    def __str__(self):
        return self.title

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
