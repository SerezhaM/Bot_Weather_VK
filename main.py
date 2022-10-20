from vkbottle.bot import Bot, Message

bot = Bot(token="19836e6ac396213b8ff3588e408938558ed3fc00d5a4e9d3a76fd7dcfcd35c155caadf842df8a5d7f54b8")

@bot.on.message(text="Привет")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))

bot.run_forever()