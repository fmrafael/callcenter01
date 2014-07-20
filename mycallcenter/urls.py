from django.conf.urls import patterns, include, url
from sms.views import home
from django.contrib import admin

from django.http import HttpResponseRedirect
from sms.forms import ClienteForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sms/$', 'sms.views.sms'),
    url(r'^thanks/$', 'sms.views.thanks')
)
