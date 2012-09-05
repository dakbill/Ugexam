from django.shortcuts import render_to_response
from recrep.models import Account ,Voucher
from datetime import datetime,date
from datetime import timedelta
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
import shlex
import requests
from django.http import QueryDict
import dj_simple_sms
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
def sms_search(sms):
        msg= sms.body.strip()
	lis=shlex.split(msg)
	if(len(lis) != 2):
		pass
	else:
				
		try:					
			vouch=Voucher.objects.get(num=lis[1])			
			cust=Account.objects.get(accnum=lis[0])
			cust.balance=cust.balance+1
			vouch.Account=cust
			vouch.date_used=datetime.now()			
			vouch.save()
			cust.save()
			sendthis="http://bulk.mnotification.com/smsapi?key=1445a42ca3c9cde00912&to="
			sendthis=sendthis+(cust.phone)
			sendthis=sendthis+"&msg="
			sendthis=sendthis+"total account balance: "+str(cust.balance)+" "
			sendthis=sendthis+"&sender_id=scweb"			
			#return HttpResponseRedirect(sendthis)
		except:			
			pass			
	response = dj_simple_sms.models.SMS(to_number=sms.from_number, from_number='scrybaweb', body=sendthis)
        response.send()
@csrf_exempt
def home(request):
	if request.method=='POST':
		scode=str(request.POST.get(r"scratchcode"))		
		lis=shlex.split(scode)
		try:
			vouch=Voucher.objects.get(num=lis[1])
			if(not vouch.used):						
				cust=Account.objects.get(accnum=lis[0])
				cust.balance=cust.balance+vouch.amount
				vouch.Account=cust
				vouch.date_used=datetime.now()
				vouch.used=True			
				boolexp='False'					
				vouch.save()
				cust.save()
				t = loader.get_template('login/login.html')
				err_msg=""
		    		c = Context({'error':err_msg,'boolexp':boolexp})				
				return HttpResponse(t.render(c))
		    	else:
		    		err_msg="Voucher already used"
		    		boolexp='True'
		    		t = loader.get_template('login/login.html')
		    		c = Context({'error':err_msg,'boolexp':boolexp})
				return HttpResponse(t.render(c))
		except ObjectDoesNotExist:
			err_msg="Voucher or account does not exist"
	    		boolexp='True'
	    		t = loader.get_template('login/login.html')
	    		c = Context({'error':err_msg,'boolexp':boolexp})
			return HttpResponse(t.render(c))
			
	t = loader.get_template('login/login.html')
	err_msg=""
	boolexp='False'
	c = Context({'error':err_msg,'boolexp':boolexp})
	return HttpResponse(t.render(c))
@csrf_exempt
def send(request):
	msgque=[]
	a = datetime.today()
	numdays = 6
	dateList = []
	for x in range ( numdays,-1,-1):
    		dateList.append(a - timedelta(days = x))
	if request.method=='POST':
		try:			
			cust=Account.objects.all()
			for customer in cust:
				vouch=Voucher.objects.filter(Account=customer,date_used__range=[dateList[0],dateList[6]])				
				sendthis="http://bulk.mnotification.com/smsapi?key=2c3cebd22fb6165535ab&to="
				sendthis=sendthis+cust.phone
				sendthis=sendthis+"&msg=this+week:+"
				for voucher in vouch:
					sendthis=sendthis+str(voucher.date_used.strftime("%A")[:3])+"+"+str(voucher.amount)+"gh+"
				sendthis=sendthis+"total+account+balance:+"+str(customer.balance)
				sendthis=sendthis+"&sender_id=scrybaweb"				
				requests.post(sendthis)				
				msgque.append(sendthis)
			t = loader.get_template('login/send.html')
    			c = Context({'msgque':msgque})
			return HttpResponse(t.render(c))
    		except:
    			err_msg="Wrong scratch code"
    			boolexp='True'
    			t = loader.get_template('login/login.html')
    			c = Context({'error':err_msg,'boolexp':boolexp})
			return HttpResponse(t.render(c))
    	t = loader.get_template('login/send.html')
    	c = Context({})
	return HttpResponse(t.render(c))

