#!/usr/bin/python
import cv2
import sys
import os
import fnmatch

# import openCV library, used to process images

def resizeFile( fname, width, height ):
    "This is the file name passed in:"
    print (fname)
    image = cv2.imread(fname)

    org_height, org_width = image.shape[0:2] 
    print("height: " , org_height)
    print("width: " ,  org_width)
   
    if org_width > org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))


    #Show image for testing
    # cv2.imshow('Resized Image', newImg)
    # cv2.waitKey(0)
    import os
    if not os.path.exists('new_folder'):
        os.makedirs('new_folder')
      
    cv2.imwrite( "new_folder\\" + fname, new_image);
    return


 

#for path, dirs, files in os.walk(os.getcwd()):
      # for filename in files:
        # if filename.endswith(".jpg"):

listOfFiles = os.listdir('.')  
pattern = "*.jpg"  

for filename in listOfFiles:  
        if fnmatch.fnmatch(filename, pattern):
            resizeFile(filename, int(sys.argv[1]), int(sys.argv[2]))

