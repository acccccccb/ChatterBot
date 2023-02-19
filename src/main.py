from flask import Flask, request
from markupsafe import escape

from chatterbot import ChatBot, languages
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import time
import logging

BOT_NAME = "bot1"
BOT2_NAME = "bot2"
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

chatbot1 = ChatBot(BOT_NAME,
    storage_adapter={
        'tagger_language': languages.CHI,
        'import_path': 'chatterbot.storage.SQLStorageAdapter',
    },
)
chatbot2 = ChatBot(BOT2_NAME,
  storage_adapter={
      'tagger_language': languages.CHI,
      'import_path': 'chatterbot.storage.SQLStorageAdapter',
  },
  )
# clear all data
# chatbot.storage.drop()

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot1)
trainer2 = ChatterBotCorpusTrainer(chatbot2)
trainer.train('./data/chinese')
trainer2.train('./data/chinese')
# trainer.train('./data/custom')

#

# trainer = ListTrainer(chatbot)
# trainer.train([
#     "你好",
#     "你也好",
# ])

# Now we can export the data to a file
trainer.export_for_training('./train/ai.json')
trainer2.export_for_training('./train/ai2.json')

## cli
# inputData = input("> ")
msg = '问题'
while 1 > 0:
    try:
        response1 = chatbot1.get_response(msg)
        print(BOT_NAME + "> " + str(response1))
        response2 = chatbot2.get_response(str(response1))
        print(BOT2_NAME + "> " + str(response2))
        msg = str(response2)
        time.sleep(1)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


## host
# app = Flask('chat_bot')
# @app.route('/message', methods=['POST', 'GET'])
# def message():
#     error = None
#     if request.method == 'POST':
#         if request.form['msg']:
#             inputData = str(request.form['msg']);
#             botRes = chatbot.get_response(inputData)
#             return str(botRes)
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return error
# app.run(host='127.0.0.1',port=5000,debug=False)
