import pyaudio
import wave
import aiy.voicehat
import testModel
import os 

def record(newCommand):
    FORMAT = pyaudio.paInt16 #
    chunk = 1024 #
    RATE = 44100 #Sample Rate
    frames = []
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=chunk) #Starting the recording 

    print("Recording...")

    for i in range(0, int(RATE / chunk * 3)): #Multiplying by 3 gives us 3 seconds of audio time, change that to get more seconds.
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
        os.remove("sampleData/newCommand.wav") #Deleting this file so it doesn't cause any issues down the line.
    except Exception as e:
        print("Oops an exception occurred")
        print(e)
