# Register your models here.

from django.contrib import admin
from . models import Post, Comment

admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'email', 'created_date')

admin.site.unregister(Post)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)

