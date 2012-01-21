# -*- coding: utf-8 -*-
from django.db import models
import codecs


class vcard(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    street = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    
class education(models.Model):
    dateStart = models.DateField()
    dateEnd = models.DateField()
    school = models.CharField(max_length=50)
    specialization = models.CharField(max_length=200)
    #description = models.TextField(max_length=255, null=True)
    
    class Meta:
        ordering = ('-dateEnd',)    
    
    def __unicode__(self):
        return self.school    
    
class experience(models.Model):
    dateStart = models.DateField()
    dateEnd = models.DateField()
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    recordListingId = models.IntegerField(editable=False, null=True)
    
    class Meta:
        ordering = ('-dateEnd',)
    
    
    def __unicode__(self):
        return self.company    

class course(models.Model):
    title = models.CharField(max_length=255)    
    description = models.TextField(max_length=255)
    def __unicode__(self):
        return self.title    
    
class skill(models.Model):
    description = models.TextField(max_length=255)
    def __unicode__(self):
        return self.description    
    
class language(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name    
    
class interest(models.Model):
    description = models.TextField(max_length=255)
    def __unicode__(self):
        return self.description  
    
class MetaHtml(models.Model):
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    def __unicode__(self):
        return "Meta tagi"     
    
      
    
    
    