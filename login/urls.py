from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^$', 'login.views.home'),
    url(r'eng/$', 'login.views.eng'),
   
)
