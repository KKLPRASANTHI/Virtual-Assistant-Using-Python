import speech_recognition as sr
import subprocess
import playsound 
from gtts import gTTS 
import os
import wolframalpha 
from selenium import webdriver 
import datetime
import warnings
import calendar
import wikipedia
import webbrowser
import random
import smtplib
import pyjokes
import cv2
import time
import requests
import json#OpenWeather Map API Key --- 208fba84734ba576c4528f7157396ab2
import wx
import win32api
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
num = 1
asname='Paida'
def assistant_speaks(output):
    global num
    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print(asname+" : ", output)
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file) 
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        assistant_speaks("Good Morning!") 
   
    elif hour>= 12 and hour<18: 
        assistant_speaks("Good Afternoon!")    
   
    else: 
        assistant_speaks("Good Evening!") 
    assistant_speaks("I am your Assistant "+asname)  
def takeInput():
    take=input()
    return take
def get_audio():
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit = 10)
        #audio = rObject.listen(source)
        print("Stop.")
        try:
            text = rObject.recognize_google(audio, language ='en-US')
            print("You : ", text)
            return text
        except:
            assistant_speaks("Could not understand your audio, PLease try again !")
            return ''
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    #server.ehlo() 
    server.starttls()
    # Enable low security in gmail 
    server.login('kklprasanthi24@gmail.com', 'Alivelu@7') 
    server.sendmail('kklprasanthi24@gmail.com', to, content) 
    server.close()
def sendEmailWithAtchmnt():
    msg = MIMEMultipart()
    fromaddr = 'kklprasanthi24@gmail.com'
    msg['From'] = 'kklprasanthi24@gmail.com'
    assistant_speaks('Please Enter the body of mail')
    body=input()
    assistant_speaks('Please Enter the Subject of mail')
    msg['Subject']=input()
    msg.attach(MIMEText(body, 'plain'))
    assistant_speaks("Enter the file name")
    filename=input()
    assistant_speaks("Enter the file path")
    path=input()
    attachment = open(path, "rb") 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, "Alivelu@7") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    assistant_speaks("Enter the receivers Email ids")
    l=[]
    while True:
        key=input()
        if key=='0':
            break
        l.append(key)
    for mail in l:
        toaddr=mail.strip()
        msg['To']=mail.strip()
        s.sendmail(fromaddr, toaddr, text)
def search_web(input): 
        driver = webdriver.Chrome('./chromedriver')
        driver.implicitly_wait(1)
        driver.maximize_window()
        if 'youtube' in input.lower():
            assistant_speaks("Opening in youtube")
            indx = input.lower().split().index('youtube')
            query= input.split()[indx + 1:]
            driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
            #return
        if 'wikipedia' in input.lower():
            assistant_speaks("Opening Wikipedia")
            indx = input.lower().split().index('wikipedia')
            query = input.split()[indx + 1:]
            driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
            #return
        else:
            if 'google' in input:
                print("HERE")
                indx = input.lower().split().index('google')
                query = input.split()[indx + 1:]
                driver.get("https://www.google.com/search?q=" + '+'.join(query))
            elif 'search' in input:
                indx = input.lower().split().index('google')
                query = input.split()[indx + 1:]
                driver.get("https://www.google.com/search?q=" + '+'.join(query))
            else:
                driver.get("https://www.google.com/search?q=" + '+'.join(input.split()))
        os.system("pause")
# function used to open application 
# present inside the system. 

def open_application(input):
    temp=input.split()
    if 'youtube' in input:
        assistant_speaks("Here you go to Youtube") 
        webbrowser.open("youtube.com")
    if 'stack overflow' in input:
        assistant_speaks("Here you go to Stack Over flow.Happy coding") 
        webbrowser.open("stackoverflow.com")
        os.system("pause")
    if "chrome" in input or 'google' in input:
        assistant_speaks("opening Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    if "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Mozilla Firefox.lnk')
    if "sublime" in input:
        assistant_speaks("Opening sublime text")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Sublime Text 3.lnk')
    if "anydesk" in input or 'desk' in input:
        assistant_speaks("Opening AnyDesk")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\AnyDesk\AnyDesk.lnk')
    if "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
    if "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
    if "notepad" in input:
        assistant_speaks("Opening Note Pad")
        os.startfile(r'C:\Users\K.K.L.PRASANTHI\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk')
    if "power point" in input or 'powerpoint' in input:
        assistant_speaks("Opening Power point")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk')
    if "team viewer" in input or 'team viewer' in input or 'team' in input:
        assistant_speaks('Opening Team viewer')
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\TeamViewer.lnk')
    #l=["power point",'powerpoint','notepad',"team viewer",'team viewer','team','youtube','chrome','google',"firefox","mozilla","sublime","anydesk",'desk','word','excel',"power point",'powerpoint']
    #for ele in l:
     #   pass
    #else:  
    #   assistant_speaks("Application not available")
     #   return
    os.system("pause")
        #return
def getDate():
    
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]# e.g. Monday
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
       'June', 'July', 'August', 'September', 'October', 'November',   
       'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']
   
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'
def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False
def isLoveWord(text):
    LOVE_WORDS=['i love you','i like you','love you','love you so much','love you to the moon and back']
    text=text.lower()
    for phrase in LOVE_WORDS:
        if phrase in text:
            return True
    return False
