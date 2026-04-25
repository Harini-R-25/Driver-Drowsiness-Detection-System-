import cv2
import dlib
import os
from scipy.spatial import distance

# ---------- TEXT TO SPEECH ----------
def speak_alert():
    os.system('espeak "Drowsiness alert. Please wake up immediately"')

# ---------- EAR FUNCTION ----------
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# ---------- LOAD MODELS ----------
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

LEFT_EYE = [36,37,38,39,40,41]
RIGHT_EYE = [42,43,44,45,46,47]

EYE_THRESHOLD = 0.25
EYE_FRAMES = 10

counter = 0

# ---------- START CAMERA ----------
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:

        landmarks = predictor(gray, face)

        leftEye = [(landmarks.part(i).x, landmarks.part(i).y) for i in LEFT_EYE]
        rightEye = [(landmarks.part(i).x, landmarks.part(i).y) for i in RIGHT_EYE]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        # ---------- CHECK DROWSINESS ----------
        print(ear)
        if ear < EYE_THRESHOLD:
            counter += 1
            print(counter)
            if counter >= EYE_FRAMES:
                speak_alert()
                cv2.putText(frame,
                            "DROWSINESS ALERT!",
                            (10,30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0,0,255),
                            2)

        else:
            counter = 0

        # Draw rectangle around face
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow("Driver Monitor", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
