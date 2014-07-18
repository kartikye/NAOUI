import sys
import time

import proxy
import posture


first = True

def setup():
    return 0

def dataController(dataType, dataContent = ""):
    global first
    print >>sys.stderr, 'dataController %s \n' % dataType
    print >>sys.stderr, '%s \n' % proxy.isProxySet()
    if proxy.isProxySet():
        '''if first:
            setup()
            first = False
        else:'''
#Settings
    #Stiffness On 
        if dataType == "son":
            print >>sys.stderr, 'Stiffness On \n'
            proxy.mot.setStiffnesses("Body", 0.8)
            proxy.led.post.fadeRGB('AllLeds', 0x00909428, 2.0)
    #Stiffness Off    
        elif dataType == "sof":
            print >>sys.stderr, 'Stiffness Off \n'
            posture.squat()
            proxy.mot.setStiffnesses("Body", 0)
    #Volume    
        elif dataType == "vol":
            print >>sys.stderr, 'Volume set to %s \n' % dataContent
            proxy.aud.setOutputVolume(int(dataContent))
            proxy.textToSpeech.say("Volume set to %s " % dataContent)
#Postures
    #Squat    
        elif dataType == "squ":
            print >>sys.stderr, 'Squat \n'
            posture.squat()
    #Stand Up    
        elif dataType == "sta":
            print >>sys.stderr, 'Stand Up \n'
            proxy.behavior.runBehavior('User/StandUp0831')  
    #Shake Head       
        elif dataType == "sha":
            print >>sys.stderr, 'Shake Head \n'
            posture.shakehead()  
    #Clap     
        elif dataType == "cla":
            print >>sys.stderr, 'Shake Head \n'
            print "Clapping"
            posture.standup()
            proxy.behavior.runBehavior('User/Clapping') 
    #Wave
        elif dataType == "wav":
            print "Waving Goodbye"
            posture.standup()
            proxy.behavior.runBehavior('User/waveRhand') 
    #Long Nod
        elif dataType == "nol":                 
            print "Long nodding head"
            posture.nodhead(2)
    #Short Nod
        elif dataType == "nos":                 
            print "Short nodding head"
            posture.nodhead(1)  
    #Think
        elif dataType == "thi":                 
            posture.standup()
            print "Thinking"
            proxy.textToSpeech.post.say('hmmm')
            proxy.behavior.runBehavior('User/Thinking2')
            posture.checkrobotpose()
            posture.standup()
    #Ask Again
        elif dataType == "aag":
            posture.standup()
            print 'Asking again'
            x = posture.random.randint(0, 1)
            if x == 0:
                proxy.behavior.runBehavior('User/AskingAgain')
                print "Asking againL"
            else:
                proxy.behavior.runBehavior('User/AskingAgainR')
                print "Asking againR"
            time.sleep(1)
            posture.checkrobotpose()
    #Cough
        elif dataType == "cou":
            posture.standup()
            print "Coughing"
            proxy.behavior.runBehavior('User/Coughing')
    #Sneeze
        elif dataType == "sne":
            posture.standup()
            print "Sneezing"
            proxy.behavior.runBehavior('User/Sneezing')
    #Sleep
        elif dataType == "sle":
            print "Sleep"
            proxy.behavior.runBehavior('User/Sleeping')
#Dances    
    #Hakuna Matata
        elif dataType == "dha":
            posture.standup()
            print "Dancing Hakuna Matata"
            proxy.behavior.post.runBehavior('User/HakunaMatata')
    #Latino
        elif dataType == "dla":        
            posture.standup()
            print "Dancing Latino"
            proxy.behavior.post.runBehavior('User/Latino')
    #Jingle Bell Rock
        elif dataType == "dji":
            posture.standup()
            print "Dancing JingleBellRock"
            proxy.behavior.post.runBehavior('User/JingleBellRock')     
            posture.standup()
    #Short Funny dance
        elif dataType == "dsh":
            posture.standup()
            print "Dancing Short Funny Dance"
            proxy.behavior.post.runBehavior('User/DanceFun')
    #Gangnam Style
        elif dataType == "dga":
            posture.squat()
            print "Dancing Gangnam Style"
            proxy.behavior.runBehavior('User/Dance_GangnamStyle3')
    #It's My Life
        elif dataType == "dit":        
            posture.squat()
            print "Dancing It's My Life"
            proxy.behavior.runBehavior('User/It_Is_My_Life')
    #Let It Go
        elif dataType == "dle":  
            posture.squat()
            proxy.behavior.runBehavior('User/LetItGo')
