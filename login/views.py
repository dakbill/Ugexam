from models import ScratchCode
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def home(request):
    	if request.method=='POST':
    		scode=request.POST.get("scratchcode")
    		try:
    			code=ScratchCode.objects.get(code=scode)
    			request.session['code']=scode
    			print request.session['code']
    		except:
    			err_msg="Wrong scratch code"
    			t = loader.get_template('login/login.html')
    			c = Context({'error':err_msg})
			return HttpResponse(t.render(c))
    			print err_msg
    			
    	t = loader.get_template('login/login.html')
	return render_to_response('login/login.html')
