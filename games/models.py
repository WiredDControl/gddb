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
    mobygameslink = models.CharField(max_length=300,blank=True,default="")
    ogdblink = models.CharField(max_length=300,blank=True,default="")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Platform(models.Model):
    platformname = models.CharField("Name",max_length=250,default="")
    platformshort = models.CharField("Abkürzung",max_length=250,default="")
    platformdescr = models.TextField("Beschreibung",blank=True)
    platformimgfilename = models.CharField("Logo",max_length=250,blank=True,default="")

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.platformname

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
    coverfilename = models.CharField("Cover-Dateiname",max_length=250,blank=True,default="")
    title = models.ForeignKey(Game, on_delete=models.CASCADE)
    #platformlnk = models.ForeignKey(Platform, on_delete=models.CASCADE, default="1")
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

    year = models.CharField("Veröffentlichungsjahr",max_length=10)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    speech = models.CharField("Sprachausgabe",max_length=250)
    text = models.CharField("Textsprachen",max_length=250)

    barcode = models.CharField("Barcode",max_length=250)
    usk = models.CharField("USK-Freigabe",max_length=100)
    ogdblink = models.CharField("Link zu OGDB",max_length=300,blank=True,default="")
    archivelink = models.CharField("Eintrags auf archive.org",max_length=300,blank=True,default="")
    rawfile = models.CharField("Raw-Files Dateiname",max_length=250,blank=True,default="")
    content = models.TextField()

    good = '1'
    ok = '2'
    bad = '3'    
    quali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    quali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=quali_CHOICES,
        default=good,
    )
    comment = models.TextField("Kommentar",blank=True)

    timberown = models.BooleanField("Im Besitz",default=False)
    timberquali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    timberquali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=timberquali_CHOICES,
        default=good,
    )
    timbercomment = models.TextField("Kommentar",blank=True)     

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
    imgfilename = models.CharField("Bilddatei",max_length=250)
    #imgfilename = 'https://timberserver.de/gddb/media/images/'+imgfilename
    #deprecated:    
    #   imgfilename = models.ImageField("Bilddatei",upload_to=ImagePathfilename)
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
    imgdescr = models.CharField("Beschreibung",max_length=250,blank=True)
    good = '1'
    ok = '2'
    bad = '3'    
    imgquali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    imgquali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=imgquali_CHOICES,
        default=good,
    )    
    imgcomment = models.TextField("Kommentar",blank=True)
    source = models.CharField("Von wem ist das Bild",max_length=300,default="Timber")  
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.get_imgtype_display()

class Disk(models.Model):
    diskfilename = models.CharField("Image-Datei der Medien",max_length=250,blank=True,default="")
    #imgfilename = 'https://timberserver.de/gddb/media/disks/'+diskfilename
    rlstitle = models.ForeignKey(Release, related_name="releasetitle2", on_delete=models.CASCADE,verbose_name="Release")
    floppy35 = 'F35'
    floppy35k = 'F35K'
    floppy52 = 'F52'
    floppy52k = 'F52K'
    cdrom = 'CDR'
    dvdrom = 'DVD'
    download = 'DDL'
    disktype_CHOICES = [
        (floppy35, 'Floppy 3,5"'),
        (floppy35k, 'Floppy 3,5" (Kryoflux)'),
        (floppy52, 'Floppy 5,25"'),
        (floppy52k, 'Floppy 5,25" (Kryoflux'),
        (cdrom, 'CD-ROM'),
        (dvdrom, 'DVD-ROM'),
        (download, 'Download'),
    ]
    disktype = models.CharField(
        "Medientyp:",
        max_length=4,
        choices=disktype_CHOICES,
        default=floppy35,
    )
    diskcount = models.IntegerField()
    diskdescr = models.CharField("Beschreibung",max_length=250,blank=True)
    good = '1'
    ok = '2'
    bad = '3'    
    quali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    quali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=quali_CHOICES,
        default=good,
    )
    diskcomment = models.TextField("Kommentar",blank=True)
    source = models.CharField("Von wem ist der Rip",max_length=300,blank=True,default="Timber")
    timberown = models.BooleanField("Im Besitz",default=False)
    timberquali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    timberquali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=timberquali_CHOICES,
        default=good,
    )
    timbercomment = models.TextField("Kommentar",blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.get_disktype_display()

class Extra(models.Model):
    extrafilename = models.CharField("Dateiname",max_length=250,blank=True,default="")
    #imgfilename = 'https://timberserver.de/gddb/media/extras/'+extrafilename
    rlstitle = models.ForeignKey(Release, related_name="releasetitle3", on_delete=models.CASCADE,verbose_name="Release")
    manual = 'MAN'
    refcard = 'REF'
    map = 'MAP'
    regcard = 'REG'
    hintbook = 'HBK'
    other = 'OTH'
    extratype_CHOICES = [
        (manual, 'Handbuch'),
        (refcard, 'Referenzkarte'),
        (map, 'Karte/Poster'),
        (regcard, 'Registrationskarte'),
        (hintbook, 'Lösungsbuch'),
        (other, 'other...'),
    ]
    extratype = models.CharField(
        "Extra-Typ:",
        max_length=3,
        choices=extratype_CHOICES,
        default=manual,
    )
    extratypedescr = models.CharField("Typ Beschreibung",max_length=250,blank=True)
    extralanguage = models.CharField("Sprache(n)",max_length=250,default="de")
    extrapages = models.IntegerField("Anzahl Seiten")
    extradescr = models.CharField("Beschreibung",max_length=250,blank=True)
    good = '1'
    ok = '2'
    bad = '3'    
    extraquali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    extraquali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=extraquali_CHOICES,
        default=good,
    )    
    extracomment = models.TextField("Kommentar",blank=True)
    extrasource = models.CharField("Von wem ist der Scan",max_length=300,blank=True,default="Timber")
    timberown = models.BooleanField("Im Besitz",default=False)
    timberquali_CHOICES = [
        (good, '1 - Gut'),
        (ok, '2 - Ausreichend'),
        (bad, '3 - Schlecht'),
    ]
    timberquali = models.CharField(
        "Qualität:",
        max_length=1,
        choices=timberquali_CHOICES,
        default=good,
    )
    timbercomment = models.TextField("Kommentar",blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.get_extratype_display()
