import os
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

import en_core_web_sm

nlp = en_core_web_sm.load()



# first time you must run the below commands each in a new cell
# 1 . py -m pip install chatterbot
# 2. py -m pip install chatterbot_corpus
# then rerun the imports again

# was just testing this piece of code before i impplemented it

exit_codes = ["Bye", "exit", "quit", "i'm outta here", "i'm out", 'Goodbye']
exit_codes = [x.lower() for x in exit_codes]
print(exit_codes)

# name of the chatbot
x  = ChatBot("BK Chatbot")
# train the chatbot
trainer = ChatterBotCorpusTrainer(x)
trainer.train("chatterbot.corpus.english")
# loop for exiting the code
# try removing the exit_codes and using one word and see what happens
# but it leaves limited choices for the user

while True:
    message = input("Me :")
    if message.strip()!= "Bye":
        reply = x.get_response(message)
        
    print("Robot  : ", reply)
    
    if message.strip() == "Bye":
        print("Robot : It was nice talking to you")
        break


