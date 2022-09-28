from django.contrib import admin
from .models import Task

admin.site.site_header = 'TODO LIST PROJECT'
admin.site.site_title = 'Todo list'
admin.site.index_title = 'TODO APP'

# Register your models here.

admin.site.register(Task)
