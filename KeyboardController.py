from VoiceController import VoiceController as vc       # Self made module placed in same directory
import keyboard                                         # pip install keyboard
import os                                               # usually comes by default

class KeyboardController():
    '''
    Author : Armaan Agrawal, Aayush Agrawal
    Email : armngrwl1299@gmail.com, aayush2095@gmail.com

    Description : 
    This class contains keyboard shortcuts to perform various action in Windows OS.
    Inner class binds similar type of hotkey combinations.
    '''


    class windows_x_hotkeys():
        '''
        Description :
        This class contains all (windows + x) hotkey combination
        '''
        def template(self, key, message):
            '''
            Basic Template (to avoid code repetition of code)
            Parameters : 
            a) key = key(s) being pressed after (windows + x) i.e. (windows + x) then (key(s))
            b) message = action being performed
                -> used by Voice Assistant to speak messages accordingly
            '''
            # Pressing (windows + x) keys
            keyboard.send("windows + x", do_press=True, do_release=True)
            try:
                # Checking if (Windows + x) are released or not
                if not keyboard.is_pressed("windows + x"):
                    print(message)              # Printing the action being performed
                    vc().outputAudio(message)   # Speaking the action being performed
                    keyboard.send(key, do_press=True, do_release=True)  # Pressing key(s) to perform actions accordingly
            except:
                # Faced some issue while performing action
                print('faced some issue while ' + message)              # Printing Failure message
                vc().outputAudio('faced some issue while ' + message)   # Speaking Failure message

        def template2(self, key, message):
            '''
            Basic Template (to avoid code repetition of code)
            Parameters : 
            a) key = key(s) being pressed after (windows + x) then (u) i.e. (windows + x) then (u) then (key(s))
            b) message = action being performed
                -> used by Voice Assistant to speak messages accordingly
            '''
            # Pressing (windows + x) keys
            keyboard.send("windows + x", do_press=True, do_release=True)
            try:
                # Checking if (Windows + x) are released or not
                if not keyboard.is_pressed("windows + x"):
                    print(message)              # Printing the action being performed
                    vc().outputAudio(message)   # Speaking the action being performed
                    # Pressing (u) key
                    keyboard.send("u", do_press=True, do_release=True)
                    # Checking if (u) is released or not
                    if not keyboard.is_pressed("u"):
                        keyboard.send(key, do_press=True, do_release=True)  # Pressing key(s) to perform actions accordingly
            except:
                print('faced some issue while ' + message)              # Printing Failure message
                vc().outputAudio('faced some issue while ' + message)   # Speaking Failure message

        
        def appsAndFeatures(self):
            # Apps and Feature
            # Hotkey = (windows + x) then f
            self.template('f','opening apps and features')

        def mobilityCenter(self):
            # Mobility Center
            # Hotkey = (windows + x) then b
            self.template('b','opening mobility center')

        def powerOptions(self):
            # Power Options
            # Hotkey = (windows + x) then o
            self.template('o','opening power options')

        def eventViewer(self):
            # Eveny Viewer
            # Hotkey = (windows + x) then v
            self.template('v','opening event viewer')
        
        def system(self):
            # System
            # Hotkey = (windows + x) then y
            self.template('y','opening system')

        def deviceManager(self):
            # Device Manager
            # Hotkey = (windows + x) then m
            self.template('m','opening device manager')

        def networkConnections(self):
            # Network Connections
            # Hotkey = (windows + x) then w
            self.template('w','opening network connections')

        def diskManagement(self):
            # Disk Management
            # Hotkey = (windows + x) then k
            self.template('k','opening disk management')

        def computerManagement(self):
            # Computer Management
            # Hotkey = (windows + x) then g
            self.template('g','opening computer management')
        
        def commandPrompt(self):
            # Command Prompt
            # Hotkey = (windows + x) then c
            self.template('c','opening command prompt')
        
        def commandPromptAdmin(self):
            # Command Prompt
            # Hotkey = (windows + x) then a
            self.template('a','opening command prompt as administrator')
        
        def taskManager(self):
            # Task Manager
            # Hotkey = (windows + x) then t
            self.template('t','opening task manager')
        
        def settings(self):
            # Settings
            # Hotkey = (windows + x) then n
            self.template('n','opening settings')
        
        def fileExplorer(self):
            # File Explorer
            # Hotkey = (windows + x) then e
            self.template('e','opening file explorer')
        
        def windowsSearch(self):
            # Windows Search
            # Hotkey = (windows + x) then s
            self.template('s','opening windows search')
        
        def run(self):
            # Run Prompt
            # Hotkey = (windows + x) then r
            self.template('r','opening run prompt')
        
        def desktop(self):
            # Desktop
            # Hotkey = (windows + x) then d
            self.template('d','switching to desktop')
        
        def shutDown(self):
            # Shutdown
            # Hotkey = (windows + x) then u
            self.template2('u','shutting down your system')
        
        def restart(self):
            # Restart / Reboot
            # Hotkey = (windows + x) then r
            self.template2('r','rebooting your system')
        
        def signout(self):
            # Signout
            # Hotkey = (windows + x) then i
            self.template2('i','signing you out')
        
        def sleep(self):
            # Sleep
            # Hotkey = (windows + x) then s
            self.template2('s','turning device to sleeping mode')

    
    class windows_hotkeys():
        '''
        Description :
        This class contains all (windows) hotkey combination
        '''
        def template(self, key, message):
            '''
            Basic Template (to avoid code repetition of code)
            Parameters : 
            a) key = key(s) being pressed after (windows) i.e. (windows) then (key(s))
            b) message = action being performed
                -> used by Voice Assistant to speak messages accordingly
            '''
            try:
                print(message)              # Printing the action being performed
                vc().outputAudio(message)   # Speaking the action being performed
                # Pressing (windows + (key)) keys
                keyboard.send("windows + " + key, do_press=True, do_release=True)
            except:
                print('faced some issue while ' + message)              # Printing Failure message
                vc().outputAudio('faced some issue while ' + message)   # Speaking Failure message

        def run(self):
            # Run Prompt
            # Hotkey = (windows + r)
            self.template('r','opening run prompt')
        
        def fileExplorer(self):
            # File Explorer
            # Hotkey = (windows + e)
            self.template('e','opening file explorer')

        def maximize(self):
            # Maximizing Window
            # Hotkey = (windows + up)
            self.template('up','maximizing active window')

        def minimize(self):
            # Minimizing Window
            # Hotkey = (windows + down)
            self.template('down','minimizing active window')

        def shiftWindowLeft(self):
            # Shifting active window towards left
            # Hotkey = (windows + left)
            self.template('left','shifting active window towards left')

        def shiftWindowRight(self):
            # Shifting active window towards right
            # Hotkey = (windows + right)
            self.template('right','shifting active window towards right')

        def desktop(self):
            # Desktop
            # Hotkey = (windows + d)
            self.template('d','switching to desktop')

        def minimizeAllWindows(self):
            # Minimizing all windows
            # Hotkey = (windows + m)
            self.template('m','minimizing all windows')

        def maximizeAllWindows(self):
            # Maximizing all windows
            # Hotkey = (windows + shift + m)
            self.template('shift + m','maximizing all windows')

        def systemProperties(self):
            # System Properties
            # Hotkey = (windows + break)
            self.template('break','displaying system properties')

        def windowsHelpAndSupport(self):
            # Windows Help and Support
            # Hotkey = (windows + f1)
            self.template('f1','showing results for windows help and support')

        def taskView(self):
            # Task View (Currently running applications)
            # Hotkey = (windows + tab)
            self.template('tab','displaying running applications')

        def screenshot(self):
            # Screenshot
            # Hotkey = (windows + prtscn)
            self.template('prtscn','capturing screen')

        def windowsSearch(self):
            # Windows Search
            # Hotkey = (windows + s)
            self.template('s','taking to windows search')

        def lockScreen(self):
            # Lock Screen
            # Hotkey = (windows + l)
            self.template('l','locking screen')

        def snippingTool(self):
            # Snipping Tool
            # Hotkey = (windows + shift + s)
            self.template('shift + s','opening snipping tool')


    class BasicCommands():
        '''
        Description :
        This class contains all hotkey combination of basic commands
        '''
        def template(self, key, success_mssg, failure_mssg):
            '''
            Basic Template (to avoid code repetition of code)
            Parameters : 
            a) key = keys combination being pressed
            b) success_mssg = message on successful completion of action
                -> used by Voice Assistant to speak messages accordingly
            c) failure_mssg = message on failure of action
                -> used by Voice Assistant to speak messages accordingly
            '''
            try:
                print(success_mssg)             # Printing the action being performed
                vc().outputAudio(success_mssg)  # Speaking the action being performed
                # Pressing relevant keys
                keyboard.send(key, do_press=True, do_release=True)
            except:
                print(failure_mssg)             # Printing Failure message
                vc().outputAudio(failure_mssg)  # Speaking Failure message

        def template2(self, key1, key2, success_mssg, failure_mssg):
            '''
            Basic Template (to avoid code repetition of code)
            Parameters : 
            a) key1 = key(s) being pressed
            b) key2 = key(s) being pressed after realeasing (key1)
            c) success_mssg = message on successful completion of action
                -> used by Voice Assistant to speak messages accordingly
            d) failure_mssg = message on failure of action
                -> used by Voice Assistant to speak messages accordingly
            '''
            # Pressing (key1) keys
            keyboard.send(key1, do_press=True, do_release=True)
            try:
                # Checking if (key1) key(s) are released or not
                if not keyboard.is_pressed(key1):
                    # Pressing (key2) key(s)
                    keyboard.send(key2, do_press=True, do_release=True)
                    print(success_mssg)             # Printing the action being performed
                    vc().outputAudio(success_mssg)  # Speaking the action being performed
            except:
                print(failure_mssg)                 # Printing Failure message
                vc().outputAudio(failure_mssg)      # Speaking Failure message

        def cut(self):
            # Cut
            # Hotkey = (ctrl + x)
            self.template('ctrl + x','item ready to move','faced some issue while moving')

        def copy(self):
            # Copy
            # Hotkey = (ctrl + c)
            self.template('ctrl + c','item copied','faced some issue while copying')

        def paste(self):
            # Paste
            # Hotkey = (ctrl + v)
            self.template('ctrl + v','item pasted','faced some issue while pasting')

        def selectAll(self):
            # Select all
            # Hotkey = (ctrl + a)
            self.template('ctrl + a','selected','faced some issue while selecting')

        def save(self):
            # Save
            # Hotkey = (ctrl + s)
            self.template('ctrl + s','saving file','faced some issue while saving file')

        def printCmd(self):
            # Print
            # Hotkey = (ctrl + p)
            self.template('ctrl + p','opening print dialog box','faced some issue while printing')

        def delete(self):
            # Delete key
            # Hotkey = (del)
            self.template('del','item deleted','faced some issue while deletion')

        def deletePermanently(self):
            # Delete Permanently
            # Hotkey = (shift + del)
            self.template('shift + del','item deleted permanently','faced some issue while deletion')

        def enter(self, output_text):
            # Enter key
            # Hotkey = (enter)
            self.template('enter',output_text,'faced some issue')

        def closeWindow(self):
            # Close Active Window
            # Hotkey = (alt + f4)
            self.template('alt + f4','active window closed','faced some issue while closing active window')

        def up(self):
            # Up Arrow key
            # Hotkey = (up)
            self.template('up','navigated upward','faced some issue while navigating upward')

        def down(self):
            # Down Arrow key
            # Hotkey = (down)
            self.template('down','navigated downward','faced some issue while navigating downward')

        def left(self):
            # Left Arrow key
            # Hotkey = (left)
            self.template('left','navigated towards left','faced some issue while navigating towards left')

        def right(self):
            # Right Arrow key
            # Hotkey = (right)
            self.template('right','navigated towards right','faced some issue while navigating towards right')

        def pageUp(self):
            # Page Up Arrow key
            # Hotkey = (pageup)
            self.template('pageup','moved upward','faced some issue while moving upward')

        def pageDown(self):
            # Page Down Arrow key
            # Hotkey = (pagedown)
            self.template('pagedown','moved downward','faced some issue while moving downward')

        def pageTabUp(self):
            # Previous Tab
            # Hotkey = (ctrl + pageup)
            self.template('ctrl + pageup','switiched to previous tab','faced some issue while switiching to previous tab')

        def pageTabDown(self):
            # Next Tab
            # Hotkey = (ctrl + pagedown)
            self.template('ctrl + pagedown','switiched to next tab','faced some issue while switiching to next tab')

        def refresh(self):
            # Refresh
            # Hotkey = (f5)
            self.template('f5','refreshed','faced some issue while refreshing')
        
        def capsLock(self):
            # Capslock key
            # Hotkey = (capslock)
            self.template('capslock','font case toggeled','faced some issue while toggeling font case')

        def home(self):
            # Home key
            # Hotkey = (home)
            self.template('home','reached to home','faced some issue while reaching home')

        def end(self):
            # End key
            # Hotkey = (end)
            self.template('end','reached to end','faced some issue while reaching end')

        def esc(self):
            # Esc key
            # Hotkey = (esc)
            self.template('esc','exit full screen','faced some issue while exiting full screen')

        def selectLine(self):
            # Select Line
            # Hotkey = (end) then (shift + home)
            self.template2('end','shift + home','current line selected','faced some issue while selecting current line')

        def typeText(self, content):
            # Typing the string in 'content'
            keyboard.write(content)