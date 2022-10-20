import vkbottle
import os
import tracemalloc
import requests_weather as rw

from vkbottle.bot import Bot, Message


tracemalloc.start()

#Подключение к тестовому сообществу
bot = Bot(token = "19836e6ac396213b8ff3588e408938558ed3fc00d5a4e9d3a76fd7dcfcd35c155caadf842df8a5d7f54b8")

@bot.on.private_message(state = None)
async def hi_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    users_message = message.text
    print(users_message)
    if "погода" in users_message.lower():
        city = users_message.split('в ')
        try:
            weather = rw.what_weather(city[1])
            await message.answer(f"{user[0].first_name}, погода в {city[1]}: \n{weather}")
        except:
            return "<ошибка – ты не ввел город>"
    else:
        return "Извини, но я пока что не понимаю тебя :("

bot.run_forever()

