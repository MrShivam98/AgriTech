from django.contrib import admin
from home.models import Contact, technology, driver, service

# Register your models here.
admin.site.register((Contact, technology, driver, service))
