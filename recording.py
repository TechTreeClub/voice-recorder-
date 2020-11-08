import sounddevice
from scipy.io.wavfile import write

#sample_rate
fs = 44100 
#enter your required time..
second = int(input("Enter the time duration in second: ")) 
print("Recording....\n")
record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished...\nPlease Check it...")
