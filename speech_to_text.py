import speech_recognition as sr


def start_speech_recognition(filename):
    # create a recognizer object
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language='de-DE')
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    exit()
