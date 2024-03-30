from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# custom 404 page
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# user login
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'dashboard')
        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'login_register.html')
    

# user logout
def logoutUser(request):
    logout(request)
    messages.info(request, 'User Logged Out')

    return redirect('login')

# user registration
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User Registred')

            login(request, user)
            return redirect('dashboard')  

        else:
            messages.error(request, 'User not registered')

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)

# dashboard view
@login_required(login_url = 'login')
def dashboard(request):
    context = {}
    return render(request, 'dash.html', context)

# homepage
def home(request):
    context = {}
    if HomeContent.objects.all().exists():
        home_content = HomeContent.objects.filter()[:1].get()
        context = {'home_content': home_content}
    return render (request, 'index.html', context)

# view school setup data
@login_required(login_url = 'login')
def viewSchool(request):
    context = {}
    return render(request, 'base/viewschool.html', context)

# add school setup
@login_required(login_url = 'login')
def addSchool(request):
    school = SchoolSetup.objects.all()
    form = SchoolSetupForm()
    if request.method == 'POST':
        form = SchoolSetupForm(request.POST, request.FILES)
        if form.is_valid():
            school = form.save(commit=False)
            school.save()

            messages.success(request, 'School setup saved successfully')
            return redirect('home')
    context ={'form': form, 'school': school}
    return render (request, 'base/schoolform.html', context)

# edit school setup
@login_required(login_url = 'login')
def editSchool(request, pk):
    school = SchoolSetup.objects.get(id=pk)
    form = SchoolSetupForm(instance=school)
    if request.method == 'POST':
        form = SchoolSetupForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()

            messages.success(request, 'School setup updated successfully')
            return redirect('home')
    context ={'form': form}
    return render (request, 'base/schoolform.html', context)


# delete school setup
@login_required(login_url = 'login')
def deleteSchool(request, pk):
    school = SchoolSetup.objects.get(id=pk)
    if request.method == 'POST':
        school.delete()

        messages.success(request, 'School setup deleted successfully')
        return redirect('home')
    context ={'obj': school}
    return render (request, 'delete.html', context)

# view socials
@login_required(login_url = 'login')
def viewSocials(request):
    context = {}
    return render(request, 'base/viewsocials.html', context)

# add social content
@login_required(login_url = 'login')
def addSocial(request):
    social = Socials.objects.all()
    form = SocialsForm()
    if request.method == 'POST':
        form = SocialsForm(request.POST)
        if form.is_valid():
            social = form.save(commit=False)
            social.save()

            messages.success(request, 'Socials added successfully')
            return redirect('home')
    context = {'social': social, 'form': form}
    return render(request, 'base/socialform.html', context)

# edit social content
@login_required(login_url = 'login')
def editSocial(request, pk):
    social = Socials.objects.get(id=pk)
    form = SocialsForm(instance=social)
    if request.method == 'POST':
        form = SocialsForm(request.POST, instance=social)
        if form.is_valid():
            form.save()

            messages.success(request, 'Socials updated successfully')
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/socialform.html', context)

# delete social content
@login_required(login_url = 'login')
def deleteSocial(request, pk):
    social = Socials.objects.get(id=pk)
    if request.method == 'POST':
        social.delete()

        messages.success(request, 'Socials deleted successfully')
        return redirect('home')
    context ={'obj': social}
    return render (request, 'delete.html', context)

# view home content
@login_required(login_url = 'login')
def viewHomeContent(request):
    context = {}
    if HomeContent.objects.all().exists():
        home_content = HomeContent.objects.filter()[:1].get()
        context = {'home_content': home_content}
    return render(request, 'base/viewhomecontent.html', context)

# add home content 
@login_required(login_url = 'login')
def addHomeContent(request):
    home_content = HomeContent.objects.all()
    form = HomeContentForm()
    if request.method == 'POST':
        form = HomeContentForm(request.POST, request.FILES)
        if form.is_valid():
            home_content = form.save(commit=False)
            home_content.save()

            messages.success(request, 'Home content saved successfully')
            return redirect('home')
    context ={'form': form, 'home_content': home_content}
    return render (request, 'base/homecontentform.html', context)

# edit home content 
@login_required(login_url = 'login')
def editHomeContent(request,pk):
    home_content = HomeContent.objects.get(id=pk)
    form = HomeContentForm(instance=home_content)

    if request.method == 'POST':
        form = HomeContentForm(request.POST, request.FILES, instance=home_content)
        if form.is_valid():
            form.save()

            messages.success(request, 'Home content updated successfully')
            return redirect('home')
        

    context = {'form': form}
    return render(request, 'base/homecontentform.html', context)

