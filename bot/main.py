import telebot
from config import Config


class BotHandler:
    def __init__(self):
        self.telegram_bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)

    def register_handlers(self):
        pass

    def start_bot(self):
        self.telegram_bot.polling()


def main():
    bot_handler = BotHandler()
    bot_handler.start_bot()

if __name__ == '__main__':
    main()