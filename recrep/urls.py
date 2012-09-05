from django.conf.urls.defaults import *
from piston.resource import Resource
from recrep.handlers import CalcHandler
class CsrfExemptResource(Resource):
	def _init_(self,handler,authentication=None):
		super(CsrfExemptResource,self)._init_(handler,authentication)
		self.csrf_exempt=getattr(self.handler,'csrf_exempt',True)
ext_in=CsrfExemptResource(CalcHandler)
urlpatterns = patterns('',
    url(r'^$', 'recrep.views.home'),
    url(r'send/$', 'recrep.views.send'),
    url(r'whatsapp/$', 'recrep.views.whatsapp'),
    url(r'receive/(?P<entry1>\d+)/(?P<entry2>\d+)/', ext_in),
        
   
)
