from django.contrib import admin
from .models import Contact,Category,Blog,Portfolio,PortfolioCategory,Team
from django.utils.html import format_html

# Register your models here.

admin.site.register((Contact,Category,PortfolioCategory,Portfolio)) 


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','img')
    readonly_fields = ['slug']
    def img(self, obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('rasm','job','full_name')
    readonly_fields = ['img']
    def rasm(self, obj):
        return format_html('<img width="50" height="50" src="{}" />'.format(obj.img.url))
