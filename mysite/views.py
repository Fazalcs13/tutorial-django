from django.shortcuts import render
from .models import User, CoursesModel1
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django import forms

def courses_view(request, course_name):
    if request.session.get('UserID') is not None:

        template = 'courses.html'
        if course_name == u'microsoft_office_suite':
            courses = CoursesModel1.objects.filter(course_category='MOS')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'graphic_design':
            courses = CoursesModel1.objects.filter(course_category='GD')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'sound_music':
            courses = CoursesModel1.objects.filter(course_category='SM')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'website_development':
            courses = CoursesModel1.objects.filter(course_category='WD')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'animation_production':
            courses = CoursesModel1.objects.filter(course_category='AP')
            context = {'courses': courses}
            return render(request, template, context)
        elif course_name == u'video_editing':
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
        request.session['UserID'] = user.id
        return HttpResponseRedirect("/")
    else:
        raise forms.ValidationError("You have forgotten about Fred!")
        return render(request, template)
