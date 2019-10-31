# generates a json file containing musical notes and their frequencies in equal temperament tuning
import json

basefrequency = 27.5
scaleDict = {}
notes = [ 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# for i in range(12):

for octave in range(8):
    for halfstep in range(12):

        if(halfstep > 2):
            scaleDict[round(basefrequency * (2**(octave + halfstep / 12)), 2)] = notes[halfstep] + str(octave + 1)
        else:
            scaleDict[round(basefrequency * (2**(octave + halfstep / 12)), 2)] = notes[halfstep] + str(octave)

with open("scales.js", 'w') as scales:
    scales.write("scales = " + json.dumps(scaleDict))

