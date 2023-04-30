import sounddevice as sd
import wavio as wv


def record_function(filename, record_time):
    fs = 44100  # Sample rate
    seconds = record_time  # Duration of recording

    print("Start Rec ...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished

    # Convert the NumPy array to audio file
    wv.write(filename, myrecording, fs, sampwidth=2)
    print("End Rec ...")
