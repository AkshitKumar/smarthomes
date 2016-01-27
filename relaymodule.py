import os
import psycopg2
import urlparse
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('postgres://gsngmlylshjzpx:e0xQCVlwPalL5sJxuMviyubgxO@ec2-107-20-222-114.compute-1.amazonaws.com:5432/d3ffantdtd5sjo')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()

while 1:
    cur.execute("""SELECT * FROM devices WHERE rpi_id='b8:27:eb:93:16:b2' ORDER BY id""")
    rows = cur.fetchall()
    deviceStates = dict()
    deviceName = []
    for row in rows:
	deviceStates[row[1]] = row[2]
	deviceName.append(row[1])
    d1 = deviceStates[deviceName[0]]
    d2 = deviceStates[deviceName[1]]
    d3 = deviceStates[deviceName[2]]
    if(d1 == False and d2 == False and d3 == False):
	GPIO.output(36,0)
	GPIO.output(38,0)
	GPIO.output(40,0)
	print "000"
    elif(d1 == False and d2 == False and d3 == True):
        GPIO.output(36,1)
	GPIO.output(38,0)
	GPIO.output(40,0)
	print "001"
    elif(d1 == False and d2 == True and d3 == False):
        GPIO.output(36,0)
	GPIO.output(38,1)
	GPIO.output(40,0)
	print "010"
    elif(d1 == False and d2 == True and d3 == True):
	GPIO.output(36,1)
	GPIO.output(38,1)
	GPIO.output(40,0)
	print "011"
    elif(d1 == True and d2 == False and d3 == False):
        GPIO.output(36,0)
	GPIO.output(38,0)
	GPIO.output(40,1)
	print "100"
    elif(d1 == True and d2 == False and d3 == True):
	GPIO.output(36,1)
	GPIO.output(38,0)
	GPIO.output(40,1)
	print "101"
    elif(d1 == True and d2 == True and d3 == False):
	GPIO.output(36,1)
	GPIO.output(38,1)
	GPIO.output(40,0)
	print "110"
    elif(d1 == True and d2 == True and d3 == True):
	GPIO.output(36,1)
	GPIO.output(38,1)
	GPIO.output(40,1)
	print "111"
    else:
	print "Check code"
    time.sleep(5) 
