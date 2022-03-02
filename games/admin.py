#from tkinter import Image
from django.contrib import admin
from .models import Developer, Game,Genre,GLP, Publisher, Release, Image

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(GLP)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('rlstitle', 'imgtype')
    pass
admin.site.register(Image, ImageAdmin)

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('rlstitle', 'media')
    pass
admin.site.register(Release, ReleaseAdmin)