from motor import Tesla_motor
import wiringpi as wp
from time import sleep

def my():
    wp.wiringPiSetupGpio()
    wp.wiringPiSetup()
    tesla  = Tesla_motor(23,18,25,24)
    tesla.allStop()
    #1
    tesla.forwardDrive()
    sleep(5)
    tesla.allStop()
    #2
    tesla.reverseDrive()
    sleep(5)
    tesla.allStop()
    #3
    tesla.forwardTurnLeft()
    sleep(1)
    tesla.allStop()
    tesla.forwardDrive()
    sleep(3)
    tesla.allStop()    
    #4
    tesla.reverseTurnRight()
    sleep(1)
    tesla.allStop()
    tesla.reverseDrive()
    sleep(3)
    tesla.allStop()
    #5
    tesla.forwardDrive()
    sleep(2)
    tesla.allStop()
    tesla.spinLeft()
    sleep(1)
    tesla.allStop()
    #6
    tesla.reverseDrive()
    sleep(2)
    tesla.allStop()
    tesla.SpinRight()
    sleep(1)
    tesla.allStop()
    
my()