# delete home content
@login_required(login_url = 'login')
def deleteHomeContent(request,pk):
    home_content = HomeContent.objects.get(id=pk)
    if request.method == 'POST':
        home_content.delete()
        
        messages.success(request, 'Home content deleted successfully')
        return redirect('home')
    context = {'obj': home_content}
    return render(request, 'delete.html', context)

# view about
@login_required(login_url = 'login')
# def viewAbout(request):
#     context = {}
#     if About.objects.all().exists():
#         about = About.objects.filter()[:1].get()
#         context = {'about': about}
#     return render(request, 'base/viewabout.html', context)
def viewAbout(request):
    abouts = About.objects.all()
    context = {'abouts': abouts}
    return render(request, 'base/viewabout.html', context)

# about page
# def about(request):
#     context = {}
#     if About.objects.all().exists():
#         about = About.objects.filter()[:1].get()
#         context = {'about': about}
#     return render (request, 'about.html', context)

def about(request):
    abouts = About.objects.all()
    context = {'abouts': abouts}
    return render(request, 'abt.html', context)

# add about section
@login_required(login_url = 'login')
def addAbout(request):
    abouts = About.objects.all()
    form = AboutForm()
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            abouts = form.save(commit=False)
            abouts.save()

            messages.success(request, "About content saved successfully")
            return redirect('about')
    context = {'abouts': abouts, 'form': form}
    return render(request, 'base/aboutform.html', context)

