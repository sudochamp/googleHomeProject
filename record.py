import pyaudio
import wave
import time
import os
from sys import argv

script, fileName, category = argv

class AudioFile:
	chunk = 1024

	def __init__(self,file):
		self.wf = wave.open(file, 'rb')
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format= self.p.get_format_from_width(self.wf.getsampwidth()), channels=self.wf.getnchannels(), rate = self.wf.getframerate(), output = True)

	def play(self):
		data = self.wf.readframes(self.chunk)
		while data != '':
			self.stream.write(data)
			data = self.wf.readframes(self.chunk)
	def close(self):
		self.stream.close()
		self.p.terminate()

def record(argv):
    FORMAT = pyaudio.paInt16
    chunk = 1024
    RATE = 44100
    frames = []
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=chunk)

    path = "trainingData/" + category

    if not os.path.exists(path):
        os.makedirs(path)

    print("Recording...")

    for i in range(0, int(RATE / chunk * 3)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    print("Done Recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("trainingData/" + category + "/" + fileName + ".wav", 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def record_main(argv):
    FORMAT = pyaudio.paInt16
    chunk = 1024
    RATE = 44100
    frames = []
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=chunk)

    path = "trainingData/" + category

    if not os.path.exists(path):
        os.makedirs(path)

    print("Recording main command...")

    for i in range(0, int(RATE / chunk * 3)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    print("Done Recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("commands/" + fileName + ".wav", 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

record_main("main")

numberOfRecordings = 0

while numberOfRecordings < 4:
    fileName = fileName + "{}".format(numberOfRecordings)
    numberOfRecordings += 1
    record(fileName)
    if numberOfRecordings == 3:
        break
