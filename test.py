# coding: utf-8
#Define Libraries
# import RPi.GPIO as gpio
import time

class Test:

    def motor(self, pos):
        print("teste aqui", pos)
        #Configuring don’t show warnings
        # gpio.setwarnings(False)
        #
        # #Configuring GPIO
        # gpio.setmode(gpio.BOARD)
        # gpio.setup(40,gpio.OUT)
        #
        # #Configure the pwm objects and initialize its value
        # pwm_motor = gpio.PWM(40,100)
        # pwm_motor.start(0)
        #
        # #Create the dutycycle variables
        # dcMotor = 100
        #
        # #Loop infinite
        # while True:
        #     #increment gradually the luminosity
        #     pwm_motor.ChangeDutyCycle(dcMotor)
        #     time.sleep(0.05)
        #     # dcMotor = dcMotor + 1
        #     # if dcMotor == 100:
        #     #     dcMotor = 0
        #
        # #End code
        # gpio.cleanup()
        # exit()
