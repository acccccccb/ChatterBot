from flask import Flask, request
from markupsafe import escape

from chatterbot import ChatBot, languages
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import time
import logging

BOT_NAME = ""
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

chatbot = ChatBot(BOT_NAME,
    storage_adapter={
        'tagger_language': languages.CHI,
        'import_path': 'chatterbot.storage.SQLStorageAdapter',
    },
)
# clear all data
# chatbot.storage.drop()

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('./data/chinese')
# trainer.train('./data/custom')

#

# trainer = ListTrainer(chatbot)
# trainer.train([
#     "你好",
#     "你也好",
# ])

# Now we can export the data to a file
trainer.export_for_training('./train/ai.json')

## cli
# inputData = input("> ")
msg = '问题';
while 1 > 0:
    try:
        print("> " + msg)
        response = chatbot.get_response(msg)
        print(str(BOT_NAME + "> ") + str(response))
        msg = str(response)
        time.sleep(0.2)
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
