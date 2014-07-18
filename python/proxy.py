from naoqi import ALProxy
#from PyQt4.QtCore import QString, QStringList

ip = "";

mem = None
mot = None
sonar = None
textToSpeech = None
led = None
asr = None
aup = None
pose = None
behavior = None
aud = None
battery = None
redBallTracker = None
redBallDetection = None
faceTracker = None
cam = None

def setProxy(IP):
    global ip
    global mem
    global mot 
    global sonar 
    global textToSpeech 
    global led 
    global asr 
    global aup 
    global pose 
    global behavior 
    global aud 
    global battery 
    global redBallTracker 
    global redBallDetection 
    global faceTracker 
    ip = IP
    
    mem = ALProxy("ALMemory" , IP , 9559)
    mot = ALProxy("ALMotion" , IP , 9559)
    sonar = ALProxy("ALSonar" , IP , 9559)
    textToSpeech = ALProxy("ALTextToSpeech" , IP , 9559)
    led = ALProxy("ALLeds" , IP , 9559)
    asr = ALProxy("ALSpeechRecognition" , IP , 9559)
    aup = ALProxy("ALAudioPlayer",IP, 9559)
    pose = ALProxy("ALRobotPose" , IP ,9559)
    behavior = ALProxy("ALBehaviorManager" , IP ,9559)
    aud = ALProxy("ALAudioDevice" , IP ,9559)
    battery = ALProxy("ALBattery" , IP ,9559)
    redBallTracker = ALProxy("ALRedBallTracker", IP, 9559)
    redBallDetection = ALProxy("ALRedBallDetection", IP, 9559)
    faceTracker = ALProxy("ALFaceTracker", IP, 9559)
    cam = ALProxy("ALVideoDevice", IP, 9559)
    aud.setOutputVolume(50)
    return "Robot Connected"

def isProxySet():
    if ip == "":
        return False
    else:
        return True		

'''class MyALBehaviorManager():
    #def __init__(self):
    #    i = 0
    def post(self):
        behavior.post.runBehavior('User/Protect')
        behavior.post.stopAllBehaviors()
    def stopAllBehaviors(self):
        behavior.stopAllBehaviors()

class textToSpeechParameterChanged():
    
    def __init__(self, speed = 85, voiceShaping = 100):
        self._speed = speed
        self._voiceShaping = voiceShaping
    
    def setSpeed(self, value):
        self._speed = value
        
    def setVoiceShaping(self, value):
        self._voiceShaping = value
        
    def getSpeed(self):
        return self._speed 
    
    def getVoiceShaping(self):
        return self._voiceShaping   
        
    def post(self, p):
        tempStringList  = QString(p).split('. ')
        for string in tempStringList: 
            sentence = "\RSPD="+ str( self.getSpeed()) + "\ "
            sentence += "\VCT="+ str( self.getVoiceShaping() ) + "\ "
            sentence += str(string)
            sentence +=  "\RST\ "
            textToSpeech.post.say(str(sentence))
            
    def say(self, p):
        tempStringList  = QString(p).split('. ')
        for string in tempStringList:  
            sentence = "\RSPD="+ str( self.getSpeed()) + "\ "
            sentence += "\VCT="+ str( self.getVoiceShaping() ) + "\ "
            sentence += str(string)
            sentence +=  "\RST\ "
            textToSpeech.say(str(sentence))

print 'success'

ConfigFileName='Config.txt'
ConfigFile = open(ConfigFileName , "r")   
#Read whole file into data
array = QStringList()
for line in ConfigFile:
    lineArray = QString(line).split(" ")
    for lineElement in lineArray:
        array.append(lineElement)

VoiceSpeedIndex = array.indexOf("VoiceSpeed")
VoiceShapingIndex = array.indexOf("VoiceShaping")
SessionDurationInMinsIndex = array.indexOf("SessionDurationInMins")
SessionDurationInMins = array[SessionDurationInMinsIndex + 1]

if ((VoiceSpeedIndex != -1) and (VoiceShapingIndex != -1)):
    say = textToSpeechParameterChanged(array[VoiceSpeedIndex + 1], array[VoiceShapingIndex + 1])
    myt =  say.getSpeed()
    
    myBehavior = MyALBehaviorManager()
 
  
elif (VoiceSpeedIndex == -1):
    print "VoiceSpeed parameter is not found!"
    
else:
    print "VoiceShaping parameter is not found!"
    

# Close the file
ConfigFile.close() '''                  		
