from motor import Tesla_motor
from ultrasonic import Ultrasonic
import wiringpi as wp

def my():
    wp.wiringPiSetupGpio()
    wp.wiringPiSetup()
    uls = Ultrasonic(20, 21)
    tesla  = Tesla_motor(23,18,25,24)
    tesla.allStop()
    while 1:
        distance = uls.distance()
        print(distance)
        if distance > 50:
            tesla.forwardDrive()
        #sleep(5)
        else: 
            tesla.reverseDrive()
    
    

my()