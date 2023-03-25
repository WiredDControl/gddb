import os
import requests
import sqlite3
import time
from internetarchive import upload, get_item
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from sqlite3 import Error

####################################################################
# Startup Parameter:
uploadfolder = 'D:\\_scans+stuff\\todo\\TFX\\archiv'

title = 'TFX (1993) German PC Soft Price Big Box CD'
my_item = 'tfx-1993-german-pc-soft-price-cd'

gddb_releaseid = '563'
#ogdb_releaseid = '121256'

description = 'TFX (1993) German PC Soft Price Big Box CD<br /><br />complete scans'
mediatype = 'image'
language = 'German'
subject = ['Big Box', 'Scan']
collection = 'opensource_image'
####################################################################
####################################################################

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def insert_image(conn, insert):
    sql = ''' INSERT INTO games_image(imgfilename,imgtype,imgdescr,imgcomment,created_date,published_date,rlstitle_id,source,imgquali)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, insert)
    conn.commit()
    return cur.lastrowid


# Upload ins Archive
#   archive cli nutzen
md = {'collection': collection, 
      'title': str(title), 
      'mediatype': str(mediatype), 
      'description': str(description), 
      'language': str(language), 
      'subject': subject}

#   upload
filelist = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(uploadfolder) for f in filenames]
r = upload(str(my_item), files=filelist, metadata=md, verbose=True)
r[0].status_code
print(r[0].status_code)
print("")
print("")


'''
# get infos from ogdb
ua = UserAgent()
header = {
    "User-Agent": ua.random
}

url = "https://ogdb.eu/index.php?section=game&gameid="+str(ogdb_releaseid)

req = requests.get(url, headers=header)
soup = BeautifulSoup(req.text, "html.parser")
'''


# Eintragung in die sql.lite db
created_date = time.strftime("%Y-%m-%d %H:%M:%S")
published_date = time.strftime("%Y-%m-%d %H:%M:%S")
conn = create_connection("D:\\python-projects\\db.sqlite3")

for file in filelist:
    file_name, file_extension = os.path.splitext(file)
    print("processing: "+file)

    if (str(file_extension) in ['.jpg','.png','.tif']): # jedes jpg, png und tif

        

        imgtype = ""
        imgdescr = ""

        if ("_image_box-back." in str(file)):
            imgtype = "bck"
            imgdescr = ""
        if ("_image_box-front." in str(file)):
            imgtype = "cvr"
            imgdescr = ""
        if ("_image_media." in str(file)):
            imgtype = "med"
            imgdescr = ""
        if ("_image_box-front-left." in str(file)):
            imgtype = "oth"
            imgdescr = "Front-Left"
        if ("_image_box-front-right." in str(file)):
            imgtype = "oth"
            imgdescr = "Front-Right"
        if ("_image_box-front-top." in str(file)):
            imgtype = "oth"
            imgdescr = "Front-Top"
        if ("_image_box-front-bottom." in str(file)):
            imgtype = "oth"
            imgdescr = "Front-Bottom"
        if ("_image_box-back-left." in str(file)):
            imgtype = "oth"
            imgdescr = "Back-Left"
        if ("_image_box-back-right." in str(file)):
            imgtype = "oth"
            imgdescr = "Back-Right"
        if ("_image_box-back-top." in str(file)):
            imgtype = "oth"
            imgdescr = "Back-Top"
        if ("_image_box-back-bottom." in str(file)):
            imgtype = "oth"
            imgdescr = "Back-Bottom"
        if ("_image_jewelcase-front." in str(file)):
            imgtype = "oth"
            imgdescr = "Jewelcase-Front"
        if ("_image_jewelcase-front-inlay." in str(file)):
            imgtype = "oth"
            imgdescr = "Jewelcase-Frontinlay"
        if ("_image_jewelcase-back." in str(file)):
            imgtype = "oth"
            imgdescr = "Jewelcase-Back"
        if ("_image_jewelcase-back-inlay." in str(file)):
            imgtype = "oth"
            imgdescr = "Jewelcase-Backinlay"

        if ("_image_disc" in str(file)):
            imgtype = "oth"
            imgdescr = str(file_name).rsplit("_",1)[1]

        if ("_image_overview." in str(file)):
            imgtype = "oth"
            imgdescr = "Overview"
        if ("_image_overview2." in str(file)):
            imgtype = "oth"
            imgdescr = "Overview-2"
        if ("_image_overview3." in str(file)):
            imgtype = "oth"
            imgdescr = "Overview-3"
        if ("_image_detail." in str(file)):
            imgtype = "oth"
            imgdescr = "Detail"
        if ("_image_detail2." in str(file)):
            imgtype = "oth"
            imgdescr = "Detail-2"
        if ("_image_detail3." in str(file)):
            imgtype = "oth"
            imgdescr = "Detail-3"

        if (imgtype == ""):
            print("... WARNING: unidentified image file found: "+str(file))
        else:
            print("... found "+imgtype+" ("+imgdescr+")")
            insert = (str(os.path.split(file)[1]), imgtype, imgdescr, "", created_date, published_date, gddb_releaseid, "Timber", "1")
            insert_image(conn, insert)

# automatischer Upload der sql.lite db möglich?




'''
#TEST
item = get_item('invest-1990-german-pc-retail-small-box-floppy-525')

for k,v in item.metadata.items():
    print(print(k,":",v))
'''