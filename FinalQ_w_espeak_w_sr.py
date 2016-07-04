import wx
import wolframalpha
import wikipedia
from espeak import espeak
import speech_recognition as sr

espeak.synth("Welcome Akki")
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450, 100), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.Statictext(panel, label= "Hello I am PyDa the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0,wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self,event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r= sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print "Google Speech Recognition could not understank what you said"
            except sr.RequestError as e:
                print "Could not request results from google speech recognition service; {0}".format(e)
        else:
            try:
                app_id = "YHUEYQ-AE59WVTVEG"
                client = wolframalpha.Client(app_id)
                res = client.query(input )
                answer = next(res.results).text
                print answer
                espeak.synth("The answer is "+answer)
            except:
                #Wikipedia is not compatable with espeak, so we can't make the wiki part of the code to speak.
                input = input.split(" ")
                input = " ".join(input[2:])
                #So instead of making our application speak the result that wiki gives, we will make it speak out the question :)
                espeak.synth("Searched for "+ input)
                print wikipedia.summary(input)


if __name__ == "__main__":
    app=wx.App(True)
    frame = MyFrame()
    app.MainLoop()
    
