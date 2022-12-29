from django.contrib import admin
from .models import student

class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll_no']
    ordering=[('id'),]

admin.site.register(student,studentAdmin)



# Register your models here.
