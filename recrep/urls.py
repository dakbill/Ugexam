from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^$', 'recrep.views.home'),
    url(r'send/$', 'recrep.views.send'),
        
   
)
