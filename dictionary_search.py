# From https://github.com/ShudarsanRegmi/pythonDictionary/blob/master/4_dictionary.py

import requests
import json
import argparse
# from playsound import playsound

# Dictionary class for the dictionary api
class Dictionary():

    def __init__(self):
        self.lang="en_US"
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-w",default=None,help="Word to Search")
        self.parser.add_argument("-l",default="en_US",help="Language")
        self.parser.add_argument("-a",default=None,help="Shows all avaibales languages(use \"all\" as argument)")
        self.args = self.parser.parse_args()

    def get_language(self):
        if (self.args.a == "all"):
            self.help()
        if (self.args.l == "uk"):
            self.lang = "en_GB"
        elif self.args.l == "hi":
            self.lang = "hi"
        elif self.args.l == "fr":
            self.lang == "fr"
        elif self.args.l == "es":
            self.lang = "es"
        elif self.args.l == "de":
            self.lang == "de"

    def help(self):
        print("""Avaibales languages are: 
        English(us) --> en_US
        English(UK) --> uk
        Hindi       --> hi
        French      --> fr
        Spanish     --> es
        German      --> de
        """)

    def search(self, word):
        url = "https://api.dictionaryapi.dev/api/v2/entries/"+self.lang+"/"+word
        try:
            response = requests.get(url)
            responseText = response.text
            result = json.loads(responseText)
            if(response.status_code == 404):
                print("No word found")
            else:
                #final results
                word = result[0]["word"]
                phonetics = result[0]["phonetics"]
                phoneticsText = phonetics[0]["text"]
                phoneticsAudio = phonetics[0]["audio"]
                #meanings
                print("----------------------------------------------")
                print(f"| Word: {word} ({phoneticsText})")
                print("| Click here for Pronunciation: ",phoneticsAudio)
                print("----------------------------------------------")
                # pprint(result[0]["meanings"])
                length = len(result[0]["meanings"])
                for i in range(length):
                    print("-------------------------------------------")
                    try:
                        print("| Part of Speech: ",result[0]["meanings"][i]["partOfSpeech"])
                    except KeyError:
                        print("| Parts Of Speech Unavaibale")
                    try:
                         print("| Definition: ",result[0]["meanings"][i]["definitions"][0]["definition"])
                    except KeyError:
                         print("| Definition was not Found")
                    try:
                        print("| Example: ",result[0]["meanings"][i]["definitions"][0]["example"])
                    except KeyError:
                        print("| Example not available!!")
                    print("-------------------------------------------")
                #while True:
                    #pressedKey = input("Press Enter For Pronunciation(q for quit!)")
                    #if(pressedKey == "quit" or pressedKey == "exit" or pressedKey =="q" or pressedKey =="stop" ):
                        #break
                    #else:
                        #try:
                            #playsound(phoneticsAudio)
                        #except:
                            #print("Unable to play audio")
        except KeyboardInterrupt:
            print("Quitting..")
        except:
            print("Unable to connect to the server! Try checking your Internet Connection")