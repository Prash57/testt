from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Calendar(models.Model):
    calendar = models.ImageField(upload_to="uploads/calendar")
    uploaded = models.DateTimeField(auto_now_add=True)
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.uploaded)
    class Meta:
        verbose_name_plural = "00. Calender"


class SchoolSetup(models.Model):
    data_set = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="uploads/logos")
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    opening_hours = models.CharField(max_length=255)
    map_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. School Setup"

class Socials(models.Model):
    data_set = models.CharField(max_length=255)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    linkedIn_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "02. Social Media"

class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_subtitle = models.CharField(max_length=255)
    about_content = models.TextField()
    about_image = models.ImageField(upload_to="uploads/about_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about_title
    
    class Meta:
        verbose_name_plural = "03. About"

class Vision(models.Model):
    vision_title = models.CharField(max_length=255)
    vision_subtitle = models.CharField(max_length=255)
    vision_content = models.TextField()
    vision_image = models.ImageField(upload_to="uploads/vision_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vision_title
    
    class Meta:
        verbose_name_plural = "04. Vision"

class Mission(models.Model):
    mission_title = models.CharField(max_length=255)
    mission_subtitle = models.CharField(max_length=255)
    mission_content = models.TextField()
    mission_image = models.ImageField(upload_to="uploads/mission_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mission_title
    
    class Meta:
        verbose_name_plural = "05. Mission"

class MessageFrom(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to="uploads/message_from_images")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "06. Message From"

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/team_images')
    facebook= models.URLField(null=True, blank=True)
    instagram= models.URLField(null=True, blank=True)
    linkedin= models.URLField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "07. Team Members"

class Testimonial(models.Model):
    name= models.CharField(max_length=200)
    position= models.CharField(max_length=200)
    testimonial= models.TextField()
    image = models.ImageField(upload_to="uploads/testimonial_images/")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "08. Testimonials"

class Courses(models.Model):
    name= models.CharField(max_length=200)
    faculty= models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/course_images/")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "09. Courses"

class Faqs(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "10. FAQs"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="uploads/blogs_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):

            if self.slug == None:
                slug = slugify(self.title)

                has_slug = Blog.objects.filter(slug=slug).exists()
                count = 1
                while has_slug:
                    count += 1
                    slug = slugify(self.title) + '-' + str(count) 
                    has_slug = Blog.objects.filter(slug=slug).exists()

                self.slug = slug

            super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = ("11. Blogs")
        ordering = ['-created_at']


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/gallery_images/")
    created = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return str(self.created)
    
    class Meta:
        verbose_name_plural = ("12. Gallery")
        ordering = ['-created']

class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "13. Contact"
        ordering = ['-created']

class HomeContent(models.Model):
    data_set = models.CharField(max_length=255)
    title_text = models.CharField(max_length=99)
    sub_text = models.CharField(max_length=55)
    button_text = models.CharField(max_length=20)
    button_url = models.URLField()
    banner_image = models.ImageField(upload_to="uploads/hero_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data_set
    
    class Meta:
        verbose_name_plural = "14. Home Content"

class PopupMessage(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(default=None)
    image = models.ImageField(upload_to="uploads/popup_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "15. Popup Message"

class Notice(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="uploads/notice_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "16. Notices"
        ordering = ['-created_at']

class Vacancy(models.Model):
    STATUS_TYPES = (
        ('Open', 'Open'),
        ('Closed', 'Closed')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    number = models.IntegerField()
    deadline = models.DateField()
    desc = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):

            if self.slug == None:
                slug = slugify(self.title)

                has_slug = Vacancy.objects.filter(slug=slug).exists()
                count = 1
                while has_slug:
                    count += 1
                    slug = slugify(self.title) + '-' + str(count) 
                    has_slug = Vacancy.objects.filter(slug=slug).exists()

                self.slug = slug

            super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "17. Vacancy"
        ordering = ['-created_at']


class Comment(models.Model):
    blog = models.ForeignKey(Blog,  related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)
    
    class Meta:
        verbose_name_plural = ('18. Comments')
        ordering = ['-created_at']