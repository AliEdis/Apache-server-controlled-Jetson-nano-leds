
import RPi.GPIO as GPIO

import time 
 
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
time.sleep(2) 

while True: 
  
 
  
  GPIO.output(led_pin1, GPIO.HIGH) 
  time.sleep(2) 
  GPIO.output(led_pin2, GPIO.HIGH)
  time.sleep(2) 
  GPIO.output(led_pin3, GPIO.HIGH)
  time.sleep(2) 
  GPIO.output(led_pin4, GPIO.HIGH)
  time.sleep(2) 
  GPIO.output(led_pin5, GPIO.HIGH)
  time.sleep(5) 

  GPIO.output(led_pin1, GPIO.LOW) 
  time.sleep(2) 
  GPIO.output(led_pin2, GPIO.LOW)
  time.sleep(2) 
  GPIO.output(led_pin3, GPIO.LOW)
  time.sleep(2) 
  GPIO.output(led_pin4, GPIO.LOW)
  time.sleep(2) 
  GPIO.output(led_pin5, GPIO.LOW)

  

