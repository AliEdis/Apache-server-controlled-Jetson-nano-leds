import mysql.connector
import cv2
import imutils
import RPi.GPIO as GPIO
 
led_pin1 = 40
led_pin2 = 35
led_pin3 = 36
led_pin4 = 37
led_pin5 = 38
 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin1, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(led_pin2, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(led_pin3, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(led_pin4, GPIO.OUT, initial=GPIO.LOW)  
GPIO.setup(led_pin5, GPIO.OUT, initial=GPIO.LOW) 

GREEN='\033[92m'
cap=cv2.VideoCapture(0)
while True:

 _,img=cap.read()
 img=cv2.flip(img,1)
 mysqldb = mysql.connector.connect(
    host="localhost",
    user="sammy",
    password="Password123#@!",
    database="coral"
 )
 cursor = mysqldb.cursor()
 cursor.execute ("Select id,led_status FROM led")
 for id,led in cursor:
  
  print(f"{GREEN}" ,"ID: ", id,"LED_STATUS: ",led)
  text_format=("ID: {} | LED_STATUS: {}").format(id,led)
  led_get=str(led)
  led_len=len(led_get)

 
  cv2.rectangle(img,(0,400),(1000,600),(0,0,0),-1,lineType=cv2.LINE_AA)
  cv2.putText(
  img = img,
  text = text_format,
  org = (10, 450),
  fontFace = cv2.FONT_HERSHEY_SIMPLEX,
  fontScale = 1,
  color = (255, 255, 255),
  thickness = 2,
  lineType=cv2.LINE_AA
  )

  if(led_len==5):
    if(led_get[0]=='0'):
        GPIO.output(led_pin1, GPIO.LOW)
    else:
        GPIO.output(led_pin1, GPIO.HIGH)

    if(led_get[1]=='0'):
        GPIO.output(led_pin2, GPIO.LOW)
    else:
        GPIO.output(led_pin2, GPIO.HIGH)
 

    if(led_get[2]=='0'):
        GPIO.output(led_pin3, GPIO.LOW)
    else:
        GPIO.output(led_pin3, GPIO.HIGH)

    if(led_get[3]=='0'):
        GPIO.output(led_pin4, GPIO.LOW)
    else:
        GPIO.output(led_pin4, GPIO.HIGH)

    if(led_get[4]=='0'):
        GPIO.output(led_pin5, GPIO.LOW)
    else:
        GPIO.output(led_pin5, GPIO.HIGH)
   


  if( led_get=='0'):
      GPIO.output(led_pin1, GPIO.LOW) 
      GPIO.output(led_pin2, GPIO.LOW)
      GPIO.output(led_pin3, GPIO.LOW)
      GPIO.output(led_pin4, GPIO.LOW)
      GPIO.output(led_pin5, GPIO.LOW)
      

  if(led_get=='1'):
      
      GPIO.output(led_pin1, GPIO.HIGH) 
      GPIO.output(led_pin2, GPIO.HIGH)
      GPIO.output(led_pin3, GPIO.HIGH)
      GPIO.output(led_pin4, GPIO.HIGH)
      GPIO.output(led_pin5, GPIO.HIGH)

  cv2.imshow("img",img)
  if cv2.waitKey(1) and 0xFF==ord('q'):
   break


      


  
  
          
