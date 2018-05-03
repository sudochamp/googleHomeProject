import pyaudio
import wave
import aiy.voicehat
import testModel

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

status_ui = aiy.voicehat.get_status_ui()
status_ui.status('starting')
while True:
    try:
        status_ui.status('ready')
        print("Ready...")
        button = aiy.voicehat.get_button()
        button.wait_for_press()
        status_ui.status('listening')
        newCommand = "newCommand"
        record("newCommand")

        testModel.findWinner("sampleData/newCommand.wav")
    except Exception as e:
        print("Oops an exception occurred")
        print(e)
