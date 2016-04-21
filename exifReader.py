from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np


def draw_histogram(dat,filename):
    plt.clf()
    plt.hist(dat, 100,color='#c46835')
    plt.ylabel('amount')
    plt.xlabel('focal length')
    plt.xticks([0,20, 40, 60, 80, 100,120,140,160,180,200])
    plt.savefig(filename)



def get_exif_info(path,filename):
    # retrieve all files at destiantion path with the following extensions

    allowed_ext = ['jpg', 'JPG']
    if os.path.exists(path):
        images = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in allowed_ext) and not fn.startswith('.')]
    else:
        return -1

    sum_fl = 0
    sum_ap = 0
    sum_et = 0
    num_images = len(images)

    fls = []
    index = 0
     #"Directory contains no images!!"
    if num_images == 0:
        return 0
    for n in images:
        index = index + 1
        if path != ".":
            pic = Image.open(path + "/" + n)
        else:
            pic = Image.open(n)

        exif = pic._getexif()
        #print n
        for tag, value in exif.items():
            entry = TAGS.get(tag, tag)
            #print entry

            if entry == 'FocalLength':
               # print "length", value[0], ":", value[1]
                sum_fl = sum_fl + value[0] *1.0/ value[1]
                fls.append(value[0] *1.0/ value[1])

            if entry == 'FNumber':
                # print "f", value[0], ":", value[1]
                sum_ap = sum_ap + value[0] * 1.0 / value[1]
            if entry == 'ExposureTime':
                # print "ExposureTime", value[0], ":", value[1]
                sum_et = sum_et + value[0] * 1.0 / value[1]

    avr_focalL = sum_fl / num_images
    avr_ap = sum_ap / num_images
    avr_et = sum_et / num_images
   # print "Average calculated for", num_images, "pictures"
   # print "----------------------------------"
   # print "Average FocalLength:", avr_focalL, "mm"
   # print "Average Aperture:", avr_ap
   # print fls
    draw_histogram(fls,filename)
    return num_images
    # print "Average ExposureTime:" , Fraction(avr_et).limit_denominator() , "s"


if __name__ == "__main__":
    path = ""
    filename = ""
    if len(sys.argv)<2:
        print "Please give path to directory"
    else:
        path = sys.argv[1]

    if len(sys.argv)<3:
        filename = "output.png"
    else:
        filename = sys.argv[2]

    result = get_exif_info(path, filename)

    if result > 0:
        print "Saved histogram"
    elif result == 0:
        print "No images found"
    else:
        print "Path not valid"
