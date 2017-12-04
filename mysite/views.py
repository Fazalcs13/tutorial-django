from django.shortcuts import render_to_response, render
from .models import User, CoursesModel1, CoursesTopic
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms

def coursesTopic_view(request):
        template = 'index.html'
        coursesTopic = CoursesTopic.objects.all()
        context = {'coursesTopic': coursesTopic}
        return render(request, template, context)


def courses_view(request, course_name):
    if request.user.is_authenticated():

        template = 'courses.html'
        if course_name == u'Microsoft_Office_Suite':
            courses = CoursesModel1.objects.filter(course_category='MOS')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Graphic_Design':
            courses = CoursesModel1.objects.filter(course_category='GD')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Sound_Music':
            courses = CoursesModel1.objects.filter(course_category='SM')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Web_Site_Development':
            courses = CoursesModel1.objects.filter(course_category='WD')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Animation_Production':
            courses = CoursesModel1.objects.filter(course_category='AP')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'Video_Editing':
            courses = CoursesModel1.objects.filter(course_category='VE')
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
        return HttpResponseRedirect("/")
    else:
        return render(request, template)

def logout_view(request):
    # A backend authenticated the credentials
    auth.logout(request)
    return HttpResponseRedirect("logins")
