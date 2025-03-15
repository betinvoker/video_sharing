from django.contrib import admin
from .models import VideoPost, Comment, UserData

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "comment", "date_create")

class VideoPostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "desc", "category")

admin.site.register(UserData)
admin.site.register(Comment, CommentAdmin)
admin.site.register(VideoPost, VideoPostAdmin)