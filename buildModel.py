#!/usr/local/bin/python2
from pyAudioAnalysis import audioTrainTest as aT
import os
from sys import argv

file, dir = argv

subdirectories = os.listdir(dir)
subdirectories.pop(0)

subdirectories = [dir + "/" + subDirName for subDirName in subdirectories]

print(subdirectories)
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False)