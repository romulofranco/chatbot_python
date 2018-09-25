from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Romulo Bot")
conversa = ['Oi', 'Ola', 'Tudo bem?', 'Eu estou bem']
bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
	quest = input('Voce: ')
	resposta = bot.get_response(quest)
	print ('Bot: ', resposta)
	
	
