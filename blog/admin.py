from django.contrib import admin
from .models import Post,Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'author', 'date',  
                       'description')
admin.site.register(Post, PostAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','prof_image','bio')
admin.site.register(Profile, ProfileAdmin)