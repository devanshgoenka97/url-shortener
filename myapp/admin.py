from django.contrib import admin
from myapp.models import urls
# Register your models here.

class urladmin(admin.ModelAdmin):
	list_display=('short_id','httpurl','pub_date','count')
	ordering = 	('-pub_date',)

admin.site.register(urls,urladmin)