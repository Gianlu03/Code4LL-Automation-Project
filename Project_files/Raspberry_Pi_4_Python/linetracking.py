import RPi.GPIO as GPIO
import time

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

GPIO.setmode(GPIO.BCM)

'''#Definizione dei 3 sensori a infrarossi come pin di input'''
GPIO.setup(line_pin_right, GPIO.IN)
GPIO.setup(line_pin_middle, GPIO.IN)
GPIO.setup(line_pin_left, GPIO.IN)


'''
    3 Funzioni degli stati dei 3 sensori
'''
def status_right():
    return GPIO.input(line_pin_right)
def status_left():
    return GPIO.input(line_pin_left)
def status_middle():
    return GPIO.input(line_pin_middle)
    
#while True:
#    print("Left: %d, Middle: %d, Right %d" % (status_left(), status_middle(), status_right()))
