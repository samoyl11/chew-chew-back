from django.contrib import admin

from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'telephone', 'completed')

# Register your models here.
admin.site.register(Form, FormAdmin) # add this
