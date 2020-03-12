#Importa Banco de dados mocados
import users

"""
Tips and notes:
    -As soon as you add new handlers to dispatcher, they are in effect.
    -The Filters class contains a number of functions that filter incoming messages for text, images, status updates and more.
     Any message that returns True for at least one of the filters passed to MessageHandler will be accepted. You can also write your own filters if you want.

Commands and requests:
    /saldo - Devolve quanto dinheiro o usuario tem na conta corrente
    /extrato - Pergunta qual extrato vc quer receber: diario, semanal e mensal
    /minhaconta - Devolve uma mensagem para ser compartilhada com outros usuarios para realizar a transferenecia
    /transferencia - Recebe a mensagem gerada em /minhaconta por outro usuario e pergunta o valor a ser transferido
    /calcula - Recebe o valor a vista e o preco da prestacao 
"""

#Headers and bot initiation
from telegram.ext import Updater
updater = Updater(token = '1105160055:AAGkIIuk_M4B3r_uwumehJwJ8ZLwQDqylqo', use_context = True)
dispatcher = updater.dispatcher

#Sets up the logging module
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#Bot functions
def start(update, context):
    reply_keyboard = [['Saldo', 'Extrato', 'Transferencia', 'Calcula']]
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Oi, eu sou seu assistente pessoal da NuBank!\nAntes de poder te ajudar, preciso fazer o seu cadastro!")
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Para isso, me envie seu CPF primeiro:")

def echo(update, context):
    """Echoes sent message, testing usage only
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.text)

#Command Handler
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

#Start the bot
updater.start_polling()