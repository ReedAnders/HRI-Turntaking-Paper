# from naoqi import ALProxy

# Connect to NAO
# # tts = ALProxy("ALTextToSpeech", "<IP of your robot>", 9559)
# tts = ALProxy("ALTextToSpeech", "nao.local", 9559)


# Run Script
# tts.say("Hello, world!")

from getch import getch
from time import sleep

convo_prompts = ['Hi, my name is Nao', 'This is an audio test']
pointer = 0

# Set for 500ms delay
wait = True

def callAudio(text):
	if wait:
		sleep(0.5)
		
	# tts.say(text)
	print text

while True:
    key = ord(getch())
    print key

    # Press escape (or arrow keys) to exit
    if key == 27:
    	break

    # Press spacebar play audio and iterate
    elif key == 32:
    	
    	try:
    		callAudio(convo_prompts[pointer])
    		pointer += 1
    	except IndexError:
    		print "Audio ended, thanks."
    		break
