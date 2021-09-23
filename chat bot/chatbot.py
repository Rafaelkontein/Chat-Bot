rom chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# isso aqui só precisa para corrigir o bug
from spacy.cli import download
​
download("en_core_web_sm")
​
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
​
​
chatbot= ChatBot('Norman',tagger_language=ENGSM)
​
conversa =[
    'Olá',
    'Olá, tudo bem?',
    'sim!.',
    'Oque vai ter hoje?',
    'Hoje vamos ter uma reunião com o flavio',
    'Que legal em!',
    'Sim, vamos criar uma Ia !!'
]
​
trainer=ListTrainer(chatbot)
trainer.train(conversa)
List Trainer: [####################] 100%
while True:
    msg= str(input('Sou o Norman da Web marcas, como posso te ajuda?\nUsuario:'))
    if msg == 'Tchau':
        print('Obrigado pela preferencia da Web Marcas.')
        break
    resposta=chatbot.get_response(msg)
    print(resposta)   