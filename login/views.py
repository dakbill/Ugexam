from models import ScratchCode
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def home(request):
    	if request.method=='POST':
    		scode=request.POST.get("scratchcode")
    		try:
    			codeobject=ScratchCode.objects.get(code=scode)
    			boolexp='False'
    			codeobject.count=codeobject.count+1
    			codeobject.save()
    			#request.session['code']=scode
    			t = loader.get_template('examui/examui.html')
    			c = Context({})
			return HttpResponse(t.render(c))
    		except:
    			err_msg="Wrong scratch code"
    			boolexp='True'
    			t = loader.get_template('login/login.html')
    			c = Context({'error':err_msg,'boolexp':boolexp})
			print err_msg
			return HttpResponse(t.render(c))
    	t = loader.get_template('login/login.html')
    	c = Context({})
	return HttpResponse(t.render(c))
@csrf_exempt
def eng(request):
	t = loader.get_template('examui/eng.html')
    	c = Context({})
	return HttpResponse(t.render(c))

