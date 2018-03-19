import pyaudio
import wave


p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)

print ("Recording...")

frames = []

for i in range(0, int(44100/1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

print("Done Recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("output.wav", 'wb')
wf.setnchannels(2)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()