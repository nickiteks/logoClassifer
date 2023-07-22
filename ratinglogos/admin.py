from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('file', 'logo_image', 'rating')
    readonly_fields = ('date', 'logo_image')
admin.site.register(Data, DataAdmin)