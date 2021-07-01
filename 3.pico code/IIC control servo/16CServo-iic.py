from machine import Pin, I2C
import time
#Configure IIC
i2c=I2C(0, scl=Pin(21),sda=Pin(20), freq=100000)
#i2c=I2C(1, scl=Pin(19),sda=Pin(18), freq=100000)
#Set IIC address
Servo_ADD = 0x2D
#IIC control servo function
def IICServo(servonum, angle):
    i2c.writeto(Servo_ADD,bytearray([servonum,angle]))
    time.sleep(0.1)

IICServo(1,0)
time.sleep(2)
IICServo(1,180)
time.sleep(2)
