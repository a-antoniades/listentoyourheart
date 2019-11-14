import serial
from aupyom import Sampler, Sound
from aupyom.util import example_audio_file

# start playing
sampler = Sampler()

audio_file = "/Users/antonis/PycharmProjects/listentoyourheart/Travis Scott - SICKO MODE (Official Audio)-192.mp3"
s1 = Sound.from_file(audio_file)

sampler.play(s1)

# data
ser = serial.Serial('/dev/cu.usbmodem14101')

first_line = ser.readline() #discard first line

while True:
    try:
        ser_bytes = ser.readline().decode("utf=8")
        beat = int(ser_bytes[5:7])
        print(beat)
        factor = (4 * ((beat - 40) / 100))
        print(factor)
        s1.stretch_factor = factor

    except ValueError:
        print("")

    except ZeroDivisionError:
        print("")

    except beat < 40:
        print("")