#Emotions
    #Laugh
        elif dataType == "ela":
            posture.standup()
            print "Happy Emotions"
            proxy.behavior.runBehavior('User/Laughing')
            posture.standup()
    #Happy
        elif dataType == "eha":
            posture.standup()
            print "Happy Emotions"
            tempVolume = proxy.aud.getOutputVolume()
            proxy.behavior.runBehavior('User/Happy2')  
            proxy.aud.setOutputVolume(tempVolume)
        
    #Joyful
        elif dataType == "ejo":
            posture.standup()
            print "Joyful Emotions"
            proxy.behavior.runBehavior('User/Joy4')

    #Surprise
        elif dataType == "esu":
            posture.standup()
            print "Surprise Emotions"
            x = posture.random.randint(0, 1)
            if x == 0:
                proxy.behavior.runBehavior('User/Surprise')
            elif x == 1:    
                #proxy.behavior.runBehavior('User/Amazement')
                proxy.behavior.runBehavior('User/Surprise')
    #Fearful
        elif dataType == "efe":
            posture.standup()
            print "Fear Emotions"
            proxy.behavior.runBehavior('User/Fear1')
            posture.standup()
    #Sad
        elif dataType == "esa":
            posture.standup()
            print "Sad Emotions"
            proxy.behavior.runBehavior('User/Sad4')
        
    #Disgust
        elif dataType == "edi":
            posture.standup()
            print "Disgusting Emotions"
            tempVolume = proxy.aud.getOutputVolume()
            proxy.behavior.runBehavior('User/Disgusting2')       
            proxy.aud.setOutputVolume(tempVolume)
            posture.standup()

    #Amazement
        elif dataType == "ema":
            posture.standup()
            print "Amazement Emotion"
            proxy.behavior.runBehavior('User/Amazement')

    #Angry
        elif dataType == "ean":      
            posture.standup()
            print "Angry"
            tempVolume = proxy.aud.getOutputVolume()
            proxy.behavior.runBehavior('User/angry')
            proxy.aud.setOutputVolume(tempVolume)
    #Angry Sit
        elif dataType == "eas":
            posture.standup()
            print "Angry Sit"
            tempVolume = proxy.aud.getOutputVolume()
            proxy.behavior.runBehavior('User/AngrySit')
            time.sleep(3)
            proxy.behavior.post.runBehavior('User/turnOnEyesLED')
            proxy.behavior.runBehavior('User/StandUp0831') 
            proxy.aud.setOutputVolume(tempVolume)
#Simon Says
    #Instructions 1
        elif dataType == "ss1":  
            print "on_pushButtonSimonSaysInstrutions1_clicked"
            proxy.textToSpeech.post.say("Now we're going to play Simon Says. It is a copying game. ")
   
    #Instructions 2
        elif dataType == "ss2":  
            print "on_pushButtonSimonSaysInstrutions2_clicked"
            proxy.textToSpeech.post.say("In this game, I'm going to say 'Simon says follow by an action'. You only do the same action after I say Simon Says.")
 
    #Instructions 3
        elif dataType == "ss3":  
            print "on_pushButtonSimonSaysInstrutions3_clicked"
            proxy.textToSpeech.say("For example, if I say 'Simon Says shake your head', then you have to shake your head. Like this.")
            print "Shaking head"    
            posture.shakehead()  
    #Instructions 4
        elif dataType == "ss4":
            print "on_pushButtonSimonSaysInstrutions4_clicked"
            proxy.textToSpeech.post.say("Lets try!")
            
    #Instructions 5
        elif dataType == "ss5":  
            print "on_pushButtonSimonSaysInstrutions5_clicked"
            proxy.textToSpeech.say("Simon Says wave your hands.")
            proxy.behavior.runBehavior('User/waveRhand')
    #Instructions 6a
        elif dataType == "s6a":
            print "on_pushButtonSimonSaysInstrutions6a_clicked"
            proxy.textToSpeech.post.say("That's right!")
    #Instructions 6b
        elif dataType == "s6b":  
            print "on_pushButtonSimonSaysInstrutions6b_clicked"
            proxy.textToSpeech.say("No, when I say 'Simon says, wave your hands' You do this")
            print "Wave Your hands"
            proxy.behavior.runBehavior('User/waveRhand')
    #Instructions 7
        elif dataType == "ss7":  
            print "on_pushButtonSimonSaysInstrutions7_clicked"
            proxy.textToSpeech.post.say("If I did not say 'Simon Says' before the action, then you must stay still. Do not move. ")
    #Instructions 8
        elif dataType == "ss8":  
            print "on_pushButtonSimonSaysInstrutions8_clicked"
            proxy.textToSpeech.post.say("Do you understand the game?")
    #Instructions 9
        elif dataType == "ss9":  
            print "on_pushButtonSimonSaysInstrutions9_clicked"
            proxy.textToSpeech.post.say("Let's start!")
    #Instructions 10
        elif dataType == "s10":  
            print "on_pushButtonSimonSaysInstrutions10_clicked"
            proxy.textToSpeech.post.say("If I say 'clap your hands'. What do you do?")
    #Instructions 11
        elif dataType == "s11":                   
            print "on_pushButtonSimonSaysInstrutions11_clicked"
            proxy.textToSpeech.post.say("No, I did not say 'Simon says', so you should not move.")
    #Instructions 12
        elif dataType == "s12":  
            print "on_pushButtonSimonSaysInstrutions12_clicked"
            proxy.textToSpeech.post.say("Lets try another one. Ready?")
    #Simon Says Clap
        elif dataType == "scl":
    #Simon Says Wave   
        elif dataType == "swa":
    #Simon Says Shake     
        elif dataType == "ssh":
    #Simon Says Nod      
        elif dataType == "sno":
    #Simon Says Step Left      
        elif dataType == "ssl":
    #Simon Says Step Right      
        elif dataType == "ssr":
    #Simon Says Squat       
        elif dataType == "sss":
    #Simon Says Turn Left       
        elif dataType == "stl":
    #Simon Says Turn Right      
        elif dataType == "str":
    #Simon Says Turn Around      
        elif dataType == "sst":

 
    else:
        if dataType == "ipa":
            return proxy.setProxy(dataContent)