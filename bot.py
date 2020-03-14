import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


STATE1 = 1
STATE2 = 2


def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = 'Olá, ' + firstName + '!'
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def feedback(update, context):
    try:
        message = 'Por favor, digite um feedback para o nosso tutorial:'
        update.message.reply_text(
            message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
        return STATE1
    except Exception as e:
        print(str(e))


def inputFeedback(update, context):
    try: 
        feedback = update.message.text
        print(feedback)
        if len(feedback) > 10:
            message = """Seu feedback foi muito curtinho... 
                            \nInforma mais pra gente, por favor?"""
            update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
            return STATE2
        else:
            update.message.reply_text("Muito obrigada pelo seu feedback!")
    except Exception as e:
        print(str(e))


def cancel(update, context):
    return ConversationHandler.END


def main():
    try:
        # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
        token = 'cole_aqui_o_token_de_acesso_do_seu_bot'
        updater = Updater(token=token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', welcome))

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('feedback', feedback)],
            states={
                STATE1: [MessageHandler(Filters.text, inputFeedback)],
                STATE2: [MessageHandler(Filters.regex(
                    '^(Digitar novamente|Permanecer este feedback)$'), inputFeedback)]
            },
            fallbacks=[CommandHandler('cancel', cancel)]
        )
        updater.dispatcher.add_handler(conversation_handler)

        # updater.dispatcher.add_error_handler(error)
        updater.start_polling()
        print("Updater no ar: " + str(updater))
        updater.idle()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
