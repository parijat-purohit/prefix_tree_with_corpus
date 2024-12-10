from django.contrib import admin
from .models import Prefix


@admin.register(Prefix)
class PrefixAdmin(admin.ModelAdmin):
    list_display = ('id', 'word')
    search_fields = ('word',)
