import asyncio

from aiogram import Bot, Dispatcher, executor, types
import logging
import time
import requests
from bs4 import BeautifulSoup
import lxml
import aioschedule
from db_apple import Database
from datetime import datetime
import os


load_dotenv()

def tel_bot():

    bott = Bot(token=os.getenv('TOKEN'))
    bot = Dispatcher(bott)
    logging.basicConfig(level=logging.INFO)

    @bot.message_handler(commands=["13"])
    async def iphone(message: types.Message):
        db = Database('apple.db')
        try:
            url = 'https://lhstore.ru/product/apple-iphone-13-pro/'
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"
            }
            req = requests.get(url, headers=headers)
            src = req.text
            # print(src)
            soup = BeautifulSoup(src, 'lxml')
            price = soup.find('div', class_='summary entry-summary').find(class_='price').find('span')
            iphone13_price = db.get_13()
            text = price.text.split('₽')[0].replace('Â ', '')
            dif = int(text) - int(iphone13_price)
            db.set_13(int(text))

            if dif == 0:
                text += ' ~~~'
            elif dif > 0:
                text += f' ⬆️⬆️⬆ {dif}'
            elif dif < 0:
                text += f' ⬇️⬇⬇ {abs(dif)}'
            # print(text)
            await bott.send_message(message.chat.id, text)

        except:
            # print('no')
            await bott.send_message(message.chat.id, 'упс(')


    # @bot.message_handler(commands=["13"])
    async def iphone13():
        db = Database('apple.db')
        try:
            url = 'https://lhstore.ru/product/apple-iphone-13-pro/'
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"
            }
            req = requests.get(url, headers=headers)
            src = req.text
            # print(src)
            soup = BeautifulSoup(src, 'lxml')

            price = soup.find('div', class_='summary entry-summary').find(class_='price').find('span')
            iphone13_price = db.get_13()
            text = price.text.split('₽')[0].replace('Â ', '')
            dif = int(text) - int(iphone13_price)
            db.set_13(int(text))

            if dif == 0:
                text += ' ~~~'
            elif dif > 0:
                text += f' ⬆️⬆️⬆ {dif}'
            elif dif < 0:
                text += f' ⬇️⬇⬇ {abs(dif)}'
            #print(text)
            await bott.send_message(740124049, text)

        except:
            #print('no')
            await bott.send_message(740124049,'упс(')

    @bot.message_handler(commands=["14"])
    async def iphone():
        db = Database('apple.db')
        try:
            url = 'https://prostoreshop.ru/product/smartfon-apple-iphone-14-pro-128-gb-kosmicheskij-chernyj/'
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"
            }
            req = requests.get(url, headers=headers)
            src = req.text
            # print(src)
            soup = BeautifulSoup(src, 'lxml')

            price = soup.find('div', class_='mf-product-detail').find('div', class_='summary entry-summary').find(
                'span')
            iphone14_price = db.get_14()
            text = price.text.split(' руб.')[0].replace(' ', '')
            dif = int(text) - int(iphone14_price)
            db.set_14(int(text))

            if dif == 0:
                text += ' ~~~'
            elif dif > 0:
                text += f' ⬆️⬆️⬆️ {dif}'
            elif dif < 0:
                text += f' ⬇️⬇⬇ {abs(dif)}'
            # print(text)
            await bott.send_message(740124049, text)

        except:
            # print('no')
            await bott.send_message(740124049, 'упс(')

    # @bot.message_handler(commands=["14"])
    async def iphone14():
        db = Database('apple.db')
        try:
            url = 'https://prostoreshop.ru/product/smartfon-apple-iphone-14-pro-128-gb-kosmicheskij-chernyj/'
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"
            }
            req = requests.get(url, headers=headers)
            src = req.text
            # print(src)
            soup = BeautifulSoup(src, 'lxml')

            price = soup.find('div', class_='mf-product-detail').find('div', class_='summary entry-summary').find(
                'span')
            iphone14_price = db.get_14()
            text = price.text.split(' руб.')[0].replace(' ', '')
            dif = int(text) - int(iphone14_price)
            db.set_14(int(text))

            if dif == 0:
                text += ' ~~~'
            elif dif > 0:
                text += f' ⬆️⬆️⬆️ {dif}'
            elif dif < 0:
                text += f' ⬇️⬇⬇ {abs(dif)}'
            #print(text)
            await bott.send_message(740124049, text)

        except:
            #print('no')
            await bott.send_message(740124049, 'упс(')

    @bot.message_handler(commands=["start"])
    async def start(message: types.Message):
        await message.bot.send_message(message.chat.id, 'Запуск!')
        asyncio.create_task(scheduler())


    async def scheduler():
        #aioschedule.every().day.at("12:00").do(noon_print)
        #aioschedule.every(3).seconds.do(iphone13)
        #aioschedule.every(5).seconds.do(iphone14)
        aioschedule.every().day.at("14:23").do(iphone13)
        aioschedule.every().day.at("14:24").do(iphone14)

        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    @bot.message_handler(commands=["time"])
    async def start(message: types.Message):
        now = str(datetime.now().time())
        await message.bot.send_message(message.chat.id, now)

    executor.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    tel_bot()



