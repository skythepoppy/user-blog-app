from django.contrib import admin
from .models import Post

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}     # automatically fills in slug field with post title

admin.site.register(Post, AdminPost)


