from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import time 
time.clock = time.time
import logging 
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)



bot = ChatBot('myBot')

trainer = ListTrainer(bot)


for file in os.listdir('data/'):
    data = open('data/'+file, 'r', encoding='utf-8').readlines()
    trainer.train(data)


print("*************WELCOME*************")
print("----- press q to exit -----")
while True:
    query = input('>>>')
    if query.lower()=="q":
        exit()
    else:
        ans = bot.get_response(query)
        print("Bot-> ",ans)