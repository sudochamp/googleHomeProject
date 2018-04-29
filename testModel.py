from sys import argv
import numpy as np
import wave
import pyaudio
import sys
from pyAudioAnalysis import audioTrainTest as aT

isSignificant = 0.3



def findWinner(filename):
    #try different values.

    # P: list of probabilities
    Result, P, classNames = aT.fileClassification(filename, "svmModel", "svm")
    winner = np.argmax(P) #pick the result with the highest probability value.

    # is the highest value found above the isSignificant threshold?
    if P[winner] > isSignificant:
      print("File: " +filename + " is in category: " + classNames[winner] + ", with probability: " + str(P[winner]))
    else :
      print("Can't classify sound: " + str(P))

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

    file = AudioFile("commands/" + classNames[winner] + ".wav")
    file.play()

if __name__=='__main__':
    sys.exit(findWinner(sys.argv[1]))