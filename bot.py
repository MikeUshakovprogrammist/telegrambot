import config
import telebot
import random

class Capy:
    def __init__(self, token1, random, list1):
        self.token1 = token1
        self.random = random
        self.list1 = list1

    def run(self):
        bot = telebot.TeleBot(self.token1)
        @bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            bot.reply_to(message, 'Привет, я капибара!')


        @bot.message_handler(commands=['random'])
        def r(message):
            bot.reply_to(message, f'выпало: {self.random}')


        @bot.message_handler(commands=['info'])
        def info(message):
            bot.reply_to(message, '- команда /joke - Возвращает случайную шутку\n- команда /quote - Присылает мудрую цитату\n- команда /fact - Рассказывает интересный факт\n-команда /help /start - кто я такой\n- команда /random - Рандомная цифра.')


        @bot.message_handler(commands=['quote'])
        def quote(message):
            bot.reply_to(message, 'Даже самый маленький ребенок пройдя через боль станет взрослым.')


        @bot.message_handler(commands=['fact'])
        def fact(message):
            bot.reply_to(message, 'Капибара – самый большой грызун из всех известных.Взрослая особь может достигать в весе до 65 кг, а тело может достигать 1,35 метров в длину и 60 см в высоту.')

        
        @bot.message_handler(commands=['joke'])
        def joke(message):
            bot.reply_to(message, self.list1)

        bot.infinity_polling()

capy = Capy(token1=config.token, random=random.randint(1, 10), list1=random.choice(['Родители долго думали, чем заняться на майские праздники. Вовочка решил все за них: принес из школы кишечный вирус.', 'Сказка была такой страшной, что уже после первой главы воспитательница вывела всю группу покурить.', 'Поймал старик золотую рыбку. — Отпусти меня, старче, три желания исполню! — Зашибись! — сказал старик. И зашиблась бедная рыбка, так и не исполнив два другие желания.']))
capy.run()
