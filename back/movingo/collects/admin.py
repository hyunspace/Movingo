from django.contrib import admin
from .models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user',)

admin.site.register(Collection, CollectionAdmin)