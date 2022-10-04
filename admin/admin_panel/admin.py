from django.contrib import admin
from .models import *


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(User)
admin.site.register(Text, TextAdmin)

# Register your models here.
