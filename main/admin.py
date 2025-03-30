from django.contrib import admin
from .models import Faculty, VideoPost, Comment, UserData
from django.utils.html import mark_safe

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "comment", "date_create")

@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "desc", "category")

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "display_logo", "date_create")
    readonly_fields = ("display_logo",)

    def display_logo(self, obj):
        if obj:
            return mark_safe("<img src={} with='49' height='57'/>".format(obj.logo.url))
        return "Нет логотипа"

    display_logo.short_description = "Герб факультета"

admin.site.register(UserData)