# edit about section
@login_required(login_url = 'login')
def editAbout(request, pk):
    about = About.objects.get(id=pk)
    form = AboutForm(instance=about)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()

            messages.success(request, "About content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/aboutform.html', context)


# delete about section
@login_required(login_url = 'login')
def deleteAbout(request,pk):
    about = About.objects.get(id=pk)
    if request.method == 'POST':
        about.delete()
        
        messages.success(request, 'About content deleted successfully')
        return redirect('about')
    context = {'obj': about}
    return render(request, 'delete.html', context)

# view vision
@login_required(login_url = 'login')
def viewVision(request):
    context = {}
    return render(request, 'base/viewvision.html', context)

# add vision section
@login_required(login_url = 'login')
def addVision(request):
    vision = Vision.objects.all()
    form = VisionForm()
    if request.method == 'POST':
        form = VisionForm(request.POST, request.FILES)
        if form.is_valid():
            vision = form.save(commit=False)
            vision.save()

            messages.success(request, "Vision content saved successfully")
            return redirect('about')
    context = {'vision': vision, 'form': form}
    return render(request, 'base/visionform.html', context)

# edit vision section
@login_required(login_url = 'login')
def editVision(request, pk):
    vision = Vision.objects.get(id=pk)
    form = VisionForm(instance=vision)
    if request.method == 'POST':
        form = VisionForm(request.POST, request.FILES, instance=vision)
        if form.is_valid():
            form.save()

            messages.success(request, "Vision content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/visionform.html', context)


# delete vision section
@login_required(login_url = 'login')
def deleteVision(request,pk):
    vision = Vision.objects.get(id=pk)
    if request.method == 'POST':
        vision.delete()
        
        messages.success(request, 'Vision content deleted successfully')
        return redirect('about')
    context = {'obj': vision}
    return render(request, 'delete.html', context)

# view mission
@login_required(login_url = 'login')
def viewMission(request):
    context = {}
    return render(request, 'base/viewmission.html', context)

# add mission section
@login_required(login_url = 'login')
def addMission(request):
    mission = Mission.objects.all()
    form = MissionForm()
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.save()

            messages.success(request, "Mission content saved successfully")
            return redirect('about')
    context = {'mission': mission, 'form': form}
    return render(request, 'base/missionform.html', context)

# edit mission section
@login_required(login_url = 'login')
def editMission(request, pk):
    mission = Mission.objects.get(id=pk)
    form = MissionForm(instance=mission)
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES, instance=mission)
        if form.is_valid():
            form.save()

            messages.success(request, "Mission content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/missionform.html', context)


# delete mission section
@login_required(login_url = 'login')
def deleteMission(request,pk):
    mission = Mission.objects.get(id=pk)
    if request.method == 'POST':
        mission.delete()
        
        messages.success(request, 'Mission content deleted successfully')
        return redirect('about')
    context = {'obj': mission}
    return render(request, 'delete.html', context)

# view message from
@login_required(login_url = 'login')
def viewMessageFrom(request):
    context = {}
    return render(request, 'base/viewmessagefrom.html', context)

# add message from section
@login_required(login_url = 'login')
def addMessageFrom(request):
    message = MessageFrom.objects.all()
    form = MessageFromForm()
    if request.method == 'POST':
        form = MessageFromForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()

            messages.success(request, "Message From content saved successfully")
            return redirect('about')
    context = {'message': message, 'form': form}
    return render(request, 'base/messagefromform.html', context)

# edit message from section
@login_required(login_url = 'login')
def editMessageFrom(request, pk):
    message = MessageFrom.objects.get(id=pk)
    form = MessageFromForm(instance=message)
    if request.method == 'POST':
        form = MessageFromForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()

            messages.success(request, "Message From content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/messagefromform.html', context)


# delete message from section
@login_required(login_url = 'login')
def deleteMessageFrom(request,pk):
    message = MessageFrom.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        
        messages.success(request, 'Message From content deleted successfully')
        return redirect('home')
    context = {'obj': message}
    return render(request, 'delete.html', context)

# view blogs
@login_required(login_url = 'login')
def viewBlogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'base/viewblogs.html', context)

# blogs page
def blogs(request):
    blogs = Blog.objects.all()

    page = request.GET.get('page')

    paginator = Paginator(blogs, 12)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {'blogs':blogs}
    return render (request, 'blogs.html', context)

# add blog
@login_required(login_url = 'login')
def addBlog(request):
    blog = Blog.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()

            messages.success(request, 'Blog added successfully')
            return redirect('viewblogs')
    context = {'blog': blog, 'form': form}
    return render(request, 'base/blogform.html', context)


# edit blog
@login_required(login_url = 'login')
def editBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()

            messages.success(request, 'Blog updated successfully')
            return redirect('blogs')
    context = {'form': form}
    return render(request, 'base/blogform.html', context)

# delete blog
@login_required(login_url = 'login')
def deleteBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == 'POST':
        blog.delete()

        messages.success(request, 'Blog deleted successfully')
        return redirect('blogs')
    context = {'obj': blog}
    return render(request, 'delete.html', context)

# blogs detail page
def blogDetail(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(blog=blog, name=request.POST['name'], body=body)
            comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm(initial={'blog_id': blog.id})
    context = {'blog': blog, 'comments':comments, 'comment_form':comment_form}
    return render (request, 'blog_detail.html', context)

# view gallery
@login_required(login_url = 'login')
def viewGallery(request):
    photos = Gallery.objects.all()
    context ={'photos': photos}
    return render(request, 'base/viewgallery.html', context)

# gallery page
def gallery(request):
    photos = Gallery.objects.all()

    # page = request.GET.get('page')

    # paginator = Paginator(photos, 3)

    # try:
    #     photos = paginator.page(page)
    # except PageNotAnInteger:
    #     photos = paginator.page(1)
    # except EmptyPage:
    #     photos = paginator.page(paginator.num_pages)

    context ={'photos': photos}
    return render (request, 'gallery.html', context)

# add photo
@login_required(login_url = 'login')
def addPhoto(request):
    photo = Gallery.objects.all()
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            messages.success(request, 'Photo added successfully')
            return redirect('viewgallery')
    context = {'photo': photo, 'form': form}
    return render(request, 'base/photoform.html', context)

# edit photo
@login_required(login_url = 'login')
def editPhoto(request, pk):
    photo = Gallery.objects.get(id=pk)
    form = GalleryForm(instance=photo)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()

            messages.success(request, 'Photo updated successfully')
            return redirect('viewgallery')
    context = {'form': form}
    return render(request, 'base/photoform.html', context)

# delete photo
@login_required(login_url = 'login')
def deletePhoto(request, pk):
    photo = Gallery.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()

        messages.success(request, 'Photo deleted successfully')
        return redirect('viewgallery')
    context = {'obj': photo}
    return render(request, 'delete.html', context)


# contact page
def contactForm(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacts = form.save(commit=False)
            contacts.save()

            messages.success(request, 'Query sent successfully')
            return redirect('contact')

    context ={'form': form, 'contacts': contacts}
    return render(request, 'contact.html', context)

# viewing contacted page
@login_required(login_url = 'login')
def viewContacts(request):
    contacts = Contact.objects.all().order_by('-created')
    context= {'contacts': contacts}
    return render(request, 'view_contacts.html', context)

# view carrers/vacancy page
@login_required(login_url = 'login')
def viewCarrers(request):
    vacancys = Vacancy.objects.all()
    context = {'vacancys': vacancys}
    return render(request, 'base/viewcarrers.html', context)

# carrers/vacancy page
def carrers(request):
    vacancys = Vacancy.objects.all()
    context = {'vacancys': vacancys}
    return render(request, 'carrers.html', context)

# add vacancy
@login_required(login_url = 'login')
def addVacancy(request):
    vacancy = Vacancy.objects.all()
    form = VacancyForm()
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.save()

            messages.success(request, 'Vacancy added successfully')
            return redirect('viewcarrers')
    context = {'vacancy': vacancy, 'form': form}
    return render(request, 'base/vacancyform.html', context)

# edit vacancy
@login_required(login_url = 'login')
def editVacancy(request, slug):
    vacancy = Vacancy.objects.get(slug=slug)
    form = VacancyForm(instance=vacancy)
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES, instance=vacancy)
        if form.is_valid():
            form.save()
 
            messages.success(request, 'Vacancy updated successfully')
            return redirect('carrers')
    context = {'form': form}
    return render(request, 'base/vacancyform.html', context)

# delete vacancy
@login_required(login_url = 'login')
def deleteVacancy(request, slug):
    vacancy = Vacancy.objects.get(slug=slug)
    if request.method == 'POST':
        vacancy.delete()

        messages.success(request, 'Vacancy deleted successfully')
        return redirect('carrers')
    context = {'obj': vacancy}
    return render (request, 'delete.html', context)

# carrers/vacancy detail page
def carrersDetail(request, slug):
    vacancy = Vacancy.objects.get(slug=slug)
    context = {'vacancy': vacancy}
    return render(request, 'carrers_detail.html', context)


# view notice page
@login_required(login_url = 'login')
def viewNotices(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'base/viewnotices.html', context)


# notice page
def notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'notice.html', context)

# add notice
@login_required(login_url = 'login')
def addNotice(request):
    notice = Notice.objects.all()
    form = NoticeForm()
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()

            messages.success(request, 'Notice added successfully')
            return redirect('viewnotices')
    context = {'notice': notice, 'form': form}
    return render(request, 'base/noticeform.html', context)

# edit notice
@login_required(login_url = 'login')
def editNotice(request, pk):
    notice = Notice.objects.get(id=pk)
    form = NoticeForm(instance=notice)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()

            messages.success(request, 'Notice updated successfully')
            return redirect('viewnotices')
    context = {'form': form}
    return render(request, 'base/noticeform.html', context)


# delete notice
@login_required(login_url = 'login')
def deleteNotice(request, pk):
    notice = Notice.objects.get(id=pk)
    if request.method == 'POST':
        notice.delete()
        
        messages.success(request, 'Notice deleted successfully')
        return redirect('home')
    context = {'obj': notice}
    return render(request, 'delete.html', context)

# view popup message
@login_required(login_url = 'login')
def viewPopupMessages(request):
    context = {}
    return render(request, 'base/viewpopupmessage.html', context)

# add popup message
@login_required(login_url = 'login')
def addPopupMessage(request):
    popup = PopupMessage.objects.all()
    form = PopupMessageForm()
    if request.method == 'POST':
        form = PopupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            popup = form.save(commit=False)
            popup.save()

            messages.success(request, 'Popup Message added successfully')
            return redirect('home') 

    context = {'popup': popup, 'form': form}
    return render (request, 'base/popupform.html', context)

# edit popup message
@login_required(login_url = 'login')
def editPopupMessage(request, pk):
    popup = PopupMessage.objects.get(id=pk)
    form = PopupMessageForm(instance=popup)
    if request.method == 'POST':
        form = PopupMessageForm(request.POST, request.FILES, instance=popup)
        if form.is_valid():
            form.save()

            messages.success(request, 'Popup Message updated successfully')
            return redirect('home') 

    context = {'form': form}
    return render (request, 'base/popupform.html', context)


# delete popup message
@login_required(login_url = 'login')
def deletePopupMessage(request, pk):
    popup = PopupMessage.objects.get(id=pk)
    if request.method == 'POST':
        popup.delete()

        messages.success(request, 'Popup Message deleted successfully')
        return redirect('home')
    context = {'obj': popup}
    return render (request, 'delete.html', context)

# view faqs
@login_required(login_url = 'login')
def viewFaqs(request):
    context = {}
    return render (request, 'base/viewfaqs.html', context)

# add faqs
@login_required(login_url = 'login')
def addFaq(request):
    faq = Faqs.objects.all()
    form = FaqsForm()
    if request.method =='POST':
        form = FaqsForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()

            messages.success(request, 'Faq added successfully')
            return redirect('home')
    context = {'faq': faq, 'form': form}
    return render (request, 'base/faqform.html', context)


# edit faq
@login_required(login_url = 'login')
def editFaq(request, pk):
    faq = Faqs.objects.get(id=pk)
    form = FaqsForm(instance=faq)
    if request.method == 'POST':
        form = FaqsForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()

            messages.success(request, 'Faq updated Successfully')
            return redirect('home')
    context = {'form': form}
    return render (request, 'base/faqform.html', context)

# delete faq
@login_required(login_url = 'login')
def deleteFaq(request, pk):
    faq = Faqs.objects.get(id=pk)
    if request.method == 'POST':
        faq.delete()

        messages.success(request, 'Faq was deleted successfully')
        return redirect('home')
    context= {'obj': faq}
    return render (request, 'delete.html', context)

# view course
@login_required(login_url = 'login')
def viewCourses(request):
    context = {}
    return render (request, 'base/viewcourses.html', context)

# add course
@login_required(login_url = 'login')
def addCourse(request):
    course = Courses.objects.all()
    form = CoursesForm()
    if request.method =='POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()

            messages.success(request, 'Faq added successfully')
            return redirect('home')
    context = {'course': course, 'form': form}
    return render (request, 'base/courseform.html', context)


# edit course
@login_required(login_url = 'login')
def editCourse(request, pk):
    course = Courses.objects.get(id=pk)
    form = CoursesForm(instance=course)
    if request.method =='POST':
        form = CoursesForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()

            messages.success(request, 'Faq updated successfully')
            return redirect('home')
    context = {'form': form}
    return render (request, 'base/courseform.html', context)


# delete course
@login_required(login_url = 'login')
def deleteCourse(request, pk):
    course = Courses.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()

        messages.success(request, 'Course was deleted successfully')
        return redirect('home')
    context= {'obj': course}
    return render (request, 'delete.html', context)

# view testimonial
@login_required(login_url = 'login')
def viewTestimonials(request):
    context = {}
    return render (request, 'base/viewtestimonial.html', context)

# add testimonial
@login_required(login_url = 'login')
def addTestimonial(request):
    testimonial = Testimonial.objects.all()
    form = TestimonialForm()
    if request.method =='POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()

            messages.success(request, 'Testemonial added successfully')
            return redirect('home')
    context = {'testimonial': testimonial, 'form': form}
    return render (request, 'base/testimonialform.html', context)


# edit testimonial
@login_required(login_url = 'login')
def editTestimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    form = TestimonialForm(instance=testimonial)
    if request.method =='POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()

            messages.success(request, 'Testemonial added successfully')
            return redirect('home')
    context = {'form': form}
    return render (request, 'base/testimonialform.html', context)



# delete testimonial
@login_required(login_url = 'login')
def deleteTestimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    if request.method == 'POST':
        testimonial.delete()

        messages.success(request, 'Testimonial was deleted successfully')
        return redirect('home')
    context= {'obj': testimonial}
    return render (request, 'delete.html', context)

# view team member
@login_required(login_url = 'login')
def viewTeamMembers(request):
    context = {}
    return render (request, 'base/viewteam.html', context)

# add team member
@login_required(login_url = 'login')
def addTeamMember(request):
    teams = TeamMember.objects.all()
    form = TeamMemberForm()
    if request.method =='POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            teams = form.save(commit=False)
            teams.save()

            messages.success(request, 'Team Member added successfully')
            return redirect('viewteammembers')
    context = {'teams': teams, 'form': form}
    return render (request, 'base/teammemberform.html', context)


# edit team member
@login_required(login_url = 'login')
def editTeamMember(request, pk):
    teams = TeamMember.objects.get(id=pk)
    form = TeamMemberForm(instance=teams)
    if request.method =='POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=teams)
        if form.is_valid():
            form.save()

            messages.success(request, 'Team Member updated successfully')
            return redirect('viewteammembers')
    context = {'form': form}
    return render (request, 'base/teammemberform.html', context)

# delete team member
@login_required(login_url = 'login')
def deleteTeamMember(request, pk):
    teams = TeamMember.objects.get(id=pk)
    if request.method == 'POST':
        teams.delete()

        messages.success(request, 'Team Member was deleted successfully')
        return redirect('about')
    context= {'obj': teams}
    return render (request, 'delete.html', context)


