
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'nick_name',
        'email',
        'student_num',
        'date_joined',
        )
    search_fields = ('user_id', 'nick_name', 'student_id')

admin.site.register(User, UserAdmin)
