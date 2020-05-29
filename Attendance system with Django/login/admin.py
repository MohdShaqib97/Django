from django.contrib import admin

# Register your models here.
from .models import info

class infoAdmin(admin.ModelAdmin):
    list_display = ('Emp_name','Emp_attendance','Date','Time',)
   #list_filter = ('')
    search_fields = ('Emp_name',)

admin.site.register(info,infoAdmin)
