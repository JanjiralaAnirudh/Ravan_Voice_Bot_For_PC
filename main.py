import functions
import speech_recognition

listener = speech_recognition.Recognizer()

def run_query(command):
    if "play" in command:
        functions.play_song(command)

    elif "time" in command:
        functions.time()

    elif ("date" in command):
        functions.date()

    elif "bluetooth" in command:

        if "on" in command:
            functions.bluetooth_access(command)
        elif "off" in command:
            functions.bluetooth_access(command)
        elif "half" in command:
            functions.bluetooth_access(command)
        elif ("check" in command) or ("status" in command) or ("state" in command):
            functions.bluetooth_access(command)
        else:
            functions.talk("please tell it in a proper manner")

    elif ("open" in command) and ("camera" in command):
        functions.open_camera()
        pass

    elif "open" in command:
        command = command.replace("open","")
        functions.check_application(command)
        if "whatsapp" in command:
                functions.open_whatsapp()
        else :
                functions.talk("not found!!!!!!!!!")
            
    elif ("volume" in command) or ("sound" in command):
        if ("increase" in command) or ("up" in command) :       functions.increse_sound()

        if ("decrease" in command) or ("down" in command):       functions.decrese_sound()

        if "mute" in command:       functions.mute_sound()

        if "unmute" in command:         functions.unmute_sound()

    elif ("power off") in command:  functions.shut_down()

    elif ("power half") in command: functions.shut_down()

    elif (("turn off") in command) or (("turn half")  in command) or (("turn of") in command):
        if ("pc" in command) or ("system" in command) or ("computer" in command):
            functions.shut_down()

    elif (("shut down" in command) and ("system" in command)) or (("shut down" in command) and ("pc" in command)) or (("shut down" in command) and ("computer" in command)) or (("shutdown" in command) and ("computer" in command)) or (("shutdown" in command) and ("system" in command)):  
        functions.shut_down()

    elif (("lock" in command) and ("system" in command)) or (("lock" in command) and ("pc" in command)) or (("lock" in command) and ("computer" in command)):   
        functions.lock_system()

    elif (("restart" in command) and ("system" in command)) or (("restart" in command) and ("pc" in command)) or (("restart" in command) and ("computer" in command)):   
        functions.restart_sys()

    elif ("wi-fi") in command:
        if " on " in command:
            functions.talk("yes your wi-fi is in on")
        elif ("off" in command) or ("half" in command):
            functions.talk("it is misson impossible")
        elif ("check" in command) or ("status" in command) or ("state" in command) :
            functions.wifi_status()
        elif ("network" in command) or ("connected" in command) or ("name" in command):
            functions.wifi_net_con()
        else :
            functions.talk("can you say it on proper manner ")
    
    elif ("charging" in command) or ("charge" in command) or ("battery" in command):
        if ("percent" in command) or ("percentage" in command) or ("level" in command):
            functions.BatteryPercentage()
        if ("check"  in command) or ("connect" in command) or ("connected" in command):
            functions.in_charge_or_not()
    elif ("user" in command) and (("pc" in command) or ("system" in command) or ("computer" in command)):
        functions.get_username()

    elif (("last" in command) and ("query" in command)) or (("previous" in command) and ("query" in command)) or (("previous" in command) and ("command" in command)) or (("last" in command) and ("command" in command)):
        functions.get_queries()
    
    elif (("close" in command) and ("tab" in command)) or (("close" in command) and ("app" in command)) or (("close" in command) and ("application" in command)) or (("exit" in command) and ("tab" in command)) or (("exit" in command) and ("app" in command)) or (("exit" in command) and ("application" in command)):
        functions.tab_closing()
        
    else:
        functions.talk("it doesn't programmed or i don't know")    

try:
    functions.talk("hai this is arey Ravan\nhow can i help you")
    with speech_recognition.Microphone() as source:
        print("now u can speak")
        voice = listener.listen(source)
        query = listener.recognize_google(voice)
        query = query.lower()
        print(query)
        if (("last" in query) and ("query" in query)) or (("previous" in query) and ("query" in query)) or (("previous" in query) and ("command" in query)) or (("last" in query) and ("command" in query)):
            run_query(query)
        else :                
            functions.save_query_to_csv(query)
            run_query(query)
except:
    functions.talk("check the internet connection or may be any error occured")
