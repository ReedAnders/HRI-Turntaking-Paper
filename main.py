from naoqi import ALProxy

# Connect to NAO
# tts = ALProxy("ALTextToSpeech", "<IP of your robot>", 9559)
tts = ALProxy("ALTextToSpeech", "nao.local", 9559)

# Run Script
tts.say("Hello, world!")