#/usr/bin/python

#use opencv to capture video from usb

import numpy as np
import cv2

#initialize camera
cap = cv2.VideoCapture(0)
if cap is None:
    print 'Warning: unable to access camera'

#stopPin = 7 # listen for a change on this pin to stop

# number of frames to acquire
numFrames = 30
currFrame = 0

#outfilebase = 'images/image' #append number + .tif

print 'starting capture of ' + str(numFrames) + ' frames.'
print 'press ctrl-c to stop ... eventually we will stop on a TTL'
while(cap.isOpened()):
    try:
        ret, frame = cap.read()
        if ret==True:
            #flip frame
            #frame = cv2.flip(frame,0)

            #print frame.shape

            # write the flipped frame
            try:
                #out.write(frame)
                #cv2.SaveImage('file' + str(currFrame) + '.tif', frame)
                cv2.imwrite('images/image' + str(currFrame) + '.tif', frame)
            except:
                print 'Error in out.write() OR user hit ctrl-c'
                break

            currFrame += 1
            #if (currFrame > numFrames):
            #    print 'finished ' + str(numFrames) + ' frames.'
            #    break
    
        else:
            break

    except KeyboardInterrupt:
        print 'user hit ctrl-c'
        print 'frames=' + str(currFrame)
        break

# Release camera
cap.release()

