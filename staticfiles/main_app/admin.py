from django.contrib import admin
from .models import Heading,Title,Downbase
# Register your models here.


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    list_display=[
        'address'
    ]

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display=[
        'title'
    ]


@admin.register(Downbase)
class DownbaseAdmin(admin.ModelAdmin):
    list_display=[
        'social_handle'
    ]