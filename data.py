import serial
import numpy as np


ser = serial.Serial('/dev/cu.usbmodem14101')

beats = np.array([])
no_beats = np.count_nonzero(beats)

first_line = ser.readline()

while True:
    ser_bytes = ser.readline()
    print(ser_bytes)
    if no_beats < 5:
        np.append(beats, ser_bytes)

    elif no_beats == 5:
        av_beats = np.sum(beats)/5
        print(av_beats)

