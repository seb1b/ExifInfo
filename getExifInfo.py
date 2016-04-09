from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from fractions import Fraction
 
def get_exif_info(path):

    #retrieve all files at destiantion path with the following extensions
    allowed_ext = ['jpg', 'JPG']
    images = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in allowed_ext) and not fn.startswith('.')]

    print images
    sum_fl = 0
    sum_ap = 0
    sum_et = 0
    for n in images:
    	if path != ".":
    		pic = Image.open(path+"/"+n)
    	else:
    		pic = Image.open(n)

    	exif = pic._getexif()
    	for tag, value in exif.items():
        	entry = TAGS.get(tag, tag)

        	if entry == 'FocalLength':
        		#print "length", value[0], ":", value[1]
        		sum_fl = sum_fl + value[0] *1.0/ value[1]

        	if entry == 'FNumber':
        		#print "f", value[0], ":", value[1]
        		sum_ap = sum_ap + value[0] *1.0/ value[1]
        	if entry == 'ExposureTime':
        		#print "ExposureTime", value[0], ":", value[1]
        		sum_et = sum_et + value[0] *1.0/ value[1]

    num_images = len(images)
    avr_focalL = sum_fl/num_images
    avr_ap = sum_ap/num_images 
    avr_et = sum_et/num_images 
    print "Average calculated for", num_images, "pictures"
    print "----------------------------------"
    print "Average FocalLength:", avr_focalL , "mm"
    print "Average Aperture:" , avr_ap
   # print "Average ExposureTime:" , Fraction(avr_et).limit_denominator() , "s"
    


if __name__ == "__main__":
	get_exif_info(sys.argv[1])

