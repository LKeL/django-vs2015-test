from django.contrib import admin

from mysite.models import Author,Tag,Classification,Article
# Register your models here.
#from django_summernote.admin import SummernoteModelAdmin
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Classification)
'''
class ArticleAdmin(admin.ModelAdmin):
      pass
admin.site.register(Article,ArticleAdmin)
'''

class ArticleAdmin(admin.ModelAdmin):
      class Media:
         js = (
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',      
         )
admin.site.register(Article,ArticleAdmin)
     
