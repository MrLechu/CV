#from django.template import Context, loader
from django.shortcuts import render_to_response
from cv.mycv.models import vcard, education, experience, course, skill, language, interest
from django.http import HttpResponse

def index(request):
    vcards = vcard.objects.all()
    educations = education.objects.all()
    experiences = experience.objects.all()
    courses = course.objects.all()
    skills = skill.objects.all()
    languages = language.objects.all()
    interests = interest.objects.all()
    
    return render_to_response('mycv/index.html', 
    {
        'vcards': vcards, 
        'educations': educations, 
        'experiences': experiences,
        'courses': courses,
        'skills': skills,
        'languages': languages,
        'interests': interests
    })

