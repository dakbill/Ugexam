from django.db import models
from django.contrib import admin
class ScratchCode(models.Model):
	code=models.CharField(max_length=50)
	date_used = models.DateField(null=True,blank=True)
   	date_disable = models.DateField(null=True,blank=True)
	def __unicode__(self):
		return self.code
admin.site.register(ScratchCode)
