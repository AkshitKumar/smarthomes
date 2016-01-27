import smbus
import time
bus = smbus.SMBus(1)
import urlparse
import psycopg2

# This is the address we setup in the Arduino Program
address = 0x05

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse('postgres://gsngmlylshjzpx:e0xQCVlwPalL5sJxuMviyubgxO@ec2-107-20-222-114.compute-1.amazonaws.com:5432/d3ffantdtd5sjo')

"""conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)"""
"""cur = conn.cursor()"""
def writeNumber(value):
	bus.write_byte(address, value)

#while(1):
#	for i in range(100):
#		writeNumber(i)
#		time.sleep(1)


def readNumber():
	arr = [0]*4
	for i in range(4):
		arr[i] =  bus.read_byte(address)
	return arr

while(1):
	values = readNumber()
	#temp = str(values[1])
	#hum = str(values[0])
	#SQL = "UPDATE sensors SET value = (%s) WHERE id = 1 AND rpi_id = 'b8:27:eb:93:16:b2'"
	#data = (str(temp),)
	#cur.execute(SQL,data)
	#SQL2 = "UPDATE sensors SET value = (%s) WHERE id = 2 AND rpi_id = 'b8:27:eb:93:16:b2'"
	#data = (str(hum),) 
	#cur.execute(SQL,data)
	#conn.commit()
	print values
	time.sleep(10)
	
