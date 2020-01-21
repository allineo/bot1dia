import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = 'Olá, ' + firstName + '!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def feedback(update, context):
    try:
        message = 'feedback!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))

def cancel(update, context):
    return ConversationHandler.END


def main():
    # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
    token = 'cole_aqui_o_token_de_acesso_do_seu_bot'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('feedback', feedback)],
        states={
        #    GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
        #    BIO: [MessageHandler(Filters.text, bio)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    updater.dispatcher.add_handler(conversation_handler)
    
    # updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()