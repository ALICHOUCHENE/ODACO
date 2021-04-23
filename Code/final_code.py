import time
import snowboydecoder
import sys
import signal
from pygame import mixer
import socket
from threading import Thread
import serial
import os
import random

time.sleep(5)
 os.system("sudo rfcomm connect0 98:D3:B1:FD:6D:AE & ")
 ble=serial.Serial("/dev/rfcomm0",9600)
 ble.write('connected to HC05'.encode())
 
try:
    ser=serial.Serial('/dev/ttyUSB0',9600)
except:
    ser=serial.Serial('/dev/ttyUSB1',9600)
finally:
    print('connected to arduino nano')


 
 HOST = '192.168.1.113' # Server IP or Hostname
 PORT = 1024 # Pick an open Port (1000+ recommended), must match the client sport
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 print ('Socket created')
 try:
     s.bind((HOST, PORT))
 except socket.error:
     print ('Bind failed ')
 
 
 s.listen(5)
 print ('Socket awaiting messages')
 (conn, addr) = s.accept()
 print ('Connected')

def speak(path):
    mixer.init()
    mixer.music.load('/'+path)
    mixer.music.play()

def motivate(ch):
    trois = ["trois_lettres_1" , "trois_lettres_2"]
    quatre = ["quatre_lettres_1","quatre_lettres_2"]
    zero = ["zero_lettres_1", "zero_lettres_2","zero_lettres_3"]
    if len(ch)==1:
        if (ch == 'a'):
            speak("home/pi/odaco/snowboy/bras_droite.mp3")
        if (ch == 'b'):
            speak("home/pi/odaco/snowboy/bras_gauche.mp3")
        if (ch == 'c'):
            speak("home/pi/odaco/snowboy/jambe_gauche.mp3")
        if (ch == 'd'):
            speak("home/pi/odaco/snowboy/jambe_droite.mp3")
        if (ch == 'j'):
            speak("home/pi/odaco/snowboy/"+random.choice(zero)+".mp3")

    elif len(ch)==2:
        if (ch == 'ab') or (ch == 'ba'):
            speak("home/pi/odaco/snowboy/partie_superieure.mp3")
        elif (ch == 'cd') or (ch == 'dc'):
            speak("home/pi/odaco/snowboy/partie_inferieure.mp3")
        else:
            a = random.randrange(1)
            motivate(ch[a])
    elif len(ch)==3:
        speak("home/pi/odaco/snowboy/"+random.choice(trois)+".mp3")
    elif len(ch) == 4:
        speak("home/pi/odaco/snowboy/"+random.choice(quatre)+".mp3")


def display():
    print("displaying")
    speak("home/pi/odaco/snowboy/displayvoc.mp3")
#     conn.send('do display')

def start():
    print("starting")
    speak("home/pi/odaco/snowboy/startvoc.mp3")
#     conn.send("do start")
    
def stop():
    print("stoping")
    speak("home/pi/odaco/snowboy/stopvoc.mp3")
#     conn.send("do stop")
    
def repeat():
    print("repeating")
    speak("home/pi/odaco/snowboy/repeatvoc.mp3")
#     conn.send('do repeat')
def back():
    print("previous exercise running")
    speak("home/pi/odaco/snowboy/backvoc.mp3")
#     conn.send('do back')
def nexte():
    print("moving to the next exercise")
    speak("home/pi/odaco/snowboy/nextvoc.mp3")
#     conn.send("do next")


# models = ["starte.pmdl", "stope.pmdl", "displaye.pmdl", "repeate.pmdl", "nextee.pmdl", "backe.pmdl"]


def vocal() :
    models = ["odaco_start.pmdl", "odaco_stop.pmdl", "odaco_suivant.pmdl", "odaco_precedent.pmdl"]
#     signal.signal(signal.SIGINT, signal_handler)

    sensitivity = [0.52, 0.43, 0.44, 0.5]
    detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
    callbacks = [lambda: start(),
                 lambda: stop(),
                 lambda: nexte(),
                 lambda: back()]

    detector.start(detected_callback=callbacks, sleep_time=0.1)
    detector.terminate()
    
 def ahl():
     
     while True:
         data = conn.recv(1024)
         data = data.decode()
         motivate(str(data))
         print(data)
         ble.write(data.encode())
        

def commande ():
    while True :
        cmd=ser.readline()
        cmd=cmd.decode('utf-8')
        conn.send(str(cmd))

        print(cmd)


if __name__ == "__main__":
    t1 = Thread(target = vocal)
    t2 = Thread(target = ahl)
    t3 = Thread (target = commande)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    while True:
        pass


