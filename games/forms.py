from django import forms
from .models import GLP,Image

class GLPForm(forms.ModelForm):

    class Meta:
         model = GLP
         fields = ('glptitle', 'title', 'glpdescription', 'eXoID', 'LBID', 'priority', 'files', 'batchname', 'foldername', 'box', 'manual', 'media', 'iso', 'comments', 'version', 'ineXoDOS', 'variant', 'comment', 'dosbox', 'dosboxsound', 'scummvm', 'scummvmsound', 'network', 'tested', 'cracked', 'hasissues', 'exception')

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('imgfilename', 'rlstitle', 'imgtype', 'imgdescr', 'imgcomment')