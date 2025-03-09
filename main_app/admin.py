from django.contrib import admin
from .models import Heading,Title,Downbase,Logistic,Vegie
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

@admin.register(Vegie)
class VegieAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]

@admin.register(Logistic)
class LogisticAdmin(admin.ModelAdmin):
    list_display=[
        'mode'
    ]