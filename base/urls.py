from django.urls import path
from . import views
from .views import custom_404_view

urlpatterns = [
    # login routes
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    # home page routes
    path('', views.home, name='home'),
    path('view-home-content/', views.viewHomeContent, name='viewhomecontent'),
    path('add-home-content/', views.addHomeContent, name='addhomecontent'),
    path('edit-home-content/<str:pk>', views.editHomeContent, name='edithomecontent'),
    path('delete-home-content/<str:pk>', views.deleteHomeContent, name='deletehomecontent'),

    # school setup routes
    path('view-school-setup/', views.viewSchool, name='schoolsetup'),
    path('add-school-data/', views.addSchool, name='addschool'),
    path('edit-school-data/<str:pk>', views.editSchool, name='editschool'),
    path('delete-school-data/<str:pk>', views.deleteSchool, name='deleteschool'),

    # social routes
    path('view-socials/', views.viewSocials, name='viewsocials'),
    path('add-social/', views.addSocial, name='addsocial'),
    path('edit-social/<str:pk>', views.editSocial, name='editsocial'),
    path('delete-social/<str:pk>', views.deleteSocial, name='deletesocial'),

    # about page routes 
    path('about/', views.about, name='about'),

    # about page routes for about section
    path('view-about/', views.viewAbout, name='viewabout'),
    path('add-about/', views.addAbout, name='addabout'),
    path('edit-about/<str:pk>', views.editAbout, name='editabout'),
    path('delete-about/<str:pk>', views.deleteAbout, name='deleteabout'),

    # about page routes for Vision section
    path('view-vision/', views.viewVision, name='viewvision'),
    path('add-vision/', views.addVision, name='addvision'),
    path('edit-vision/<str:pk>', views.editVision, name='editvision'),
    path('delete-vision/<str:pk>', views.deleteVision, name='deletevision'),

    # about page routes for Mission section
    path('view-mission/', views.viewMission, name='viewmission'),
    path('add-mission/', views.addMission, name='addmission'),
    path('edit-mission/<str:pk>', views.editMission, name='editmission'),
    path('delete-mission/<str:pk>', views.deleteMission, name='deletemission'),

    # about page routes for Message From section
    path('view-message-from/', views.viewMessageFrom, name='viewmessagefrom'),
    path('add-message-from/', views.addMessageFrom, name='addmessagefrom'),
    path('edit-message-from/<str:pk>', views.editMessageFrom, name='editmessagefrom'),
    path('delete-message-form/<str:pk>', views.deleteMessageFrom, name='deletemessagefrom'),

    # blogs page routes 
    path('view-blogs/', views.viewBlogs, name='viewblogs'),
    path('blogs/', views.blogs, name='blogs'),
    path('add-blog/', views.addBlog, name='addblog'),
    path('edit-blog/<slug:slug>', views.editBlog, name='editblog'),
    path('delete-blog/<slug:slug>', views.deleteBlog, name='deleteblog'),
    path('blog/<slug:slug>', views.blogDetail, name='blog'),

    # gallery page routes 
    path('view-gallery/', views.viewGallery, name='viewgallery'),
    path('gallery/', views.gallery, name='gallery'),
    path('add-photo/', views.addPhoto, name='addphoto'),
    path('edit-photo/<str:pk>', views.editPhoto, name='editphoto'),
    path('delete-photo/<str:pk>', views.deletePhoto, name='deletephoto'),

    # contact page routes 
    path('contact/', views.contactForm, name='contact'),
    path('view-contacts/', views.viewContacts, name='viewcontacts'),

    # carrers page routes 
    path('view-carrers/', views.viewCarrers, name='viewcarrers'),
    path('carrers/', views.carrers, name='carrers'),
    path('add-vacancy/', views.addVacancy, name='addvacancy'),
    path('edit-vacancy/<slug:slug>', views.editVacancy, name='editvacancy'),
    path('delete-vacancy/<slug:slug>', views.deleteVacancy, name='deletevacancy'),
    path('carrer/<slug:slug>', views.carrersDetail, name='carrer'),

    # notice page routes 
    path('view-notices/', views.viewNotices, name='viewnotices'),
    path('notice/', views.notice, name='notice'),
    path('add-notice/', views.addNotice, name='addnotice'),
    path('edit-notice/<str:pk>', views.editNotice, name='editnotice'),
    path('delete-notice/<str:pk>', views.deleteNotice, name='deletenotice'),

    # popup routes
    path('view-popup-messages/', views.viewPopupMessages, name='viewpopups'),
    path('add-popup-message/', views.addPopupMessage, name='addpopup'),
    path('edit-popup-message/<str:pk>', views.editPopupMessage, name='editpopup'),
    path('delete-popup-message/<str:pk>', views.deletePopupMessage, name='deletepopup'),

    # faqs routes
    path('view-faqs/', views.viewFaqs, name='viewfaqs'),
    path('add-faq/', views.addFaq, name='addfaq'),
    path('edit-faq/<str:pk>', views.editFaq, name='editfaq'),
    path('delete-faq/<str:pk>', views.deleteFaq, name='deletefaq'),

    # courses routes
    path('view-courses/', views.viewCourses, name='viewcourses'),
    path('add-course/', views.addCourse, name='addcourse'),
    path('edit-course/<str:pk>', views.editCourse, name='editcourse'),
    path('delete-course/<str:pk>', views.deleteCourse, name='deletecourse'),

    # testimonials routes
    path('view-testimonials/', views.viewTestimonials, name='viewtestimonials'),
    path('add-testimonial/', views.addTestimonial, name='addtestimonial'),
    path('edit-testimonial/<str:pk>', views.editTestimonial, name='edittestimonial'),
    path('delete-testimonial/<str:pk>', views.deleteTestimonial, name='deletetestimonial'),
    
    # team members routes
    path('view-team-members/', views.viewTeamMembers, name='viewteammembers'),
    path('add-team-member/', views.addTeamMember, name='addteammember'),
    path('edit-team-member/<str:pk>', views.editTeamMember, name='editteammember'),
    path('delete-team-member/<str:pk>', views.deleteTeamMember, name='deleteteammember'),

    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

]

handler404 = custom_404_view