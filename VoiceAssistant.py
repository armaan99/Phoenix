from VoiceController import VoiceController as vc           # Self made module placed in same directory
from WebAppManager import WebAppManager as wam              # Self made module placed in same directory
from KeyboardController import KeyboardController as kc     # Self made module placed in same directory
from SystemAppManager import SystemAppManager as sam        # Self made module placed in same directory
from LanguageTranslator import LanguageTranslator as lt     # Self made module placed in same directory
from datetime import datetime as dt                         # pip install datetime
import wolframalpha                                         # pip install wolframalpha
import webbrowser                                           # pip install wabbrowser
#import tkinter as tk                                        # pip install tkintertable

class VoiceAssistant():
    '''
    Author : Armaan Agrawal, Aayush Agrawal
    Email : armngrwl1299@gmail.com, aayush2095@gmail.com

    Description :
    This class handles all the voice commands - The Voice Assistant "Phoenix"
    This class is the main class from where execution begins.
    '''

    def __init__(self):

        # Phoenix introduction
        vc().outputAudio("Hello I am Phoenix. How can I Help you?")
        while True:
            # Listening to user's command
            action = vc().inputAudio()

            # Phrases to terminate Phoenix
            if ((("thank you" in action) or ("thanks" in action)) and ("phoenix" in action)):
                vc().outputAudio("You're Welcome")  # 'Welcome' message as output audio
                break # Terminate

            # When Phoenix was unable to listen
            elif ("Sorry! unable to recognize" in action):
                continue # Back to listen to user's command

            # To wake up Phoenix Translator
            elif ((("translate" in action) or ("translation" in action)) and ("google" not in action)):
                lt() # Instantiating Language Translator (and working through contructor call)
                
                # Asking for any other commands after translation is done (if any)
                vc().outputAudio("Anything else, I can do for you?")
                continue # Back to listen to user's command
            
            # Perform action as per user's command
            else:
                self.performAction(action)

    def performAction(self, action):
        '''
        Managing all user's command

        Parameters :
        a) action = user's command in text form
            -> used by Voice Assistant to call methods accordingly
        '''

        # Youtube
        if (("youtube" in action) or ("you tube" in action)):
            wam().GoogleServices().youtube()

        # Randomly video on youtube
        elif "play" and "song" in action:
            wam().GoogleServices().youtubeVideo(action)

        # Whatsapp Web
        elif ("whatsapp" in action) or ("whats app" in action) or ("what's up" in action):
            wam().SocialMedia().whatsapp()
        
        # Facebook
        elif (("facebook" in action) or ("fb" in action) or ("f b" in action)):
            wam().SocialMedia().facebook()

        # Instagram
        elif ("insta" in action): # 'instagram' already has 'insta'
            wam().SocialMedia().instagram()

        # Flipkart
        elif ("flipkart" in action) or ("flip kart" in action):
            wam().EShopping().flipkart()

        # Gmail
        elif (("gmail" in action) or ("g mail" in action)):
            wam().GoogleServices().gmail()

        # Amazon services
        elif ("amazon" in action):
            # Amazon Prime Video
            if ("prime" in action):
                wam().Entertainment().amazonPrime()

            # Amazon Web Services
            elif (("web service" in action) or ("cloud" in action) or ("aws" in action) or ("a w s" in action)):
                wam().CloudServices().aws()

            # Amazon India
            else:
                wam().EShopping().amazon()

        # Disney + Hotstar
        elif (("hotstar" in action) or ("hot star" in action)):
            wam().Entertainment().hotstar()

        # Internet Speed Test
        elif (("internet" in action) and ("speed" in action)):
            wam().Utilities().internetSpeedTest()

        # Desktop
        elif ("desktop" in action):
            kc().windows_hotkeys().desktop()

        # File Explorer / This PC
        elif (("file explorer" in action) or ("my computer" in action) or ("this pc" in action)):
            kc().windows_hotkeys().fileExplorer()

        # Windows search
        elif (("windows" in action) and ("search" in action)):
            kc().windows_hotkeys().windowsSearch()

        # Task view / Currently running applications
        elif (((("recent" in action) or ("current" in action)) and (("apps" in action) or ("tabs" in action))) or ("task view" in action)):
            kc().windows_hotkeys().taskView()

        # Screenshot
        elif (("screenshot" in action) or ("snapshot" in action) or ("snap" in action)):
            kc().windows_hotkeys().screenshot()

        # Snipping Tool
        elif ("snipping tool" in action):
            kc().windows_hotkeys().snippingTool()

        # For typing
        elif ("type" in action):
            kc().BasicCommands().typeText(action[4:])

        # Enter key functionalities
        elif (("enter" in action) or ("open it" in action) or ("open this" in action) or ((("change" in action) or ("next" in action)) and ("line" in action))):
            # To press Enter key
            if ("enter" in action):
                kc().BasicCommands().enter("okay")

            # To open any folder/file/application or any other thing
            elif (("open it" in action) or ("open this" in action)):
                kc().BasicCommands().enter("opening it")

            # To change line in text editors(or something else)
            elif ((("change" in action) or ("next" in action)) and ("line" in action)):
                kc().BasicCommands().enter("line changed")

        # To close active window
        elif ("close" in action):
            kc().BasicCommands().closeWindow()

        # I.R.C.T.C
        elif (("irctc" in action) or ("i r c t c" in action) or ("railways" in action)):
            wam().TravellingAndHospitality().irctc()

        # Twitter
        elif ("twitter" in action):
            wam().SocialMedia().twitter()

        # Myntra
        elif ("myntra" in action) or ("mintra" in action):
            wam().EShopping().myntra()

        # Linkedin
        elif (("linkedin" in action) or ("linked in" in action)):
            wam().SocialMedia().LinkedIn()

        # Netflix
        elif (("netflix" in action) or ("net flix" in action)):
            wam().Entertainment().netflix()

        # Paytm
        elif (("paytm" in action) or ("pay tm" in action) or ("pay t m" in action)):
            wam().Payment().paytm()
        
        # Google services
        elif ("google" in action):
            # Google search
            if ("search" in action):
                wam().GoogleServices().googleSearch()

            # Google translate
            elif ("translate" in action):
                wam().GoogleServices().googleTranslate()

            # Google drive
            elif ("drive" in action):
                wam().GoogleServices().googleDrive()

            # Google photos
            elif ("photos" in action):
                wam().GoogleServices().googlePhotos()

            # Google forms
            elif ("form" in action): # 'forms' already has 'form'
                wam().GoogleServices().googleForms()

            # Google meet
            elif ("meet" in action):
                wam().GoogleServices().googleMeet()

            # Google docs
            elif ("doc" in action): # 'docs' already has 'doc'
                wam().GoogleServices().googleDocs()

            # Google sheets
            elif ("sheet" in action): # 'sheets' already has 'sheet'
                wam().GoogleServices().googleSheets()

            # Google slides
            elif ("slide" in action): # 'slides' already has 'slide'
                wam().GoogleServices().googleSlides()

            # Google firebase (cloud services)
            elif ("firebase" in action) or ("fire base" in action):
                wam().CloudServices().firebase()

            # Google keep (notes)
            elif (("keep" in action) or ("note" in action)): # 'notes' already has 'note'
                wam().GoogleServices().googleKeep()

        # Managing Volume
        elif ("volume" in action):
            # Increasing volume
            if (("increase" in action) or ("up" in action)):
                sam().increaseVolume()

            # Decreasing volume
            elif (("decrease" in action) or ("down" in action)):
                sam().decreaseVolume()

        # Mute and Unmute
        elif ("mute" in action):
            # Unmute
            if ("unmute" in action):
                sam().unmute()

            # Mute
            else:
                sam().mute()

        # Managing Brightness
        elif ("brightness" in action):
            # increasing brightness
            if (("increase" in action) or ("up" in action)):
                sam().increaseBrightness()

            # decreasing brightness
            elif (("decrease" in action) or ("down" in action)):
                sam().decreaseBrightness()

        # managing pointer/cursor movement/navigation
        elif ("move" in action):
            # in upward direction
            if ("up" in action):
                kc().BasicCommands().up()

            # in downward direction
            elif ("down" in action):
                kc().BasicCommands().down()

            # towards left
            elif ("left" in action):
                kc().BasicCommands().left()

            # towards right
            elif ("right" in action):
                kc().BasicCommands().right()

        # Saving file
        elif ("save" in action):
            kc().BasicCommands().save()

        # Deletion
        elif ("delete" in action):
            # Parmanent Deletion
            if (("permanent" in action) or ("permanently" in action)):
                kc().BasicCommands().deletePermanently()
            
            # Deletion
            else:
                kc().BasicCommands().delete()

        # Cut
        elif ("cut" in action):
            kc().BasicCommands().cut()
        
        # Copy
        elif ("copy" in action):
            kc().BasicCommands().copy()

        # Paste
        elif ("paste" in action):
            kc().BasicCommands().paste()

        # Selection
        elif ("select" in action):
            # Select all
            if ("all" in action):
                kc().BasicCommands().selectAll()

            # Select one line
            elif ("line" in action):
                kc().BasicCommands().selectLine()

        # Refresh
        elif ("refresh" in action):
            kc().BasicCommands().refresh()

        # Window minimization/maximization
        elif (("imize" in action) or ("imise" in action)):
            # Maximizing all windows
            if ((("maximize" in action) or ("maximise" in action)) and ("all" in action)):
                kc().windows_hotkeys().maximizeAllWindows()

            # Maximizing active window
            elif (("maximize" in action) or ("maximise" in action)):
                kc().windows_hotkeys().maximize()

            # Minimizing all windows
            elif ((("minimize" in action) or ("minimise" in action)) and ("all" in action)):
                kc().windows_hotkeys().minimizeAllWindows()

            # Minimizing active window
            elif (("minimize" in action) or ("minimise" in action)):
                kc().windows_hotkeys().minimize()

        # Shutdown
        elif (("shut down" in action) or ("shutdown" in action)):
            kc().windows_x_hotkeys().shutDown()

        # Restart/Reboot
        elif (("restart" in action) or ("reboot" in action)):
            kc().windows_x_hotkeys().restart()

        # Sleep mode
        elif ("sleep" in action):
            kc().windows_x_hotkeys().sleep()

        # Notepad
        elif (("notepad" in action) or ("note pad" in action)):
            sam().notepad()

        # Control Panel
        elif ("control panel" in action):
            sam().controlPanel()

        # Udemy
        elif ("udemy" in action) or ("u demy" in action):
            wam().EdTech().udemy()

        # Coursera
        elif ("coursera" in action) or ("course era" in action):
            wam().EdTech().coursera()

        # Limeroad
        elif (("limeroad" in action) or ("lime road" in action)):
            wam().EShopping().limeroad()

        # Ajio
        elif ("ajio" in action) or ("a jio" in action):
            wam().EShopping().ajio()

        # Unacademy
        elif ("unacademy" in action) or ("un academy" in action):
            wam().EdTech().unacademy()

        # Github
        elif ("github" in action):
            wam().EdTech().github()

        # Freelancer
        elif (("free lancer" in action) or ("freelancer" in action)):
            wam().FreeLancing().freelancer()

        # Skype
        elif ("skype" in action):
            wam().SocialMedia().Skype()

        # Trivago
        elif ("trivago" in action):
            wam().TravellingAndHospitality().trivago()

        # Byjus
        elif (("byjus" in action) or ("byju's" in action)):
            wam().EdTech().byjus()

        # Internshala
        elif (("intern shala" in action) or ("internshala" in action)):
            wam().FreeLancing().internshala()

        # Geeks for Geeks
        elif (("geeksforgeeks" in action) or ("geeks for geeks" in action) or ("gfg" in action) or ("g f g" in action)):
            wam().EdTech().geeksForGeeks()

        # Javatpoint
        elif (("javatpoint" in action) or ("java t point" in action) or ("java tea point" in action)):
            wam().EdTech().javaTPoint()

        # Fiverr
        elif (("fiverr" in action) or ("fiver" in action) or ("fibre" in action) or ("fiber" in action)):
            wam().FreeLancing().fiverr()

        # Amazon Web Service
        elif (("aws" in action) or ("a w s" in action)):
            wam().CloudServices().aws()

        # Tutorialspoint
        elif (("tutorials point" in action) or ("tutorialspoint" in action) or ("tutorial point" in action) or ("tutorialpoint" in action)):
            wam().EdTech().tutorialsPoint()

        # Upwork
        elif (("up work" in action) or ("upwork" in action)):
            wam().FreeLancing().upwork()

        # Google Firebase (Cloud services)
        elif ("firebase" in action) or ("fire base" in action):
            wam().CloudServices().firebase()

        # Microsoft Azure (Cloud Services)
        elif (("azure" in action) or ("microsoft cloud" in action)):
            wam().CloudServices().azure()

        # IBM Cloud (Cloud Services)
        elif (("ibm" in action) and ("cloud" in action)):
            wam().CloudServices().ibmCloud()

        # Shifting window
        elif ((("shift" in action) or ("swipe" in action) or ("place" in action)) and ("window" in action)):
            # Shifting active window towards left
            if ("left" in action):
                kc().windows_hotkeys().shiftWindowLeft()

            # Shifting active window towards right
            elif ("right" in action):
                kc().windows_hotkeys().shiftWindowRight()

        # Print
        elif ("print" in action):
            kc().BasicCommands().printCmd()

        # Apps and Features
        elif ("apps and features" in action):
            kc().windows_x_hotkeys().appsAndFeatures()

        # Command Prompt
        elif ("command prompt" in action):
            # cmd as Admin
            if (("admin" in action) or ("administrator" in action)):
                kc().windows_x_hotkeys().commandPromptAdmin()
            
            # cmd prompt
            else:
                kc().windows_x_hotkeys().commandPrompt()
                #sam().commandPrompt()

        # Task Manager
        elif ("task manager" in action):
            kc().windows_x_hotkeys().taskManager()
            #sam().taskManager()

        # Bluetooth
        elif ("bluetooth" in action):
            sam().bluetooth()

        # Lock SCreen
        elif (("lock" in action) and ("screen" in action)):
            kc().windows_hotkeys().lockScreen()

        # Calculator
        elif ("calculator" in action):
            sam().calculator()

        # Webcam
        elif (("camera" in action) or ("web cam" in action) or ("webcam" in action)):
            sam().camera()

        # System Settings
        elif ((("settings" in action) or ("setting" in action)) and (("pc" in action) or ("system" in action) or ("device" in action))):
            kc().windows_x_hotkeys().settings()

        # Network Connections
        elif ("network connections" in action):
            kc().windows_x_hotkeys().networkConnections()

        # System power options
        elif ("power options" in action):
            kc().windows_x_hotkeys().powerOptions()

        # Microsoft Paint
        elif (("paint" in action) or ("ms paint" in action) or ("microsoft paint" in action)):
            sam().paint()

        # Navigation on page/window
        elif (("page" in action) or ("tab" in action)):
            # Previous Tab
            if ((("page" in action) and ("tab" in action) and ("up" in action)) or (("previous" in action) and ("tab" in action))):
                kc().BasicCommands().pageTabUp()

            # Page up
            elif (("page" in action) and ("up" in action)):
                kc().BasicCommands().pageUp()
        
            # Next Tab
            elif ((("page" in action) and ("tab" in action) and ("down" in action)) or (("next" in action) and ("tab" in action))):
                kc().BasicCommands().pageTabDown()

            # Page down
            elif (("page" in action) and ("down" in action)):
                kc().BasicCommands().pageDown()

        # Home key
        elif (("home" in action) or ((("start" in action) or ("starting" in action) or ("beginning" in action)) and ("line" in action))):
            kc().BasicCommands().home()

        # End key
        elif (("end" in action) or ((("end" in action) or ("ending" in action) or ("last" in action)) and ("line" in action))):
            kc().BasicCommands().end()

        # Esc key
        elif (("escape" in action) or (("exit" in action) and ("fullscreen" in action))):
            kc().BasicCommands().esc()

        # Capslock key
        elif (("caps lock" in action) or ("capslock" in action)):
            kc().BasicCommands().capsLock()

        # Run prompt
        elif ("run prompt" in action):
            kc().windows_hotkeys().run()

        # Signout
        elif ("sign out" in action):
            kc().windows_x_hotkeys().signout()

        # Time
        elif (("time" in action) and (("now" in action) or ("current" in action))):
            hour = dt().now().hour
            minute = dt().now().minute
            if hour > 12:
                hour = hour - 12
                vc().outputAudio("It's " + str(hour) + str(minute) + "pm")
            else:
                vc().outputAudio("It's " + str(hour) + str(minute) + "am")

        # Date
        elif (("date" in action) and (("today" in action) or ("today's" in action))):
            months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
            vc().outputAudio("Today is {m} {d}, {y}".format(m=months[dt().now().month], d=dt().now().day, y=dt().now().year))

        # System Information
        elif (("system" in action) and ("information" in action)):
            sam().systemInfo()

        # User account control settings
        elif ("user account control setting" in action):
            sam().userAccountControlSettings()

        # Remote ASsistance
        elif ("remote assistance" in action):
            sam().remoteAssistance()

        # System Properties
        elif (("properties" in action) and (("system" in action) or ("device" in action) or ("pc" in action))):
            kc().windows_hotkeys().systemProperties()

        # Windows Help and Support
        elif (("windows" in action) and ("help and support" in action)):
            kc().windows_hotkeys().windowsHelpAndSupport()

        # Mobility Center
        elif (("mobility centre" in action) or ("mobility center" in action)):
            kc().windows_x_hotkeys().mobilityCenter()

        # Event Viewer
        elif ("event viewer" in action):
            kc().windows_x_hotkeys().eventViewer()

        # Disk Management
        elif (("disk management" in action) or ("disc management" in action)):
            kc().windows_x_hotkeys().diskManagement()

        # Computer Management
        elif ("computer management" in action):
            kc().windows_x_hotkeys().computerManagement()

        # Wordpad
        elif ("wordpad" in action):
            sam().wordpad()

        # Magnify
        elif (("magnify" in action) or ("zoom in" in action)):
            sam().magnify()

        # to deal with actions which are not mentioned above
        else:
            try:
                # wolfromalpha, to answer basic questions, mathemetical computations or to have useless talks
                vc().outputAudio(next(wolframalpha.Client("PQ2EAG-VXGG8HH72U").query(action).results).text)
            except:
                # Google search, in case wolfromalpha could not answer
                webbrowser.open(action)


def main():
    # Object creation and instantiation
    VoiceAssistant()

main()
#root = tk.Tk()
#canvas1 = tk.Canvas(root, width = 400, height = 300)
#canvas1.pack()

#button1 = tk.Button(text='Click Me',command=main, bg='brown',fg='white')
#canvas1.create_window(200, 150, window=button1)

#root.mainloop()