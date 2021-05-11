from django.contrib import admin

# Register your models here.
from .models import todos
admin.site.register(todos)
