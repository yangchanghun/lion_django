from django.contrib import admin
from .models import Bookmark

# Ensure there is only one registration for Bookmark
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

# Register the Bookmark model with its admin configuration
admin.site.register(Bookmark, BookmarkAdmin)