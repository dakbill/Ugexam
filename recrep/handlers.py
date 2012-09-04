from piston.handler import BaseHandler
from recrep.models import Account ,Voucher
import datetime
class CalcHandler(BaseHandler):
	def enter(self,entry1,entry2):
		allowed_methods = ('GET',)
    		model = Note		
		try:
			vouch=Voucher.objects.get(num=str(entry1))
			if(not vouch.used):						
				cust=Account.objects.get(accnum=str(entry2))
				cust.balance=cust.balance+vouch.amount
				vouch.Account=cust
				vouch.date_used=datetime.now()
				vouch.used=True			
				boolexp='False'					
				vouch.save()
				cust.save()
				#return "success"
		    	else:
				pass		    		
				#return "fail"
		except ObjectDoesNotExist:
			#return fail
			pass