def isMissWord(text):
    MISS_WORDS=['i miss you','i miss you very much','miss you a lot','miss you so much','i missed you so much','miss you too much']
    text=text.lower()
    for phrase in MISS_WORDS:
        if phrase in text:
            return True
    return False
def loveWord(text):
    LOVE_WORDS=['i love you','i like you','love you','love you so much','love you to the moon and back']
    LOVE_WORD_RESPONSES=['cheers mate, high five','you have excellent taste', 'Thanks you are not so bad yourself', 'Aww thanks take a virtual hug']
    for word in LOVE_WORDS:
        if word in text.lower():
            return random.choice(LOVE_WORD_RESPONSES) + '.'
            
def missWord(text):
    MISS_WORDS=['i miss you','i miss you very much','miss you a lot','miss you so much','i missed you so much','miss you too much']
    MISS_WORD_RESPONSES=['They say absence makes the heart grow fonder',"Don't worry. I'm right here", 'Until we chat again', "Me too. I love having a chinwag with you","Me too. I'm looking forward to our next chat"]
    for word in MISS_WORDS:
        if word in text.lower():
            return random.choice(MISS_WORD_RESPONSES) + '.'
def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']
     # Greeting Response back to the user
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
     # If the users input is a greeting, then return random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    # If no greeting was detected then return an empty string
    return ''
#def love
def getPerson(text):
    wordList = text.split()# Split the text into a list of words
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]
def process_text(input):
    global asname
    try:
        response=''
        #
        #print(input)
        if 'shutdown system' in input:
            speak="Do you wish to shutdown your computer ? (yes / no)"
            assistant_speaks(speak)
            res=get_audio()
            #print('\n')
            
            if res.lower() == 'no': 
                pass
            else:
                assistant_speaks("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")
        elif 'logout' in input or 'log out' in input:
            speak="Do you wish to log out? (yes / no)"
            assistant_speaks(speak)
            ser=get_audio()
            if ser.lower() == 'yes': 
                assistant_speaks("Hold On a Sec ! You are about log out")
                os.system("shutdown -l") 
        elif 'restart' in input:
            speak="Do you wish to restart your computer ? (yes / no)"
            assistant_speaks(speak)
            res=get_audio()
            if res.lower() == 'yes': 
                assistant_speaks("Hold On a Sec ! Your system is about to re start")
                os.system("shutdown /r /t 1")
        elif 'joke' in input: 
            assistant_speaks(pyjokes.get_joke())
        elif 'how are you' in input: 
            assistant_speaks("I am fine, Thank you") 
            assistant_speaks("How are you")
            temp = str(get_audio())
            if 'fine' in temp or "good" in temp: 
                assistant_speaks("It's good to know that your fine")
            return
        elif "change name" in input or "change your name" in input:
            assistant_speaks("What would you like to call me?") 
            temp=''
            temp = str(get_audio())
            if temp!='':
                assistant_speaks('Do you want to change my name to '+temp)
                assistant_speaks('yes or no')
                cons=str(get_audio())
                if 'yes' in cons.lower():
                    assistant_speaks('OK changing my name to '+temp)
                    asname=temp
                    assistant_speaks('Name changed. Thanks for naming me')
                    return
                else:
                    assistant_speaks("That's fine ")
                    return
            else:
                assistant_speaks("That's fine ")
                return 
        elif 'open' in input:
            # another function to open
            # different application availaible
            open_application(input.lower())
            return
        elif (wakeWord(input) == True):
            # Check for greetings by the user
            speak= response + greeting(text)
            assistant_speaks(speak)
            return
         # Check to see if the user said date
        elif isLoveWord(input)==True:
            speak= response + loveWord(text)
            assistant_speaks(speak)
            return
        elif isMissWord(input)==True:
            speak= response + missWord(text)
            assistant_speaks(speak)
            return
        elif 'date' in input:
            get_date = getDate()
            speak=response + ' ' + get_date
            assistant_speaks(speak)
            return
         # Check to see if the user said time
        elif 'time' in input:
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m' #Post Meridiem (PM)
                hour = now.hour - 12
            else:
                meridiem = 'a.m'#Ante Meridiem (AM)
                hour = now.hour
            # Convert minute into a proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)
            speak = response + ' '+ 'It is '+ str(hour)+ ':'+minute+' '+meridiem+' .'
            assistant_speaks(speak)
            return   
        # Check to see if the user said 'who is'
        elif 'who is' in input:
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)            
            speak= response + ' ' + wiki
            assistant_speaks(speak)
            return
       # Assistant Audio Response
        elif 'send email' in input: 
            try:
                assistant_speaks("Do yo want to send attachment with it")
                assistant_speaks("Say yes  or  no")
                atch=takeInput()
                if atch.lower()=='yes':
                    
                    sendEmailWithAtchmnt()
                    assistant_speaks("Email has been sent !") 
                    #assistant_speaks("Do you want to send to multiple people")
                    #mul=input("Yes or No")
                    #if mul.lower()=='yes':
                else:
                    assistant_speaks("ok. What should I say?") 
                    content = takeInput()
                    assistant_speaks('Enter receivers email address')
                    print('\n')
                    to = takeInput()    
                    sendEmail(to, content) 
                    assistant_speaks("Sorry. Email has been sent !") 
            except Exception as e: 
                print(e) 
                assistant_speaks("Sorry. I am not able to send this email") 
        elif "don't listen" in input or "stop listening" in input: 
            assistant_speaks("for how much time you want to stop paida from listening commands")
            #b=get_audio()
            #if str(b).lower()=='random':
            a = int(get_audio())
            time.sleep(a) 
            print(a) 
        elif "locate" in input:  
            indx = input.lower().split().index('locate')
            location= input.split()[indx + 1]
            assistant_speaks("User asked to Locate") 
            assistant_speaks(location)
            webbrowser.open("https://www.google.com/maps/place/" + ''.join(location)+ "") 
            return
        
        elif 'search' in input or 'play' in input or 'set' in input:
            # a basic web crawler using selenium
            input= input.replace("search", "")  
            input = input.replace("play", "")
            input = input.replace("set", "") 
            #webbrowser.open(input)
            search_web(input)
        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Person. Your personal Assistant.
            I am here to make your life easier. You can command me to perform 
	    various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return
        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Prathi"
            assistant_speaks(speak)
            return
        elif "geeksforgeeks" in input:# just
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            assistant_speaks(speak)
            return
        elif "calculate" in input.lower():
            # write your wolframalpha app_id here
            app_id = "L4HLY6-6AG2VV3XP7"
            client = wolframalpha.Client(app_id)
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
        elif "camera" in input or "take a photo" in input:
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                assistant_speaks("Do you want save this image")
                assistant_speaks("say yes or no")
                res=str(get_audio()).lower()
                if res=='yes':
                    assistant_speaks('ok saving image')
                    cv2.imwrite("ASimg"+str(random.randrange(1,100000))+str(random.randrange(1,100000))+".jpg",frame)
                    result = False
                result=False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
        else:
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except Exception as e:
        print(e)
        assistant_speaks("I didn't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)
        
        #assistant_speaks('My bad!! I didn\'t ')

# function used to open application 
# present inside the system. 


# Driver Code

if __name__ == "__main__":
    wishMe()
    c=0
    assistant_speaks("Hey What's your name?")
    name ='Human'
    name = get_audio()
    assistant_speaks("Hello, " + name + '.')
    while(1):
        text=''
        assistant_speaks("What can i do for you?")
        text = get_audio().lower()
        if text == '':
            continue
        #if 'love' in str(text):
            #assistant_speaks("I Love You so much. You are the best "+ name+'.')
           # continue
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, "+ name+'.')
            assistant_speaks('see you soon')
            c=100
            break
        # calling process text to process the query
        if c!=100:
            process_text(text)
