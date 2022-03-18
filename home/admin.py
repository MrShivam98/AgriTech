from django.contrib import admin
from home.models import Contact, driver, service

# Register your models here.
admin.site.register((Contact, driver, service))
