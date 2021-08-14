from VoiceController import VoiceController as vc       # Self made module placed in same directory
from googletrans import Translator                      # pip install googletrans
import time                                             # usually comes by default

class LanguageTranslator():
    '''
    Author : Armaan Agrawal, Aayush Agrawal
    Email : armngrwl1299@gmail.com, aayush2095@gmail.com

    Description : 
    This class is used to translate between 50+ languages.
    '''

    # Language Codes as per Google Trans API
    language_codes = {'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy',
        'azerbaijani': 'az','basque': 'eu','belarusian': 'be','bengali': 'bn','bosnian': 'bs',
        'bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb','chichewa': 'ny','chinese (simplified)': 'zh-cn',
        'chinese (traditional)': 'zh-tw','corsican': 'co','croatian': 'hr','czech': 'cs',
        'danish': 'da','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et',
        'filipino': 'tl','finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl',
        'georgian': 'ka','german': 'de','greek': 'el','gujarati': 'gu','haitian creole': 'ht',
        'hausa': 'ha','hawaiian': 'haw','hebrew': 'iw','hindi': 'hi','hmong': 'hmn','hungarian': 'hu',
        'icelandic': 'is','igbo': 'ig','indonesian': 'id','irish': 'ga','italian': 'it',
        'japanese': 'ja','javanese': 'jw','kannada': 'kn','kazakh': 'kk','khmer': 'km','korean': 'ko',
        'kurdish (kurmanji)': 'ku','kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lithuanian': 'lt',
        'Luxembourgish': 'Lb','macedonian': 'mk','malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt',
        'maori': 'mi','marathi': 'mr','mongolian': 'mn','myanmar (burmese)': 'my','nepali': 'ne','norwegian': 'no',
        'pashto': 'ps','persian': 'fa','polish': 'pl','portuguese': 'pt','punjabi': 'pa','romanian': 'ro',
        'russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st','shona': 'sn',
        'sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so','spanish': 'es',
        'sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','telugu': 'te',
        'thai': 'th','turkish': 'tr','ukrainian': 'uk','urdu': 'ur','uzbek': 'uz','vietnamese': 'vi',
        'welsh': 'cy','xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu','Filipino': 'fil','Hebrew': 'he'}


    def __init__(self):

        loopBreaker = False     # flag variable to control iteration
        while (not loopBreaker):

            try:
                vc().outputAudio("From which language, to which language, you want to translate?")
                # input and output languages
                io_lang = vc().inputAudio()
                io_lang = io_lang.split()

                io_lang.remove("to")
                if "from" in io_lang:
                    io_lang.remove("from")

                # fetching input language and output language from single statement
                in_lang, out_lang = io_lang[0], io_lang[-1]

                # On listening properly (i.e. if not listened only one language, i.e. listened two different languages)
                if(in_lang != out_lang):

                    # Asking for translating statement
                    vc().outputAudio("Speak")
                    print("Speak...")

                    # Listening Translating statement
                    translatingText = vc().inputAudio()

                    flag = True    # flag variable which tells if it is the first statement to translate or not

                    while True:

                        if (("done with translation" in translatingText) or ("no" in translatingText)): # Finished with Translation
                            loopBreaker = True  # Breaking outer loop
                            break               # Breaking inner loop

                        elif "Sorry! unable to recognize" in translatingText:   # Unable to recognize
                            translatingText = vc().inputAudio() # Listening again for translating text
                            continue            # Looping back

                        else:   # Translate again
                            if (not flag):      # if not the first statement to get translated

                                # Asking for translating statement
                                vc().outputAudio("Speak")
                                print("Speak...")

                                # Listening Translating statement
                                translatingText = vc().inputAudio()

                            # Phrase being Translated
                            print("Phrase being Translated :", translatingText)

                            # Translating the text
                            self.translateNarration(translatingText, in_lang, out_lang)
                            # Waiting for some time to speak translated text
                            time.sleep(8)

                            # asking formore translation
                            vc().outputAudio("Anymore translation?")
                            # Listening user's choice
                            translatingText = vc().inputAudio()

                            flag = False        # Translated Statement is not the first anymore
                            continue            # Looping back

                # Unable to understand the languages OR Listened for only one language(unable to listen two different languages)
                else:
                    # Asking to tell i/o languages again
                    vc().outputAudio("Please say again")
                    continue    # Looping back
            except:
                # Unable to recognise voice OR Unable to fetch language code
                vc().outputAudio("Please say again")


    def translateNarration(self, translatingText, in_lang, out_lang):
        '''
        For Translation
        Parameters : 
        a) translatingText = text to be translated
            -> string being translated
        b) in_lang = from language
            -> language in which translatingText is
        c) out_lang = to language
            -> language in which translation is to be performed
        '''
        in_lang = self.language_codes[in_lang]
        # finding language code for in_lang
        out_lang = self.language_codes[out_lang]
        # finding language code for out_lang

        try:
            # Translating
            translatedText = Translator().translate(translatingText, src=in_lang, dest=out_lang)
            # Fetching translated text
            translatedText = translatedText.text
            # Speaking Translated Text
            vc().googleSpeak(translatedText,out_lang)
        except:
            # Faced issue while Translation
            vc().outputAudio("Faced some issue while translation")