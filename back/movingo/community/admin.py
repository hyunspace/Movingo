from django.contrib import admin
from .models import Thread, Comment


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('movie',)

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment)