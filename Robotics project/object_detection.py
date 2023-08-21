from time import sleep
import RPi.GPIO as GPIO
import serial
from Get_Info import *
import cv2
import numpy as np
from picamera2 import Picamera2
import time

picam2 = Picamera2()




def Motor_control(M1, M2, Run, Mode):
    if(M1 == 0):
        GPIO.output(IN1, GPIO. LOW)
        GPIO.output(IN2, GPIO.LOW)
    if(M2 == 0):
        GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    if(M1 > 0):
        if(Mode == 0):
            pwm_f.ChangeDutyCycle(10)
            if(calculate_distance_f()< 50):
                print("Obstical Front Left")
                O_V(1.1) 

        PWMA.ChangeDutyCycle(M1)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
    if(M1 < 0):

#print(-1*M1)
    if(Mode == 0):
#servo.angle = 90
        pwm_r.ChangeDutyCycle(5)
#sleep(0.5)
    if(calculate_distance_r()< 50):
        print("Obstical Back Left")
        O_V(2.1)
    PWMA.ChangeDutyCycle(-1*M1)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH

#OBJECT FOLLOWING
#pan=Servo(pin=13)
#tilt=Servo(pin=12)
panAngle=0
tiltAngle=0
#pan.set_angle(panAngle)
# tilt.set_angle(tiltAngle)
def TrackX(val):
global xPos
xPos=val
#print('x Poistion', xPos)

def TrackY(val):
global yPos
yPos=val
#print('y Poistion', yPos)
def TrackW(val):
global boxW
boxW=val
#print('Box width', boxW)
def TrackH(val):
global boxH
boxH=val
#print('Box height', boxH)
dispW=1280
dispH=720
picam2.preview_configuration.main.size = (dispW,dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate=30
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor=(0,0,255)
upperLeft=(250,20)
lowerRight=(800,650)
rColor=(255,0,255)
thickness=3
# hueLow=115
# hueHigh=130
# satLow=100
# satHigh=255
# valLow=100
# valHigh=255
#lowerBound=np.array([hueLow,satLow,valLow])
#upperBound=np.array([hueHigh,satHigh,valHigh])

cv2.namedWindow('My Trackbars')
cv2.createTrackbar('X Pos','My Trackbars',10,dispW-1,TrackX)
cv2.createTrackbar('Y Pos','My Trackbars',10,dispH-1,TrackY)
cv2.createTrackbar('Box Width','My Trackbars',10,dispW-1,TrackW)
cv2.createTrackbar('Box Height','My Trackbars',10,dispH-1,TrackH)
def onTrack1(val):
global hueLow
hueLow=val
#print('hueLow', hueLow)
def onTrack2(val):
global hueHigh
hueHigh=val
#print('hueHigh', hueHigh)
def onTrack3(val):
global satLow
satLow=val
#print('satLow', satLow)

def onTrack4(val):
global satHigh
satHigh=val
#print('satHigh', satHigh)
def onTrack5(val):
global valLow
valLow=val
#print('valLow', valLow)
def onTrack6(val):
global valHigh
valHigh=val
#print('valHigh', valHigh)
cv2.namedWindow('My Trackbar Colours')
cv2.createTrackbar('hueLow','My Trackbar Colours',1,179,onTrack1)
cv2.createTrackbar('hueHigh','My Trackbar Colours',68,179,onTrack2)
cv2.createTrackbar('satLow','My Trackbar Colours',71,255,onTrack3)
cv2.createTrackbar('satHigh','My Trackbar Colours',255,255,onTrack4)
cv2.createTrackbar('valLow','My Trackbar Colours',100 ,255,onTrack5)
cv2.createTrackbar('valHigh','My Trackbar Colours',255,255,onTrack6)

if GPIO.input(button2)==0:
tStart=time.time()
im= picam2.capture_array()
imHSV=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
lowerBound=np.array([hueLow,satLow,valLow])
upperBound=np.array([hueHigh,satHigh,valHigh])

myMask =cv2.inRange(imHSV,lowerBound,upperBound)
myMaskSm=cv2.resize(myMask,(int(dispW/2),int(dispH/2)))
objectofInterest=cv2.bitwise_and(im,im,mask=myMask)
objectofInterestSm=cv2.resize(objectofInterest,(int(dispW/2),int(dispH/2)))
contours, junk= cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
if len(contours)>0:
contours=sorted(contours, key=lambda x:cv2.contourArea(x), 
reverse=True)
cv2.drawContours(im,contours,0,(255,0,0),3)
contour=contours[0]
x,y,w,h=cv2.boundingRect(contour)
cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)
error=(x+w/2)-dispW/2
robot_dir = int(error/6)
area = int((w*h)/100)
#print(area)
if(area == 0):
Motor_control(0, 0, 0, 0)

if((area > 30) and (area < 130)):
print("dead zone")
if(robot_dir < 0):
#print("Right motor ON")
Motor_control(100, 0, 0, 0)
if(robot_dir > 0):
#print("Left motor ON")
Motor_control(0, 100, 0, 0)
if(area < 30) and (area > 1):
print("forward")
Motor_control(100, 100, 0, 0)
if(area > 130):
print("backward")
Motor_control(-100, -100, 0, 0)
cv2.putText(im,str(int(fps))+' FPS',pos,font,height,myColor,weight)
cv2.rectangle(im,(xPos,yPos),(xPos+boxW,yPos+boxH),rColor,thickness)
ROI=im[yPos:yPos+boxH,xPos:xPos+boxW]
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULL
SCREEN)
cv2.imshow("window", im)
#cv2.imshow("Object of Interest",objectofInterestSm)

#cv2.imshow("myMask",myMaskSm)
if cv2.waitKey(1)==ord('q'):
break
tEnd=time.time()
loopTime=tEnd-tStart
fps=.9*fps + .1*(1/loopTime)
