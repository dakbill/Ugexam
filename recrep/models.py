from django.db import models
from django.contrib import admin
class Account(models.Model):
	name=models.CharField(max_length=60)
	phone= models.CharField(max_length=60)
	accnum= models.CharField(max_length=60)	
	balance= models.IntegerField()	
	def __unicode__(self):
        	return self.name
class Voucher(models.Model):
	num=models.CharField(max_length=60)
	used=models.BooleanField(default=False)
	date_used= models.DateField(default="1992-02-21",editable=True)
	amount=models.IntegerField()	
	Account = models.ForeignKey(Account,related_name='Account',null=True,blank=True,default=None)	
	def __unicode__(self):
        	return self.num
class AccountAdmin(admin.ModelAdmin):
    	list_display=('name','phone')
    	search=('name',)
    	list_filter=('name','balance')

class VoucherAdmin(admin.ModelAdmin):
    	list_display=('num','amount')
    	list_filter=('num','amount')
admin.site.register(Account,AccountAdmin)
admin.site.register(Voucher,VoucherAdmin)
