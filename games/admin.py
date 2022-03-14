#from tkinter import Image
from django.contrib import admin
from .models import Developer, Game,Genre,GLP, Publisher, Release, Image, Disk, Extra, Platform

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(GLP)
admin.site.register(Platform)

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