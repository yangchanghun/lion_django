# blog/admin.py

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'modify_dt')  # 'author'가 아닌 'get_author'로 수정


admin.site.register(Post, PostAdmin)
