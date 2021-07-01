from machine import Pin, UART
import time
#Configure the serial port
uart = UART(0, 9600, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
#uart = UART(1, 9600, bits=8, parity=None, stop=1, tx=Pin(4), rx=Pin(5))
#Serial port control servo function
def UARTServo(servonum, angle):
    servonum = 64 + servonum
    date1 = int(angle/100 + 48)
    date2 = int((angle%100)/10 + 48)
    date3 = int(angle%10 + 48)
    cmd=bytearray([36,servonum,date1,date2,date3,35])
    uart.write(cmd)
    time.sleep(0.05)

UARTServo(1,0)
time.sleep(2)
UARTServo(1,180)
time.sleep(2)

