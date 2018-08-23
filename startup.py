# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from trainers.smalltalk_trainer import SmallTalkTrainer

import logging
logging.basicConfig(level=logging.INFO)

bot_name = 'Ewan'
bot = ChatBot(
    bot_name,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

print("Training " + bot_name + " please wait....")
print("--------------------------------------------------------------")

bot.set_trainer(SmallTalkTrainer)
bot.train(['data.smalltalk', 'data.core'])

print("--------------------------------------------------------------")
print('Hello, my name is ' + bot_name + ", how can I help you today? ")

while True:
    try:
        bot_input = bot.get_response(None)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
