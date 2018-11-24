from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Chatting Section')
bot.set_trainer(ListTrainer)

for files in os.listdir('D:/Documents/Chatting-Section\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
	data = open('D:/Documents/Chatting-Section\chatterbot-corpus-master\chatterbot_corpus\data\english/' +files,'r').readlines()
	bot.train(data)
	
while True:
	message = input('User :')
	if message.strip() != 'Bye':
		reply =bot.get_response(message)
		print('ChatBot :',reply)
	if message.strip() == 'Bye':
		print('ChatBot : Bye , See You..')
		break
		
	
	
  
