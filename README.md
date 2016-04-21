simple script which extracts exif data for a given directories containing either 'jpg' or 'JPG' images
and prints the focal length into a histogram

you can choose between



exifReader.py

and run with

python getExifInfo.py $PATH_TO_DIRECTORY_CONTAINING_PICTURES$  $PATH_AND_NAME_OF_HISTOGRAM$(optinal)

Requirements:
-- PIL, fractions, matplotlib, numpy
______________________________________________________________________________

Additionally serverFlask.py has a nicer interface using flask and bootstrap (uses exifReady.py)

in order to run:

python serverFlask.py and then open http://127.0.0.1:5000/ in your browser


Additional Requirements:
-- flask, exifReader, datetime

