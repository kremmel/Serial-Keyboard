import serial
import msvcrt
import sys
import os


def list_serial_ports():
	available = []
	for i in range(256):
		try:
			s = serial.Serial(i)
			available.append('COM'+str(i + 1))
			s.close()
		except serial.SerialException:
			pass
	return available
	
def send(character):
	ser.write(chr(character))
	
print list_serial_ports()
ser = serial.Serial()
ser.port = int(raw_input("PORT: ")) - 1
ser.baudrate = int(raw_input("BAUDRATE: "))
ser.timeout = 10
ser.open()

while True:
	try:
		if msvcrt.kbhit():
			char = ord(msvcrt.getch())
			if char == 0:
				char = ord(msvcrt.getch())
				if char > 58 and char < 69:
					send(char+69)
			elif char == 224:
				char = ord(msvcrt.getch())
				if char == 145:
					sys.exit(0)
				elif char == 133 or char == 134:
					send(char+5)
				else:
					send(char+69)
			else:
				send(char)
	except KeyboardInterrupt:
		send(3)
		pass
		
