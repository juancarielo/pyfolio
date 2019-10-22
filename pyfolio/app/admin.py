from django.contrib import admin
from .models import Status, Job, Client

admin.site.register([Status, Job, Client])
