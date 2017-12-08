from django.shortcuts import render_to_response, render
from .models import CreateUser, AddCourses, CoursesTopic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.core.mail import EmailMessage
from django.views.generic.base import TemplateView



def coursesTopic_view(request):
        template = 'index.html'
        coursesTopic = CoursesTopic.objects.all()
        if request.user.is_authenticated():
            username = request.user.first_name
            context = {'coursesTopic': coursesTopic}
            return render(request, template, context)

def courses_view(request, course_name):
    if request.user.is_authenticated():

        template = 'courses.html'
        if course_name == u'Microsoft_Office_Suite':
            courses = AddCourses.objects.filter(course_category='MOS')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Graphic_Design':
            courses = AddCourses.objects.filter(course_category='GD')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Sound_Music':
            courses = AddCourses.objects.filter(course_category='SM')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Web_Site_Development':
            courses = AddCourses.objects.filter(course_category='WD')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Animation_Production':
            courses = AddCourses.objects.filter(course_category='AP')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Video_Editing':
            courses = AddCourses.objects.filter(course_category='VE')
            context = {'courses': courses}
            return render(request, template, context)

        else:
                    return HttpResponseRedirect("/")
    else:
            return HttpResponseRedirect("/logins")

def login_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = authenticate(username=username, password=password)
    template = 'login.html'
    if user is not None:
        # A backend authenticated the credentials
        auth.login(request, user)
        messages.success(request, "Logged in successfully")
        return HttpResponseRedirect("/")
    else:
        return render(request, template)

def logout_view(request):
    # A backend authenticated the credentials
    auth.logout(request)
    return HttpResponseRedirect("logins")

def video_view(request, course_name):
    template = 'video.html'
    return render(request, template)

def createAccount_view(request):
    template = 'createnewAccount.html'
    if request.method == 'POST':
        email = request.POST['email']

        try:
            User.objects.get(username=email)
        except User.DoesNotExist:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']

            user = User.objects.create_user(email, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return HttpResponseRedirect("logins")

    return render(request, template)

def forgotPassword_view(request):
    template = 'forgotPassword.html'
    if request.method == 'POST':
        email = request.POST['email']
        try:

            request.session['email'] = email
            subject, from_email, to = 'Password Reset', 'noreply@techoryze.com', email

            msg = EmailMessage(subject, "Hi,You can reset your password from the link. https://techoryze.herokuapp.com/resetPassword", from_email, [to])
            msg.send()
            return HttpResponseRedirect("logins")

        except User.DoesNotExist:
            return render(request, template)

    return render(request, template)

def resetPassword_view(request):
    template = 'resetPassword.html'
    if request.method == 'POST':
        password = request.POST["password"]
        email = request.session['email']
        try:

            user = User.objects.get(username=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect("logins")
        except:
            return render(request, template)

    return render(request, template)

def ChatterBotAppView(request):
    template = "chatterbot.html"
    if request.user.is_authenticated():
        username = request.user.first_name
        context = {'username': username}
        return render(request, template, context)



