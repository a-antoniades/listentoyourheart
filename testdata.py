import serial

# data
ser = serial.Serial('/dev/cu.usbmodem14101')

ser_bytes = ser.readline() #discard first line

n = 0

while True:
    try:
        ser_bytes = ser.readline().decode("utf=8")
        beat = int(ser_bytes[5:7])
        print(beat)
        factor = 4 * ((beat - 40) / 100)
        print(factor)

    except ValueError:
        print("")

