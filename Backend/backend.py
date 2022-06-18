import serial
import database
import time

ser = serial.Serial("COM2", 9600, timeout=1)

while True:
    if ser.inWaiting():
        packet = ser.readline()
        decodedString = packet.decode('UTF-8').rstrip("'\n\r'")
        print(decodedString)
        database.set_data(decodedString)
