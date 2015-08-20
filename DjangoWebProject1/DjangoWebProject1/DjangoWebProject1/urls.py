"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # mysite:
    url(r'^home', 'mysite.views.home', name='home'),
    url(r'^$', 'mysite.views.index', name='index'),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', 'mysite.views.detail', name="detail"),#每篇文章
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^mysite/', include('mysite.urls', namespace="mysite")),
    url(r'^articleClassfi/(?P<classfi>\w+)/$', 'mysite.views.classfiDetail', name="classfiDetail"),#每个分类页下面的文章
    url(r'^articleTag/(?P<tag>\w+)/$', 'mysite.views.tagDetail', name="tagDetail"),#每个标签页下面的文章
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', 'mysite.views.detail', name="detail"),#每篇文章
    #url(r'^tinymce/', include('tinymce.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
)
