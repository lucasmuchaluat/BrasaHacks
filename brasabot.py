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

#Function callers
CPF = range(12)
SENHA = range(12)

#Sets up the logging module
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#Bot functions
def start(update, context):
    reply_keyboard = [['Saldo', 'Extrato', 'Transferencia', 'Calcula']]
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Oi, eu sou seu assistente pessoal da NuBank!\nAntes de poder te ajudar, preciso fazer o seu cadastro!")
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Para isso, me envie seu CPF primeiro(APENAS NUMEROS):")
    return CPF

def cpf(update, context):
    cpf = update.message.from_user
    logger.info("CPF: %s", cpf)
    update.message.reply_text("Obrigado! Agora digite a sua senha da NuConta")
    return SENHA

def senha(update, context):
    senha = update.message.from_user
    logger.info("Senha: %s", senha)
    update.message.reply_text("Tudo ok!, seja bem vindo, %s", senha.first_name)

def echo(update, context):
    """Echoes sent message, testing usage only
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.text)

def sair(update, context):
    user = update.message.from_user
    logger.info("%s saiu", user.first_name)
    update.message.reply_text("Tchau %s! Espero te ver de novo!", user.first_name)

def error(update, context):
    """Error logger
    """
    logger.warning("%s caused %s", update, context.error)
    return ConversationHandler.END 

#Commands/Conversation Handler
from telegram.ext import CommandHandler
#start_handler = CommandHandler('start', start)
#dispatcher.add_handler(start_handler)

from telegram.ext import MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        #CPF: [MessageHandler(Filters.text, cpf)],
        CPF: [CallbackQueryHandler(cpf)],
        SENHA: [MessageHandler(Filters.text, senha)]
    },
    fallbacks = [CommandHandler("sair", sair)]
)
dispatcher.add_handler(conv_handler)

#Log errors
dispatcher.add_error_handler(error)

#Start the bot
updater.start_polling()