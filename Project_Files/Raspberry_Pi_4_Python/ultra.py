#!/usr/bin/python3
# File name   : Ultrasonic.py
# Description : Detection distance and tracking with ultrasonic
# File contenente la funzione che ritorna la distanza dal sensore ad ultrasuoni


import RPi.GPIO as GPIO
import time

Tr = 11 #Invia il segnale
Ec = 8 #Riceve il segnale

def checkdist():       #Reading distance
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)

    while not GPIO.input(Ec):
        pass
    t1 = time.time() #time () Ritorna la data in secondi dall'Epoch, avvento di Unix
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

'''
    Riassunto:
    Setta Tr come trasmettitore, Ec come ricevitore
    Viene inviato il segnale per 0.000015s
    
'''