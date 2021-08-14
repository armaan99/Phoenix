import pyttsx3                          # pip install pyttsx3
from pyttsx3.drivers import sapi5
import speech_recognition as sr         # pip install SpeechRecognition
import os                               # usually comes by default
from gtts import gTTS                   # pip install gtts
import keyboard                         # pip install keyboard
import time                             # usually comes by default

class VoiceController():
    '''
    Author : Armaan Agrawal, Aayush Agrawal
    Email : armngrwl1299@gmail.com, aayush2095@gmail.com

    Description : 
    This class is used to deal with speech recognition (voice <-> text).
    '''

    def outputAudio(self, output_text):
        '''
        Managing all output as Audio

        Parameters :
        a) output_text = text that is to be converted into voice.
            -> used by Voice Assistant to speak messages accordingly
        '''

        # pyttsx3 -> Text to speach conversion library. It works offline.
        
        # pyttsx3.init() -> takes argument as voice angine and creates an engine object reference
        # In case of Microsoft Windows, available option is 'sapi5'
        # Alternate options are : 'nsss' or 'espeak'
        engine = pyttsx3.init("sapi5")
        
        # get properties of voices of selected voice engine
        voices = engine.getProperty("voices")

        # selecting / changing default properties of voice engine
        engine.setProperty("voice",voices[1].id)
        engine.setProperty("volume",1.0)
        engine.setProperty("rate",200)

        # giving audio as output
        engine.say(output_text)
        # blocks while processing all currently queued commands
        engine.runAndWait()


    def inputAudio(self):
        '''
        Managing all input as Audio
        '''

        # speech_recognition -> Library for performing speech recognition with support for several engines and APIs, online and offline
        
        # speech_recognition.Recognizer() -> To recognize speech
        # instance creation of Recognizer class
        speech_recognizer = sr.Recognizer()
        
        # speech_recognition.Microphone() To access the default system microphone
        with sr.Microphone() as microphone:
            # Taking input as Audio
            input_audio = speech_recognizer.listen(microphone)

            try:
                # Recognize what user said and converting audio into text
                audio_to_text = speech_recognizer.recognize_google(input_audio)
                audio_to_text = audio_to_text.lower()   # converting all the string to lower case
                print(audio_to_text)    # printing text form of input audio
                return audio_to_text    # returning text form of input audio
            except:
                # Unable to recognize what user said
                self.outputAudio("Sorry! unable to recognize")
                self.outputAudio("Please say again")
                return "Sorry! unable to recognize"


    def googleSpeak(self, translatedText, out_lang):
        '''
        Managing all output as Audio in different languages

        Parameters :
        a) translatedText = text(can be in various language) that is to be converted into voice.
            -> used by Voice Assistant to speak messages accordingly
        b) out_lang = language in which output is to be given
        '''

        # gTTS -> Google Text to Speech
            # A Python library and CLI tool to interface with Google Translate's text-to-speech API.
            # # Writes spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout 
        speak = gTTS(text=translatedText, lang=out_lang, slow= False)
        # Saving mp3 data to file
        speak.save("translated_voice.mp3")
        # Opening that mp3 file
        os.system("start translated_voice.mp3")
        # Waiting some time to listen to audio before closing media player
        time.sleep(7)
        # Closing Media Player
        keyboard.send("alt + f4", do_press=True , do_release=True)