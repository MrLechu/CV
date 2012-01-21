# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, get_object_or_404
from cv.mycv.models import vcard, education, experience, course, skill, language, interest, MetaHtml
from django.http import HttpResponse

def index(request):
    vcards = vcard.objects.all()
    educations = education.objects.all()
    experiences = experience.objects.all()
    courses = course.objects.all()
    skills = skill.objects.all()
    languages = language.objects.all()
    interests = interest.objects.all()
    metas = MetaHtml.objects.all()
    
    vc = vcard.objects.get(pk=1)
  
    return render_to_response('mycv/index.html', locals())
#    {
     
#        'vcards': vcards, 
#        'educations': educations, 
#        'experiences': experiences,
#        'courses': courses,
#        'skills': skills,
#        'languages': languages,
#        'interests': interests
#    }
    #)
