import cv2
import serial
import sys
import os
import time
from gaze_tracking import GazeTracking
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome = webdriver.Chrome()
chrome.get('http://127.0.0.1:5500/web/move.html')
ser = serial.Serial('/dev/cu.usbmodem14201', 9600, timeout = 1)

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
l=list()
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    try:
        gaze.refresh(frame)
    except:
        pass

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"

    elif gaze.is_right():
        text = "Looking right"
  
    elif gaze.is_left():
        text = "Looking left"

    elif gaze.is_center():
        text = "Looking center"

    if len(l)==0:
        l.append(text)
    elif l[0]!=text:
        l = list()
        l.append(text)
    elif len(l)==9:
        print(text)
        l = list()
        if (text == "Looking left"):
            start = time.time()
            while True:
                ser.write(b'l')
                time.sleep(0.5)
                end = time.time()
                if end - start >= 5:
                    break
            time.sleep(0.5)
        elif text == "Looking right":
            start = time.time()
            while True:
                ser.write(b'r')
                time.sleep(0.5)
                end = time.time()
                if end - start >= 5:
                    break
            time.sleep(0.5)
        elif text == "Blinking":
            start = time.time()
            while True:
                #ser.write(b's')
                #time.sleep(0.5)
                end = time.time()
                if end - start >= 5:
                    ser.close()
                    webcam.release()
                    cv2.destroyAllWindows()
                    chrome.close()
                    os.system("python hover.py")
                    sys.exit()
                    #break
            #time.sleep(0.5)
        elif text == "Looking center":
            start = time.time()
            while True:
                ser.write(b'f')
                time.sleep(0.5)
                end = time.time()
                if end - start >= 5:
                    break
            time.sleep(0.5)
    else:
        l.append(text)

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (255,178,45), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255,178,45), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255,178,45), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


ser.close()
webcam.release()
cv2.destroyAllWindows()
chrome.close()
os.system("python hover.py")
sys.exit()