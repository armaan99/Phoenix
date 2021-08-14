from VoiceController import VoiceController as vc       # Self made module placed in same directory
import screen_brightness_control as sbc                 # pip install screen-brightness-control
import subprocess                                       # pip install subprocess.run
import os                                               # usually comes by default

class SystemAppManager():
    '''
    Author : Armaan Agrawal, Aayush Agrawal
    Email : armngrwl1299@gmail.com, aayush2095@gmail.com

    Description : 
    This class provides link to most frequently used desktop(Windows) application.
    '''

    def calculator(self):
        # Calculator
        vc().outputAudio("Opening Calculator")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    def notepad(self):
        # Notepad
        vc().outputAudio("Opening Notepad")
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    def wordpad(self):
        # Wordpad
        vc().outputAudio("Opening Wordpad")
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        #os.system('start write') -> Alternate Solution (has longer execution time)

    def controlPanel(self):
        # Control Panel
        vc().outputAudio("Opening Control Panel")
        subprocess.Popen('C:\\Windows\\System32\\control.exe')
        #os.system('start control') -> Alternate Solution (has longer execution time)

    def camera(self):
        # Webcam
        vc().outputAudio("Opening Camera")
        subprocess.run('start microsoft.windows.camera:', shell=True)

    def commandPrompt(self):
        # Command Prompt
        vc().outputAudio("Opening Command Prompt")
        os.system('start cmd')

    def bluetooth(self):
        # Bluetooth
        vc().outputAudio("Opening Bluetooth Panel")
        os.system('start fsquirt')

    def magnify(self):
        # Magnify
        vc().outputAudio("Magnifying screen")
        os.system('start magnify')

    def systemInfo(self):
        # System Info
        vc().outputAudio("Displaying your System's information")
        os.system('start msinfo32')

    def paint(self):
        # Microsoft Paint
        vc().outputAudio("Microsoft Paint")
        os.system('start mspaint')

    def remoteAssistance(self):
        # Windows' Remote Assistance
        vc().outputAudio("Opening Windows Remote Assistance")
        os.system('start msra')

    def taskManager(self):
        # Task Manager
        vc().outputAudio("Opening Task Manager")
        os.system('start taskmgr')

    def userAccountControlSettings(self):
        # Windows' User Account Control Settings
        vc().outputAudio("Opening User Account Control Settings")
        os.system('start useraccountcontrolsettings')

    def increaseBrightness(self):
        # Increasing Brightness of screen
        try:
            sbc.set_brightness('+30')
            vc().outputAudio("Brightness increased")
        except:
            vc().outputAudio("Brightness is already at its maximum level")

    def decreaseBrightness(self):
        # Decreasing Brightness of screen
        try:
            sbc.set_brightness('-30')
            vc().outputAudio("Brightness decreased")
        except:
            vc().outputAudio("Brightness is already at its minimum level")

    def increaseVolume(self):
        # Increasing Media Volume
        pass

    def decreaseVolume(self):
        # Decreasing Media Volume
        pass

    def mute(self):
        # Mute Volume
        pass

    def unmute(self):
        # Unmute Volume
        pass