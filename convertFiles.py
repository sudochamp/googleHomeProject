from mutagen import wavpack
import os
from sys import argv

dir = "trainingData"

subdirectories = os.listdir(dir)

for i, dirs in enumerate(subdirectories):
    for audioDir in dirs.split():
        audioFiles = os.listdir("trainingData/" + str(audioDir))
        print(audioFiles[0])

conversionFile = wavpack("trainingData/A/03-A.wav")