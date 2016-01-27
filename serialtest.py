from serial import Serial
import time

ser = Serial('/dev/ttyAMA0',9600,timeout=0.005)
ser.close()
ser.open()
while True:
    print "hi"
    ser.write(raw_input(">>"))
    time.sleep(2)
    #print ser.readline()
    #time.sleep(4)
