from django import template

register = template.Library()

@register.filter
def preview(value):
    previewfilename = (value.rsplit(".")[0]) + "_thumb.jpg"
    return previewfilename