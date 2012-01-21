from django.contrib import admin
from django.conf import settings
from cv.mycv.models import vcard, education, experience, course, skill, language, interest, MetaHtml

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('/admin/js/tiny_mce/tiny_mce.js', '/admin/js/textareas.js',)
        js = (settings.ADMIN_MEDIA_PREFIX + 'js/tiny_mce/tiny_mce.js', settings.ADMIN_MEDIA_PREFIX + 'js/textareas.js')
        

admin.site.register(vcard)
admin.site.register(education)
admin.site.register(experience, PostAdmin)
admin.site.register(course)
admin.site.register(skill)
admin.site.register(language)
admin.site.register(interest)
admin.site.register(MetaHtml)



