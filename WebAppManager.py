from VoiceController import VoiceController as vc       # Self made module placed in same directory
from youtube_search import YoutubeSearch                # pip install youtube-search
import webbrowser                                       # pip install pycopy-webbrowser

class WebAppManager():
    '''
    Author : Armaan Agrawal, Aayush Agrawal
    Email : armngrwl1299@gmail.com, aayush2095@gmail.com

    Description : 
    This class provides link to most frequently searched web application.
    Inner class binds similar niche of web application.
    '''

    def template(self, url, application_name):
        '''
        Basic Template (to avoid code repetition of code)
        Parameters : 
        a) url = URL of web application
            -> To open website
        b) application_name = name of web application
            -> used by Voice Assistant to speak messages accordingly
        '''

        browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        # Path of web browser(Google Chrome)
        try:
            vc().outputAudio("Opening " + application_name)
            # Success output audio
            webbrowser.get(browser_path).open(url)
            # Opening website
        except:
            vc().outputAudio("Faced some issue while opening " + application_name)
            # Failure output audio


    class SocialMedia():
        '''
        Description :
        This class provides link to most frequently searched social media websites.
        '''
        def instagram(self):
            # Instagram
            WebAppManager().template("www.instagram.com", "Instaa gram")

        def whatsapp(self):
            # Whatsapp
            WebAppManager().template("web.whatsapp.com", "Whatsapp Web")

        def facebook(self):
            # Facebook
            WebAppManager().template("www.facebook.com", "Facebook")

        def twitter(self):
            # Twitter
            WebAppManager().template("www.twitter.com", "Twitter")

        def LinkedIn(self):
            # Linkedin
            WebAppManager().template("www.linkedin.com", "Linked In")

        def Skype(self):
            # Skype
            WebAppManager().template("www.skype.com", "Skype")

    
    class Entertainment():
        '''
        Description :
        This class provides link to most frequently searched OTT Platforms.
        '''
        def amazonPrime(self):
            # Amazon Prime Video
            WebAppManager().template("www.primevideo.com", "Amazon Prime")

        def netflix(self):
            # Netfix
            WebAppManager().template("www.netflix.com", "NetFlix")

        def hotstar(self):
            # Disney + Hotstar
            WebAppManager().template("www.hotstar.com", "Disney plus Hotstar")

    
    class Payment():
        '''
        Description :
        This class provides link to most frequently searched UPI Platforms.
        '''
        def paytm(self):
            # Paytm
            WebAppManager().template("www.paytm.com", "Pay T M")

    
    class GoogleServices():
        '''
        Description :
        This class provides link to most frequently searched Google Services.
        '''
        def googleSearch(self):
            # Google Search Engine
            WebAppManager().template("www.google.com", "Google Search")

        def youtube(self):
            # Youtube
            WebAppManager().template("www.youtube.com", "Youtube")

        def youtubeVideo(self, searchQuery):
            # Randomly searched Videos on Youtube
            WebAppManager().template("www.youtube.com" + YoutubeSearch(searchQuery, max_results=1).to_dict()[0]["url_suffix"], "video on Youtube")

        def gmail(self):
            # Gmail
            WebAppManager().template("mail.google.com", "G-mail")

        def googleDrive(self):
            # Google Drive
            WebAppManager().template("drive.google.com", "Google Drive")

        def googleMeet(self):
            # Google Meet
            WebAppManager().template("meet.google.com", "Google Meet")

        def googleTranslate(self):
            # Google Translate
            WebAppManager().template("translate.google.com", "Google Translate")

        def googlePhotos(self):
            # Google Photos
            WebAppManager().template("photos.google.com", "Google Photos")

        def googleDocs(self):
            # Google Docs
            WebAppManager().template("docs.google.com", "Google Docs")

        def googleSheets(self):
            # Google Sheets
            WebAppManager().template("sheets.google.com", "Google Sheets")

        def googleSlides(self):
            # Google Slides
            WebAppManager().template("slides.google.com", "Google Slides")

        def googleKeep(self):
            # Google Keep
            WebAppManager().template("keep.google.com", "Google Keep")

        def googleForms(self):
            # Google Forms
            WebAppManager().template("forms.google.com", "Google Forms")


    class EShopping():
        '''
        Description :
        This class provides link to most frequently searched Online Shopping websites.
        '''
        def amazon(self):
            # Amazon India
            WebAppManager().template("www.amazon.in", "Amazon India")

        def flipkart(self):
            # Flipkart
            WebAppManager().template("www.flipkart.com", "Flipkart")

        def myntra(self):
            # Myntra
            WebAppManager().template("www.myntra.com", "Myntra")

        def limeroad(self):
            # Limeroad
            WebAppManager().template("www.limeroad.com", "Limeroad")

        def ajio(self):
            # Ajio
            WebAppManager().template("www.ajio.com", "ajio")


    class TravellingAndHospitality():
        '''
        Description :
        This class provides link to most frequently searched Travelling and Hopitality related websites.
        '''
        def irctc(self):
            # I.R.C.T.C. (Indian Railways Catering and Tourism Corporation)
            WebAppManager().template("www.irctc.co.in", "I.R.C.T.C.")

        def trivago(self):
            # Trivago
            WebAppManager().template("www.trivago.in", "Trevaaago")

    
    class EdTech():
        '''
        Description :
        This class provides link to most frequently searched Educational Platforms.
        '''
        def unacademy(self):
            # Unacademy
            WebAppManager().template("www.unacademy.com", "Un academy")

        def byjus(self):
            # Byjus
            WebAppManager().template("www.byjus.com", "Byjoos")

        def coursera(self):
            # Coursera
            WebAppManager().template("www.coursera.org", "Course era")

        def udemy(self):
            # Udemy
            WebAppManager().template("www.udemy.com", "U day me")

        def geeksForGeeks(self):
            # Geeks for Geeks
            WebAppManager().template("www.geeksforgeeks.org", "Geeks for Geeks")

        def javaTPoint(self):
            # JavaTpoint
            WebAppManager().template("www.javatpoint.com", "Java T Point")

        def tutorialsPoint(self):
            # Tutorials Point
            WebAppManager().template("www.tutorialspoint.com", "Tutorials Point")

        def github(self):
            # Github
            WebAppManager().template("www.github.com", "Gitt hub")

    
    class FreeLancing():
        '''
        Description :
        This class provides link to most frequently searched freelancing and internship related websites.
        '''
        def freelancer(self):
            # Freelancer
            WebAppManager().template("www.freelancer.com", "Free Lancer")            

        def upwork(self):
            # Upwork
            WebAppManager().template("www.upwork.com", "Upwork")

        def fiverr(self):
            # Fiverr
            WebAppManager().template("www.fiverr.com", "Fiverr")

        def internshala(self):
            # Internshala
            WebAppManager().template("www.internshala.com", "Intern shaaala")

    
    class CloudServices():
        '''
        Description :
        This class provides link to most frequently searched Cloud Service Providers.
        '''
        def aws(self):
            # Amazon Web Services
            WebAppManager().template("aws.amazon.com", "Amazon Web Services")

        def azure(self):
            # Microsoft Azure
            WebAppManager().template("azure.microsoft.com", "Microsoft Azure")

        def ibmCloud(self):
            # IBM Cloud
            WebAppManager().template("cloud.ibm.com", "I.B.M. cloud")

        def firebase(self):
            # Google Firebase
            WebAppManager().template("firebase.google.com", "Google Firebase")


    class Utilities():
        '''
        Description :
        This class provides link to basic internet utilities.
        '''
        def internetSpeedTest(self):
            # Internet Speed Testing - by Netflix 'Fast'
            WebAppManager().template('www.fast.com', 'netflix fast internet speed test')