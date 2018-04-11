import pyaudio
import wave
import os

def record(fileName):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)

    print("Recording...")

    chunk = 1024
    RATE = 44100
    frames = []

    for i in range(0, int(RATE/chunk * 3)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    print("Done Recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(fileName + ".wav", 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

record("G-0")
record("G-1")
record("G-2")
record("G-3")
record("G-4")
record("G-5")





