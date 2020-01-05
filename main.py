from telegram.ext import Updater, CommandHandler


def main():
    token = 'cole_aqui_o_token_de_acesso_do_seu_bot'
    updater = Updater(token=token, use_context=True)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()