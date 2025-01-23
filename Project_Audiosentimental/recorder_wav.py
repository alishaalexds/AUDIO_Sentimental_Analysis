import pyaudio
import wave
import numpy as np
 
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
 
#work with one huge chunk
CHUNK = 204800
RECORD_SECONDS = 5
 
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("* recording")
def playAudio(audio, samplingRate, channels):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=samplingRate,
                    output=True)
    sound = (audio.astype(np.int16).tostring())
    stream.write(sound)
 
    stream.stop_stream()
    stream.close()
    p.terminate()
    return
 
data = stream.read(CHUNK)
data = np.fromstring(data, dtype=np.int16)
 
#make two times louder
data *= 2
 
print ("* done recording")
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
#Tests
#playAudio(data, RATE, CHANNELS)
 
#saving into file
WAVE_OUTPUT_FILENAME = 'audio.wav'
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(data))
waveFile.close()
print('WAV file was saved as', WAVE_OUTPUT_FILENAME)