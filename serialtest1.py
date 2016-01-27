from serial import Serial
import time

ser = Serial('/dev/ttyAMA0',9600,timeout=0.005)
ser.close()
ser.open()
#ser.write("testing")
try:
	while 1:
		state = ser.readline()
		print state
		time.sleep(0.4)
except:
	print "Error"
	#time.sleep(4)
