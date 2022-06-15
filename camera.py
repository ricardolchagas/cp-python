import cv2 as cv
cap  = cv.VideoCapture(2)
# out = cv.VideoWriter('output2.mkv', cv.VideoWriter_fourcc('X', 'V', 'I', 'D'), 30, (1920, 1080))
frame_number = 0

while True:
    grabed, frame = cap.read()
   
    if not grabed:
        break
    
    frame_number += 1
    cv.putText(frame, 'Capturando...', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv.putText(frame, str(frame_number), (10, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv.imshow('frame', frame)
    # out.write(frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
# out.release()