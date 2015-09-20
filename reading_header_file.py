from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

im = Image.open('IMG_20150907_151311852.jpg')

GPSInfo_key = 34853

l = None


def get_field(exif, field):
    for (k, v) in exif.iteritems():
        field_name = TAGS.get(k)
        if field == field_name:
            print(field_name)
            return v

def print_all_fields(exif):
    for k, v in exif.iteritems():
        field_name = TAGS.get(k)
        print(field_name, v)

def print_gps_info(exif):
    gpsinfo = {}
    for key in exif[GPSInfo_key].keys():
        decode = GPSTAGS.get(key, key)
        gpsinfo[decode] = exif[GPSInfo_key][key]
    print gpsinfo


exif = im._getexif()
# print get_field(exif, 'ExposureTime')
#print get_field(exif, 'GPSInfo')  # print get_field(exif, 'DateTimeOriginal')
#print get_field(exif, 'DateTimeDigitized')
print_all_fields(exif)

#print_gps_info(exif)
