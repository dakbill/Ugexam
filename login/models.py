from django.db import models
from django.contrib import admin
class ScratchCode(models.Model):
	code=models.CharField(max_length=50)
	count=models.IntegerField(blank=True,null=True)
	def __unicode__(self):
		return self.code
admin.site.register(ScratchCode)
