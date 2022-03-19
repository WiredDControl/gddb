#from tkinter import Image
from django.contrib import admin
from .models import Developer, Game,Genre,GLP, Publisher, Release, Image, Disk, Extra, Platform

class GameAdmin(admin.ModelAdmin):
    ordering = ['title']
admin.site.register(Game, GameAdmin)

class GenreAdmin(admin.ModelAdmin):
    ordering = ['name']
admin.site.register(Genre, GenreAdmin)

class DeveloperAdmin(admin.ModelAdmin):
    ordering = ['name']
admin.site.register(Developer, DeveloperAdmin)

class PublisherAdmin(admin.ModelAdmin):
    ordering = ['name']
admin.site.register(Publisher, PublisherAdmin)

admin.site.register(GLP)

class PlatformAdmin(admin.ModelAdmin):
    ordering = ['platformname']
admin.site.register(Platform, PlatformAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('rlstitle', 'imgtype')
    pass
admin.site.register(Image, ImageAdmin)

class DiskAdmin(admin.ModelAdmin):
    list_display = ('rlstitle', 'disktype')
    pass
admin.site.register(Disk, DiskAdmin)

class ExtraAdmin(admin.ModelAdmin):
    list_display = ('rlstitle', 'extratype')
    pass
admin.site.register(Extra, ExtraAdmin)

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('rlstitle', 'media')
    pass
admin.site.register(Release, ReleaseAdmin)