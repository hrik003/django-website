"""onepager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from onepager import views
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    # path("my-accounts/", include("django.contrib.auth.urls")),  # new
    path("my-accounts", TemplateView.as_view(template_name="myaccount.html"), name="myaccount"),
    path('', views.homePage, name='home'),
    path('test/', views.testPage, name='test'),
    path('about-us/', views.aboutUs, name='about'),
    path('contact-us/', views.contactUs, name='contact'),
    path('saveenquiry/', views.saveEnquiry, name='saveenquiry'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('course/', views.courses, name='courses'),
    path('userform/', views.userForm, name='userform'),
    path('submitform/', views.submitForm, name='submitform'),
    path('mycalculator/', views.mycalculator, name='mycalculator'),
    path('evenodd/', views.evenodd, name='evenodd'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('newsdetails/<slug>', views.newsDetails, name='newsdetails'),
    path('course-ints/<int:courseid>', views.courseInteger, name='Courses Details with int'),
    path('course-strs/<str:courseid>', views.courseString, name='Courses Details with String'),
    path('course-slgs/<slug:courseid>', views.courseSlug, name='Courses Details with Slug'),
    path('course-any/<courseid>', views.courseAny, name='Courses Details with anything'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)