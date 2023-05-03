from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from cleaner import clean_corpus

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

CORPUS_FILE = 'chat.txt'

chatbot = ChatBot('Chatbot')

trainer = ListTrainer(chatbot)

trainer.train(CORPUS_FILE)

exit_conditions = (':q', 'quit', 'exit')
while True:
    query = input('> ')
    if query in exit_conditions:
        break
    else:
        print(f'🤖 {chatbot.get_response(query)}')
