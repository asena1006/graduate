from django.contrib import admin

from selling.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass