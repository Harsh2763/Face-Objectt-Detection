# Python program to translate 
# speech to text and text to speech 
  
  
import speech_recognition as sr 
import pyttsx3
import object_detection as od
import cv2
flag=False
#def object_detection():
import object_detection as od

##### Edited by me####

##### Edited by me####
def object_detection():
    SpeakText("Object recognation activated......")
    objects=od.counting()
    print(objects)
    final=objects[1:]
    print("objects detected are "+final)
    SpeakText("objects detected are "+final)
    
    
    
import FaceRecognation
def person_detection():
    SpeakText("Face recognation activated......")
    person=FaceRecognation.mark_attend()
    print("Person Detected is "+person)
    SpeakText("Person Detected is "+person)
##### Edited by me####


def line_follow():
    import line
    SpeakText("Text recognation activated......")
    line1=line.motor_speed()
    print(""+line1)
    SpeakText(""+line1)

##### Edited by me####


# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init()
    ##### Edited by me####
   # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
   # engine.setProperty('voice', voice_id)
    ##### Edited by me####
    engine.say(command)  
    engine.runAndWait()
    #engine = pyttsx3.init('sapi5')
    #voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

#voices = engine.getProperty('voices') 
#engine.setProperty('voice', voice_id)
      
      
# Loop infinitely for user to 
# speak

def call():
    global c_text

    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower()
            c_text=MyText
            
  
            print("Did you say "+MyText)
            SpeakText(MyText)
            #MyText.replace(" ","1")
            print(MyText)
            if(MyText=="person detection" or MyText=="person"):
                print("face Recognation Activated..")
                person_detection()

            if(MyText=="object detection" or MyText=="object"):
                print("Object Recognation Activated..")
                
                object_detection()
                

            if(MyText=="line following" or MyText=="line"):
               print("line following Activated...")
               line_follow()
                

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured")
        
       
        
        if(c_text=="person detection" or c_text=="person"):
                print("face Recognation Activated..")
                person_detection()

        if(c_text=="object detection" or c_text=="object"):
                print("Object Recognation Activated..")
                
                object_detection()
                

        if(c_text=="text recognation" or c_text=="text"):
                print("Text Detection Activated..")
            
while(1):
    print("...")
    
    call()
