import cv2 as cv
from mtcnn.mtcnn import MTCNN

def bounding_box(image):
    detector = MTCNN()
    faces = detector.detect_faces(image)

    for face in faces:
        x, y, w, h = face['box']
        keypoints = face['keypoints']

        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(image, keypoints['left_eye'], 2, (0, 0, 255), 2)
        cv.circle(image, keypoints['right_eye'], 2, (0, 0, 255), 2)
        cv.circle(image, keypoints['nose'], 2, (0, 0, 255), 2)
        cv.circle(image, keypoints['mouth_left'], 2, (0, 0, 255), 2)
        cv.circle(image, keypoints['mouth_right'], 2, (0, 0, 255), 2)

    return image

# Open the webcam
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Apply face detection
    marked_frame = bounding_box(frame)

    # Display the resulting frame
    cv.imshow('Face Detection', marked_frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# test
# Release the webcam and close all windows
cap.release()
cv.destroyAllWindows()