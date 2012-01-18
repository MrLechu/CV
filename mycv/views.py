# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, get_object_or_404
from cv.mycv.models import vcard, education, experience, course, skill, language, interest
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def index(request):
    vcards = vcard.objects.all()
    educations = education.objects.all()
    experiences = experience.objects.all()
    courses = course.objects.all()
    skills = skill.objects.all()
    languages = language.objects.all()
    interests = interest.objects.all()
  
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
    
def save_as_pdf(request):
    
    # Utwórz obiekt HttpResponse z odpowiednimi nagłówkami
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=cybulski_leszek_cv.pdf'
    
    # Utwórz obiekt PDF, używając obiektu response jako jego "file."
    p = canvas.Canvas(response)
    
    #W tej sekcji dzieje się magia generowania PDF-a
    p.drawString(100, 100, "Hello world.")
    
    #Zamknij obiekt PDF i to będzie wszystko
    p.showPage()
    p.save()
    return render_to_response('mycv/index.html', locals())
    
    
    