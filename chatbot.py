from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import en_core_web_sm

nlp = en_core_web_sm.load()

#create a chatbot instance 
chatbot = ChatBot(
    'BkChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

#train the chatbot
training_data_questions = open("training_data/personal_robonal.txt").read().splitlines()
training_data_personal = open("training_data/personal_robonal.txt").read().splitlines()

training_data = training_data_personal + training_data_questions

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# train with the english corpus
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train("chatterbot.corpus.english")
