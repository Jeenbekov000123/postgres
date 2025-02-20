from django.contrib import admin

# Register your models here.
from .models import Blog, Area,Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Area)
admin.site.register(Comment)