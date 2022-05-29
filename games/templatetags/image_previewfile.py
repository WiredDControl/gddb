from django import template

register = template.Library()

@register.filter
def preview(value):
    previewfilename = (value.rsplit(".",1)[0]) + "_thumb.jpg"
    return previewfilename