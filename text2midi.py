#! /usr/bin/python3.4

import re, string, collections, midiutil
from midiutil.MidiFile3 import MIDIFile

filename=input('What file to process? ')

with open('./'+filename, 'r', encoding='utf8') as temp:
    f=temp.read()
f=f.lower()
f=re.sub('\W',' ', f)


letters=string.ascii_lowercase
notes=['C4','C4#','D4','D4#','E4','F4','F4#','G4','G4#','A4','A4#','B4','C5','C5#','D5','D5#','E5','F5','F5#','G5','G5#','A5','A5#','B5','C6','C6#']
midi=list(range(60,86))

notemidiletter=collections.OrderedDict()
for i in range(len(letters)):
    notemidiletter[letters[i]]=(notes[i], midi[i])

for char in letters:
    f=f.replace(char, str(notemidiletter[char][1])+'.')

f=re.sub('\.,?\s',' ',f)
f=f.split()

midiwords=list()
for i in range(len(f)):
    midiwords.append(f[i].split('.'))
    
    

# Export to midi file

SampleName=input('Write the name of sample: ')

mtrack=MIDIFile(1)
track=0
time=0
mtrack.addTrackName(track, time, SampleName)

track = 0
channel = 0
pitch = 60
time = 0
duration = 4
volume = 100

for word in midiwords:
    for midinote in word:
        pitch=int(midinote)
        mtrack.addNote(track,channel,pitch,time,duration,volume)
    time+=4

binfile = open(SampleName+'.mid', 'wb')
mtrack.writeFile(binfile)
binfile.close()
