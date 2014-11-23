from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

class PostAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'text', 'created']
    list_filter = ['blog__user']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
