import numpy as np
import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('indiahacks3.avi',fourcc, 20.0, (848,480) )

cap = cv2.VideoCapture(0)
count=0;
while(count<400):
    # Capture frame-by-frame
    ret, frame = cap.read()
    x=frame.shape
    print x
    out.write(frame) ;
    # Display the resulting frame
    cv2.imshow('frame',frame)
    count=count+1;
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
