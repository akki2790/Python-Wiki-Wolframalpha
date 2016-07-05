import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    self.txt.SetValue(r.recognize_google(audio))
except sr.UnknownValueError:
    print ("Google Speech Recognition could not understank what you said")
except sr.RequestError as e:
    print ("Could not request results from google speech recognition service; {0}".format(e))
    
