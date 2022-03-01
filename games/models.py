from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
import os
from uuid import uuid4


class Genre(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class GLP(models.Model):
    glptitle = models.CharField(max_length=250)
    title = models.ForeignKey(Game, related_name="glps", on_delete=models.CASCADE)
    glpdescription = models.TextField()
    eXoID = models.IntegerField()
    LBID = models.CharField(max_length=250)
    priority = models.CharField(max_length=10)
    files = models.CharField(max_length=10)
    batchname = models.CharField(max_length=250)
    foldername = models.CharField(max_length=250)
    box = models.CharField(max_length=10)
    manual = models.CharField(max_length=10)
    media = models.CharField(max_length=10)
    iso = models.CharField(max_length=10)
    comments = models.TextField()
    version = models.CharField(max_length=250)
    ineXoDOS = models.CharField(max_length=250)
    variant = models.CharField(max_length=250)
    comment = models.TextField()
    dosbox = models.CharField(max_length=250)
    dosboxsound = models.CharField(max_length=250)
    scummvm = models.CharField(max_length=250)
    scummvmsound = models.CharField(max_length=250)
    network = models.CharField(max_length=10)
    tested = models.CharField(max_length=10)
    cracked = models.CharField(max_length=10)
    hasissues = models.CharField(max_length=10)
    exception = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.glptitle

class Release(models.Model):
    rlstitle = models.CharField("Release",max_length=250)
    title = models.ForeignKey(Game, on_delete=models.CASCADE)
    floppy35 = 'F3'
    floppy52 = 'F5'
    cdrom = 'CD'
    dvdrom = 'DD'
    download = 'DL'
    media_CHOICES = [
        (floppy35, 'Floppy 3,5"'),
        (floppy52, 'Floppy 5,25"'),
        (cdrom, 'CD-ROM'),
        (dvdrom, 'DVD-ROM'),
        (download, 'Download'),
    ]
    media = models.CharField(
        max_length=2,
        choices=media_CHOICES,
        default=floppy35,
    )

    year = models.CharField(max_length=10)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    speech = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    barcode = models.CharField(max_length=250)
    usk = models.CharField(max_length=100)
    content = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.rlstitle + " (" + self.get_media_display() + ")"

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
            ext = filename.split('.')[-1]
            oldfilename = filename.split('.')[0]
            filename = '{}_{}.{}'.format(oldfilename,str(uuid4()), ext)
            return os.path.join(self.path, filename)

ImagePathfilename = PathAndRename("images")
ImagePathfilenameRaw = PathAndRename("images_raw")

class Image(models.Model):
    #imgfilename = models.ImageField(upload_to='images')
    imgfilename = models.ImageField("Bilddatei",upload_to=ImagePathfilename)
    rlstitle = models.ForeignKey(Release, related_name="releasetitle", on_delete=models.CASCADE,verbose_name="Release")
    cover = 'cvr'
    back = 'bck'
    media = 'med'
    other = 'oth'
    imgtype_CHOICES = [
        (cover, 'Front-Cover'),
        (back, 'Back-Cover'),
        (media, 'Media'),
        (other, 'other...'),
    ]
    imgtype = models.CharField(
        "Bildtyp:",
        max_length=3,
        choices=imgtype_CHOICES,
        default=cover,
    )
    imgdescr = models.CharField("Beschreibung",max_length=250)
    imgcomment = models.TextField("Kommentar")
    imgrawfilename = models.ImageField("Roh-Bilddatei",upload_to=ImagePathfilenameRaw)
    imgrawlink = models.CharField("Link zu Rohscans",max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.get_imgtype_display()