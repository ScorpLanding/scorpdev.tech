from django.contrib import admin
from .models import *

class ParserPhotoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lab._meta.fields]

    class Meta():
        model = Lab

admin.site.register(Lab)
