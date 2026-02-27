import logging

logger = logging.getLogger(__name__)

class MyBot:
    def __init__(self):
        pass

    def start(self):
        logger.info('Bot started')

    def stop(self):
        logger.info('Bot stopped')

if __name__ == '__main__':
    bot = MyBot()
    bot.start()