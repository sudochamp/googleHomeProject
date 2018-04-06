from pysndfx import AudioEffectsChain
from sys import argv
from librosa import load
import os
script, dirname = argv

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

subdirectories = os.listdir(dirname)
subdirectories.pop(0)

subdirectories = [dirname + "/" + subDirName for subDirName in subdirectories]


input = '01-C.wav'
output = 'C-edited.wav'


fx(input, output)

y, sr = load(input, sr=None)
x = fx(y)

y = fx(input)

fx(x, output)


