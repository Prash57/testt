from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
    
 
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})


class SchoolSetupForm(forms.ModelForm):
    class Meta:
        model = SchoolSetup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SchoolSetupForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})


class SocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SocialsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'about_content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VisionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class MessageFromForm(forms.ModelForm):
    class Meta:
        model = MessageFrom
        fields = '__all__'

        widgets = {
            'message': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(MessageFromForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CoursesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class FaqsForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = '__all__'
        widgets = {
            'answer': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(FaqsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'sub_title', 'author', 'content', 'image']
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control border-1'})



class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HomeContentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class PopupMessageForm(forms.ModelForm):
    class Meta:
        model = PopupMessage
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PopupMessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})



class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        # fields = '__all__'
        fields = ['title', 'number', 'deadline', 'desc', 'status']
        widgets = {
            'desc': SummernoteWidget(),
        }
   
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

   
    def __init__(self, *args, **kwargs):
        super(VacancyForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})
            

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {'blog_id': forms.HiddenInput()}  

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border-1'})

