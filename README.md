# ODACO

### Description : 

ODACO consists of a personnal smart trainer that allows the user to live the whole experience of a private trainning session with adapted programs, posture detection and correction, voice commands and interactions with a simple and easy interface.



![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Product/ODACO.jfif)





### My contributions : 

- Developing a voice assistant from scratch using python and Snowboy Hotword Detection toolkit.
 
- Integration of the voice assistant algorithm on Raspberry Pi while performing a Multithreading technique.
 
- Creation of the user interface Nvidia Jetson Nano board using python.

- Creation of gadgets to mesure biometric data of the user using Atmega328P microcontroller.

-Assuring the communication among different compartments via Bluetooth, socket communication and radio frequencies.

-Designing of all the electronic circuits of the system, based on AVR microcontrollers, with KiCad.

### Hardware : 

- **TH BOX :**
The box is the main part of the system.
It's based on 3 embedded boards :

- NVIDIA Jetson nano running an AI algorithm wich detect and analyse the humain posture.

- Raspberry Pi4 running the voice assistant algorithm.

- Arduino nano to communicate with the remote control, bandes and the posture belt.


**Bande :**

Those bandes will vibrate when the person make a wrong performance. 
Its circuit is based on : 

- Atmel microcontroller (Atmega328p) running at 8 MHz.

- RF433 radio receiver.

- Vibrator motor.

- Battery management system for 3.7v lipo battery.


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Product/BAND%201%20tra_.png)


- PCB View : 


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Band/Band_PCB.PNG)


- Board 3D view : 


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Band/Band_3D.PNG)




**Belt :**

This gadget is used to get biometric data of the user and send it to the Box: 
Its circuit is based on : 

- Atmel microcontroller (Atmega328p) running at 16 MHz.

- HC-06 Bluetooth Module.

- MAX30100 biometric (SPO2, Heart rate and Temperature .

- Battery management system for 3.7v lipo battery.

- Step Up Boost circuit (3.7V to 5V).


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Product/Belt.png)

- PCB View : 


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Belt/Belt_PCB.PNG)


- Board 3D view : 


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Belt/Belt_3D.PNG)




## Stay Safe : 


![alt text](https://github.com/ALICHOUCHENE/ODACO/blob/main/Product/ODACO.jpg)





