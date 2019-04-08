
"""
Muslim Kholjuraev
"""
 
from gpiozero import PWMOutputDevice
from time import sleep

class Tesla_motor:
    
    def __init__(self, pin1, pin2, pin3, pin4):

        # Motor A, Left Side GPIO CONSTANTS
        self.PWM_FORWARD_LEFT_PIN = pin1   # IN1 - Forward Drive 18
        self.PWM_REVERSE_LEFT_PIN = pin2   # IN2 - Reverse Drive 23
        
        # Motor B, Right Side GPIO CONSTANTS
        self.PWM_FORWARD_RIGHT_PIN = pin3  # IN1 - Forward Drive 24 
        self.PWM_REVERSE_RIGHT_PIN = pin4  # IN2 - Reverse Drive 25
        self.set_pwm()
 
    def set_pwm(self):
         
        # Initialise objects for H-Bridge PWM pins
        # Set initial duty cycle to 0 and frequency to 1000
        self.forwardLeft = PWMOutputDevice(self.PWM_FORWARD_LEFT_PIN, True, 0, 100)
        self.reverseLeft = PWMOutputDevice(self.PWM_REVERSE_LEFT_PIN, True, 0, 100)
         
        self.forwardRight = PWMOutputDevice(self.PWM_FORWARD_RIGHT_PIN, True, 0, 100)
        self.reverseRight = PWMOutputDevice(self.PWM_REVERSE_RIGHT_PIN, True, 0, 100)
 
 
    def allStop(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 0
        self.forwardRight.value = 0
        self.reverseRight.value = 0
 
    def forwardDrive(self):
        self.forwardLeft.value = 1.0
        self.reverseLeft.value = 0
        self.forwardRight.value = 1.0
        self.reverseRight.value = 0
 
    def reverseDrive(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 1.0
        self.forwardRight.value = 0
        self.reverseRight.value = 1.0
 
    def spinLeft(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 1.0
        self.forwardRight.value = 1.0
        self.reverseRight.value = 0
 
    def SpinRight(self):
        self.forwardLeft.value = 1.0
        self.reverseLeft.value = 0
        self.forwardRight.value = 0
        self.reverseRight.value = 1.0
 
    def forwardTurnLeft(self):
        self.forwardLeft.value = 0.2
        self.reverseLeft.value = 0
        self.forwardRight.value = 0.8
        self.reverseRight.value = 0
 
    def forwardTurnRight(self):
        self.forwardLeft.value = 0.8
        self.reverseLeft.value = 0
        self.forwardRight.value = 0.2
        self.reverseRight.value = 0
 
    def reverseTurnLeft(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 0.2
        self.forwardRight.value = 0
        self.reverseRight.value = 0.8
 
    def reverseTurnRight(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 0.8
        self.forwardRight.value = 0
        self.reverseRight.value = 0.2
    def run_very_slow(self):
        self.forwardLeft.value = 0.1
        self.reverseLeft.value = 0.1
        self.forwardRight.value = 0.1
        self.reverseRight.value = 0.1
 
    '''def main():
    
    allStop()
    forwardDrive()
    sleep(5)
    reverseDrive()
    sleep(5)
    spinLeft()
    sleep(5)
    SpinRight()
    sleep(5)
    forwardTurnLeft()
    sleep(5)
    forwardTurnRight()
    sleep(5)
    reverseTurnLeft()
    sleep(5)
    reverseTurnRight()
    sleep(5)
    allStop()

    
'''

 
