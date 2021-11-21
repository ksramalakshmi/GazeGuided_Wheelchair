import cv2
import dlib
from scipy.spatial import distance
import pyautogui
import time
from time import perf_counter
import webbrowser
from selenium import webdriver
import os
import sys

global next_time
flag = True

def game():
    url = 'http://docs.python.org/'         
    chrome = webdriver.Chrome()
    #chrome.get(url)
    next_time = time.time()
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    #chrome.navigate().refresh()
    t1_start = time.time()

    def calculate_EAR(eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear_aspect_ratio = (A+B)/(2.0*C)
        return ear_aspect_ratio

    def jump():
        pyautogui.keyDown('space')
        time.sleep(0.01)
        print("jump")
        pyautogui.keyUp('space')


    cap = cv2.VideoCapture(0)
    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    #chrome.navigate().refresh()
    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = hog_face_detector(gray)
        for face in faces:

            face_landmarks = dlib_facelandmark(gray, face)
            leftEye = []
            rightEye = []

            for n in range(36,42):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                leftEye.append((x,y))
                next_point = n+1
                if n == 41:
                    next_point = 36
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

            for n in range(42,48):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                rightEye.append((x,y))
                next_point = n+1
                if n == 47:
                    next_point = 42
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

            left_ear = calculate_EAR(leftEye)
            right_ear = calculate_EAR(rightEye)

            EAR = (left_ear+right_ear)/2
            EAR = round(EAR,2)
            # print(EAR)
            if EAR<0.26:
                jump()
                
                # cv2.putText(frame,"JUMP",(20,100), cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
                # cv2.imwrite("image.jpg",frame)

        cv2.imshow("Dino Game", frame)

        now_time = time.time()
        if (now_time - next_time < 21):
            continue
        elif (now_time - next_time >= 21):
            cap.release()
            cv2.destroyAllWindows()
            chrome.close() 
            os.system("python hover.py")
            os.system("killall -9 'Google Chrome'")
            os.system("networksetup -setairportpower airport on")
            break

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    chrome.close()
    cap.release()
    cv2.destroyAllWindows()
    return 

os.system("networksetup -setairportpower airport off")
game()
os.system("networksetup -setairportpower airport on")
while True:
    try:
        os.system("python hover.py")
        sys.exit()
    except:
        continue
