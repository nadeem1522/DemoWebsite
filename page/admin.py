from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))

    thumnail.short_description=('photos')

    list_display=["id","thumnail","created_date"]
    search_fields=["id"]
    list_filter=["id"]

admin.site.register(Team, TeamAdmin)