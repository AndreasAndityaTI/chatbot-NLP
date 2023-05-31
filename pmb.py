# pmb.py
import aiml,os
kern = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kern.bootstrap(brainFile = "bot_brain.brn")
else:
    kern.bootstrap(learnFiles = "pmb.xml", commands = "pmb")
    kern.saveBrain("bot_brain.brn")
# Press CTRL-C to break this loop
while True:
    user_input = kern.respond(input("USER > "))
    user_input.upper()
    if user_input:
        print("Bot > ", user_input)
    else:
        print("Bot > Maaf Ka, saya kurang mengerti. Bisakah diulangi lagi?" )