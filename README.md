"# jpeg-resizer" 
# Description: takes ever jpeg file (ending in .jpg) in a directory, resizes it to the
 pixel length and width indicated on the command line. Stores each image into a directory
 called new_folder. It automatically detects landscape or portrait in the original picture.

# Usage
Unzip the archive into your user directory
edit the PATH variable to point to the directory (containing the image_resize.exe file).
Go into the folder containing jpg files.
run as follows:
image_resize.py 1280 960
# or, after making a dist executable with pyinstaller image_resize.py:
image_resize 1280 960
