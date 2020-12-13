from django.contrib import admin
from blog.models import Post, Contact
# Register your models here.

# class PostAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'title', 'blog_status']
# 	list_filter = ['blog_status', 'published_date']
# 	search_fields = ['title', 'body']



admin.site.register(Post)
# admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
