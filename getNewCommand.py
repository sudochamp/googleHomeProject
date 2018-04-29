import pyaudio
import wave
import testModel
import os

def record(newCommand):
    FORMAT = pyaudio.paInt16
    chunk = 1024
    RATE = 44100
    frames = []
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=chunk)

    print("Recording...")

    for i in range(0, int(RATE / chunk * 3)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    print("Done Recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("sampleData/newCommand" + ".wav", 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



while True:
    try:
        print("Ready...")
        ask = raw_input("Go y/n?")
        if ask == 'y':
            newCommand = "newCommand"
            record("newCommand")
        testModel.findWinner("sampleData/newCommand.wav")
        os.remove("sampleData/newCommand.wav")
    except Exception as e:
        print("Oops an exception occurred")
        print(e)
