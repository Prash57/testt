from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.

admin.site.register(SchoolSetup)
admin.site.register(Socials)
admin.site.register(Calendar)
# admin.site.register(Vision)
# admin.site.register(Mission)
# admin.site.register(MessageFrom)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Courses)
# admin.site.register(Faqs)
# admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(HomeContent)
# admin.site.register(PopupMessage)
# admin.site.register(Notice)
# admin.site.register(Vacancy)
admin.site.register(Comment)


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_content')
admin.site.register(About, AboutAdmin)


class MessageFromAdmin(SummernoteModelAdmin):
    summernote_fields = ('message')
admin.site.register(MessageFrom, MessageFromAdmin)


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
admin.site.register(Blog, BlogAdmin)


class FaqsAdmin(SummernoteModelAdmin):
    summernote_fields = ('answer')
admin.site.register(Faqs, FaqsAdmin)


class NoticeAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
admin.site.register(Notice, NoticeAdmin)


class PopupMessageAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
admin.site.register(PopupMessage, PopupMessageAdmin)


class VacancyAdmin(SummernoteModelAdmin):
    summernote_fields = ('desc')
admin.site.register(Vacancy, VacancyAdmin)
