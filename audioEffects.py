from pysndfx import AudioEffectsChain
from sys import argv
from librosa import load
import os
file, dir = argv

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

subdirectories = os.listdir(dir)
subdirectories.pop()

subdirectories = [dir + "/" + subDirName for subDirName in subdirectories]


input = '01-C.wav'
output = 'C-edited.wav'


fx(input, output)

y, sr = load(input, sr=None)
x = fx(y)

y = fx(input)

fx(x, output)


