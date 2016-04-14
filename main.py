from naoqi import ALProxy

# Connect to NAO
# tts = ALProxy("ALTextToSpeech", "<IP of your robot>", 9559)
tts = ALProxy("ALTextToSpeech", "192.168.0.101", 9559)


# Run Script
# tts.say("Hello, world!")

from getch import getch
from time import sleep

convo_prompts = ['Hi, my name is Nao. Can I help you send a package?', 'Please place your package on the table in front of me. Then say, Here you go!', 'Hooray! First, what\'s the address you need the package sent to?','Great! What\'s your account number', 'Many thanks. The estimated time for delivery will be in two days. Is that acceptable?', 'The total cost will be $8 dollars even. Do you confirm I can charge this to your account?','Great, thank you! Do you have any other packages?','Alright, that settles it. Have a nice day!']
pointer = 0

tts.setParameter("pitchShift",0)

## Experiment Procedure

# 1) Participant initiates conversation with Nao
# 2) Experimenter presses space bar to make Nao respond
# 		a) Experimenter should press play bar as if they themselves are responding
# 3) If factor delay is on, set 'wait' variable to 'True'

wait = True

def callAudio(text):

	# Set for 750ms delay (750ms + 250ms (Experimenter delay) = 1s delay)
	if wait:
		sleep(0.75)

	tts.say(text)
	# print text

while True:
    key = ord(getch())

    # Press escape (or arrow keys) to exit
    if key == 27:
    	break

    # Press spacebar play audio and iterate
    elif key == 32:
    	
    	try:
    		callAudio(convo_prompts[pointer])
    		pointer += 1
    	except IndexError:
    		print "FINISHED: Experiment has ended."
    		break
