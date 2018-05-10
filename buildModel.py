#!/usr/local/bin/python2
from pyAudioAnalysis import audioTrainTest as aT
import os
from sys import argv

file, dir = argv 

subdirectories = os.listdir(dir) #Finds all dirs inside the dir specified above
subdirectories.pop(0) #Populates an array

subdirectories = [dir + "/" + subDirName for subDirName in subdirectories] #Formatting

print(subdirectories)
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False) #featureAndTrain(listOfDirs, mtWin, mtStep, stWin, stStep, classifierType, modelName, computeBEAT
