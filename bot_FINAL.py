import os
import time
import tracemalloc 

from vkbottle import BaseStateGroup, Keyboard, OpenLink,Text, GroupEventType, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Bot, Message
from pymongo import MongoClient
from random import randint 

tracemalloc.start()

# cluster = MongoClient("mongodb+srv://Drpy_test:Sfe2ld3U3n8H5hnH@cluster0.ufv8s.mongodb.net/drdata?retryWrites=true&w=majority")
# db = cluster["drdata"]
# collection = db["drcoll"]

bot = Bot(token="19836e6ac396213b8ff3588e408938558ed3fc00d5a4e9d3a76fd7dcfcd35c155caadf842df8a5d7f54b8")

class MenuState(BaseStateGroup):
    START = 1
    START_AGAIN = 2
    KONKURS = 3
    FINAL = 4
    PROF = 5
    PROF_INFO = 6
    SECRET_ROOM_1 = 7
    SECRET_ROOM_2 = 8
    SECRET_ROOM_3 = 9
    SECRET_ROOM_4 = 10
    SECRET_ROOM_5 = 11
    SECRET_SECRET_START = 12
    SECRET_SECRET_END = 13
    MAIN_LIMB = 14
    MAIN_LIMB_2 = 15
    MAIN_LIMB_3 = 16
    MAIN_LIMB_4 = 17
    MAIN_LIMB_5 = 18
    MAIN_LIMB_6 = 19
    MAIN_LIMB_7 = 20
    MAIN_LIMB_8 = 21
    MAIN_LIMB_9 = 22
    MAIN_LIMB_10 = 23
    MAIN_LIMB_11 = 24
    MAIN_LIMB_12 = 25
    MAIN_LIMB_13 = 26
    MAIN_LIMB_14 = 27
    MAIN_LIMB_15 = 28
    MAIN_LIMB_16 = 29
    MAIN_LIMB_17 = 30
    MAIN_LIMB_18 = 31
    MAIN_LIMB_19 = 32
    MAIN_LIMB_20 = 33
    MAIN_LIMB_21 = 34
    MAIN_LIMB_22 = 35
    MAIN_LIMB_23 = 36
    MAIN_LIMB_24 = 37
    MAIN_LIMB_25 = 38
    MAIN_LIMB_26 = 39
    MAIN_LIMB_27 = 40
    MAIN_LIMB_28 = 41
    MAIN_LIMB_29 = 42
    MAIN_LIMB_30 = 43
    MAIN_LIMB_31 = 44
    MAIN_LIMB_32 = 45
    MAIN_LIMB_33 = 46
    MAIN_LIMB_34 = 47
    MAIN_LIMB_35 = 48
    START_1 = 49
    SECRET_FINAL_1 = 50
    SECRET_FINAL_2 = 51
    START_HOLL = 52
    PROF_AGAIN = 53
    KONKURS_AGAIN = 54



async def check_handler(user_bd):
    key1 = 0
    key2 = 0
    key3 = 0
    key4 = 0
    key5 = 0
    key6 = 0
    if collection.count_documents({"_id": user_bd[0].id}) == 0:
        current_time = time.strftime('%d/%m/%Y %H:%M:%S')
        collection.insert_one({"_id": user_bd[0].id, "Имя": user_bd[0].first_name, "Фамилия": user_bd[0].last_name, "Ключ_1": key1, "Ключ_2": key2, "Ключ_3": key3, "Ключ_4": key4, "Ключ_5": key5, "Ключ_6": key6, "Время": current_time}) 
    else: 
        print("Данные уже есть в базе данных")



async def bd_handler(user_info, key):
    key1 = None
    key2 = None
    key3 = None
    key4 = None
    key5 = None
    key6 = None
    if key == "Здесь технологии создаются":
        key1 = key
        collection.update_one({"_id": user_info[0].id}, {"$set": {"Ключ_1": key1}})
    if key == "во благо общества":
        key2 = key
        collection.update_one({"_id": user_info[0].id}, {"$set": {"Ключ_2": key2}})
    if key == "решают сложные задачи,":
        key3 = key 
        collection.update_one({"_id": user_info[0].id}, {"$set": {"Ключ_3": key3}})
    if key == "а человек находится в":
        key4 = key 
        collection.update_one({"_id": user_info[0].id}, {"$set": {"Ключ_4": key4}})
    if key == "центре экосистемы":
        key5 = key 
        collection.update_one({"_id": user_info[0].id}, {"$set": {"Ключ_5": key5}})
    if key == "ФИНАЛ":
        key6 = key 
        collection.update_one({"_id": user_info[0].id}, {"$set": {"Ключ_6": key6}})



@bot.on.chat_message(text="/bot") #работает только если бот назначен администратором в беседе
async def chat_handler(message: Message):
    await message.answer("👋Привет всем! Я бот – Никки. \n \n Меня создал амбассадор экосистемы VK в честь дня рождения социальной сети ВКонтакте. \n \n Вы можете перейти по ссылке: https://vk.com/questbotnikki, \n написать в сообщения группы и пройти со мной интересный квест, а также выиграть призы от ВКонтакте! \n \n Советую проходить квест с компьютера :3 \n Чтобы вызвать меня снова напиши сообщение: /bot"
    )



@bot.on.chat_message(state=None)
async def chat_handler(message: Message):
    await message.answer("👋Привет всем! Я бот – Никки. \n \n Меня создал амбассадор экосистемы VK в честь дня рождения социальной сети ВКонтакте. \n \n Вы можете перейти по ссылке: https://vk.com/questbotnikki, \n написать в сообщения группы и пройти со мной интересный квест, а также выиграть призы от ВКонтакте! \n \n Советую проходить квест с компьютера :3 \n Чтобы вызвать меня снова напиши сообщение: /bot"
    )



@bot.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_join_handler(event: GroupTypes.GroupJoin):
    try:
        await bot.api.messages.send(
            peer_id=event.object.user_id,
            message="👋Привет! Я рада, что ты зашел ко мне. \n \n Знаешь, сегодня у социальной сети ВКонтакте день рождение – ей исполняется 15 лет! В честь этого, я предлагаю тебе пройти интересный квест, узнать интересные факты о профессиях ИТ-мира и выиграть призы, если сможешь отгадать все загадки! \n Напиши мне сообщение и мы начнем!",
            random_id=0
        )
    except VKAPIError(901):
        pass



@bot.on.private_message(state=[MenuState.START_AGAIN, MenuState.PROF_AGAIN, MenuState.KONKURS_AGAIN], payload=[{"cmd": "again"}, {"cmd": "konkurs_end_again"}])
async def again_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await message.answer(
        f"««МЕНЮ»» \n \n Поздравляю с успешным прохождением квеста, {user[0].first_name}! Ты всегда можешь пройти квест заново, чтобы найти все части загадки или можешь пойти отдохнуть. \n \n Выбор за тобой!",
        keyboard=(
            Keyboard()
            .add(Text("Продолжить историю...", {"cmd": "yes_again"}), color=KeyboardButtonColor.POSITIVE)
            .add(Text("Пойду отдохну...", {"cmd": "no_again"}), color=KeyboardButtonColor.NEGATIVE)
            .row()
            .add(Text("Узнать о конкурсе", {"cmd": "konkurs"}))
            .add(OpenLink("https://vk.com/topic-207666114_48032083", "Оставить отзыв"))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.START_1)



@bot.on.private_message(state=None) #Много статусов
async def start_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await message.answer(
        f"👋Привет, {user[0].first_name}! Я рада, что ты зашел ко мне. \n \n Знаешь, сегодня у социальной сети ВКонтакте день рождение – ей исполняется 15 лет! В честь этого, я предлагаю тебе пройти интересный квест, узнать интересные факты о профессиях ИТ-мира и выиграть призы, если сможешь отгадать все загадки! \n Если тебя все устраивает, тогда я бы рассказала тебе о нашем квесте. Готов?",
        keyboard=(
            Keyboard()
            .add(Text("Конечно готов!", {"cmd": "yes"}), color=KeyboardButtonColor.POSITIVE)
            .add(Text("Давай в другой раз?", {"cmd": "no"}), color=KeyboardButtonColor.NEGATIVE)
            .get_json()
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.START) #Только 1 статус



@bot.on.private_message(state=[MenuState.START, MenuState.KONKURS], payload=[{"cmd": "yes"}, {"cmd": "konkurs_end"}]) #Много статусов
async def start_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await message.answer(
        "Здорово! Прежде чем начнем прохождение, я хочу скоординировать тебя. \n \n Это квест – игра с выбором. Каждый выбор несет за собой свои проблемы или новые возможности. Приняв один выбор, ты уже не сможешь выбрать другой в рамках одного прохождения. В нашем квесте есть секреты и загадки, если хочешь узнать о них, то жми «Узнать о конкурсе» \n \n Если тебе все понятно, то может быть начнем?",
        keyboard=(
            Keyboard()
            .add(Text("Давай начнем!", {"cmd": "yes_start"}), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Узнать о конкурсе", {"cmd": "konkurs_start"}))
            .get_json()
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.START_HOLL)



@bot.on.private_message(state=MenuState.START_HOLL, payload={"cmd": "konkurs_start"})
async def konkurs_handler(message: Message):
    await message.answer(
        f"🏆Ты можешь участвовать в конкурсе, если сможешь найти ключи, собрать из них предложение и попасть в супер-секретную комнату. \n \n ЧТО ТАКОЕ КЛЮЧ? \n -Ключ обозначается звездочками(*ключ*), а также смайликом(🔑); \n \n ГДЕ ИСКАТЬ? \n -Во всем квесте спрятаны 6 ключей: \n \n 1)Один ключ находится где-то в квесте (он не спрятан); \n \n 2)Пять ключей находятся в специальных секретных комнатах, в которые можно попасть ВСЕГО ОДИН раз; \n \n 3)Все 6 ключей нужно ввести без изменений (в точности как вы их нашли) в супер-секретной комнате; \n \n 4)Все 6 ключей образуют одно предложение, которое нужно ввести в супер-секретной комнате. \n \n ПРО КОМНАТЫ \n -Попасть в каждую из комнат можно всего один раз; \n -Ты их не пропустишь, так как я скажу тебе об этом; \n -Чтобы попасть в секретную комнату нужно ввести ключевое предложение, которое будет спрятано вне квеста (Ссылка будет возле каждой секретной комнаты, поэтому не ошибетесь); \n -Ключевые предложения спрятаны в пабликах и страницах людей, которые причастны к квесту; \n -Ключевые предложения обозначены смайликом(🧷); \n -При вводе ключевого предложения, смайлик вводить НЕ НУЖНО. \n \n ПРО ПРИЗЫ И РОЗЫГРЫШ \n -Призы – это стикеры ВКонтакте; \n –В розыгрыше участвуют пользователи, кто найдет хотя бы один ключ. Чем больше ключей ты найдешь, тем выше шанс того, что ты точно получить приз! \n \n \n Более подробно про розыгрыш здесь: https://vk.com/@questbotnikki-rozygrysh-prizy-i-ostalnoe",
        keyboard=(
            Keyboard()
            .add(Text("Вернуться обратно", {"cmd": "konkurs_end"}))
            .get_json()
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.KONKURS)



@bot.on.private_message(state=MenuState.START_1, payload={"cmd": "konkurs"})
async def konkurs_handler(message: Message):
    await message.answer(
        f"🏆Ты можешь участвовать в конкурсе, если сможешь найти ключи, собрать из них предложение и попасть в супер-секретную комнату. \n \n ЧТО ТАКОЕ КЛЮЧ? \n -Ключ обозначается звездочками(*ключ*), а также смайликом(🔑); \n \n ГДЕ ИСКАТЬ? \n -Во всем квесте спрятаны 6 ключей: \n \n 1)Один ключ находится где-то в квесте (он не спрятан); \n \n 2)Пять ключей находятся в специальных секретных комнатах, в которые можно попасть ВСЕГО ОДИН раз; \n \n 3)Все 6 ключей нужно ввести без изменений (в точности как вы их нашли) в супер-секретной комнате; \n \n 4)Все 6 ключей образуют одно предложение, которое нужно ввести в супер-секретной комнате. \n \n ПРО КОМНАТЫ \n -Попасть в каждую из комнат можно всего один раз; \n -Ты их не пропустишь, так как я скажу тебе об этом; \n -Чтобы попасть в секретную комнату нужно ввести ключевое предложение, которое будет спрятано вне квеста (Ссылка будет возле каждой секретной комнаты, поэтому не ошибетесь); \n -Ключевые предложения спрятаны в пабликах и страницах людей, которые причастны к квесту; \n -Ключевые предложения обозначены смайликом(🧷); \n -При вводе ключевого предложения, смайлик вводить НЕ НУЖНО. \n \n ПРО ПРИЗЫ И РОЗЫГРЫШ \n -Призы – это стикеры ВКонтакте; \n –В розыгрыше участвуют пользователи, кто найдет хотя бы один ключ. Чем больше ключей ты найдешь, тем выше шанс того, что ты точно получить приз! \n \n \n Более подробно про розыгрыш здесь: https://vk.com/@questbotnikki-rozygrysh-prizy-i-ostalnoe",
        keyboard=(
            Keyboard()
            .add(Text("Вернуться в меню", {"cmd": "konkurs_end_again"}))
            .get_json()
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.KONKURS_AGAIN)    



#MAIN-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=[MenuState.START_HOLL, MenuState.START_1], payload=[{"cmd": "yes_start"}, {"cmd": "yes_again"}])
async def info_handler(message: Message):
    await message.answer(
        "Как и в любом другом квесте, история должна где-то начинаться. В нашем квесте, она начинается в квартире главного героя. \n \n Он – простой человек, который недавно закончил учёбу и пытается устроиться на работу. И возможно, именно сегодня ему удастся сделать это...",
        keyboard=(
            Keyboard()
            .add(Text("Начать историю", {"cmd": "start"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_2)



@bot.on.private_message(state=MenuState.MAIN_LIMB_2, payload={"cmd": "start"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Тын-тыры-тын-тын» – слышишь ты сквозь сон. \n \n «Это же будильник!» – осознаешь ты и мигом вскакиваешь. Оглядевшись и придя в себя после сна, ты наконец-то видишь мобильник и берешь его в руки.",
        keyboard=(
            Keyboard()
            .add(Text("...", {"cmd": "start_2"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_3)



@bot.on.private_message(state=MenuState.MAIN_LIMB_3, payload={"cmd": "start_2"})
async def info_item_handler(message: Message):
    await message.answer(
        "Время 8.37. Дата 10.10.2021. \n «Так рано?!» – думаешь ты, открывая почту на проверку. \n \n Не успеваешь ты отсортировать письма, как тебе прилетает уведомление: «Собеседование через 1 час». «Собеседование, точно! Как я мог забыть» – разносится в твоей голове. \n \n Нужно продумать свои действия, чтобы все успеть. Либо спокойно позавтракать и поехать в офис на такси, либо без завтрака бежать в метро. \n \n Что же выберет наш герой?",
        keyboard=(
            Keyboard()
            .add(Text("Поеду на такси", {"cmd": "taxi"}))
            .row()
            .add(Text("Поеду на метро", {"cmd": "metro"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_4)



@bot.on.private_message(state=MenuState.MAIN_LIMB_4, payload={"cmd": "taxi"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты решаешься поехать на такси и сэкономить кучу времени. \n \n Встав, позавтракав и одевшись, ты выходишь на улицу и садишься в такси. Через каких-то 20 минут ты оказываешься у здания компании. Вдох–выдох и ты входишь во внутрь. \n \n Перед тобой огромный холл, рецепция и пустота. Буквально никого нет. Хорошо, что тебе дали точный адрес с этажем и кабинетом. \n \n Можно пойти самому или остаться ждать… И как быть?",
        keyboard=(
            Keyboard()
            .add(Text("Пойти самому в кабинет", {"cmd": "taxi_go"}))
            .row()
            .add(Text("Подождать кого-нибудь на рецепции", {"cmd": "taxi_wait"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_13)   



@bot.on.private_message(state=MenuState.MAIN_LIMB_13, payload={"cmd": "taxi_wait"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Лучше подождать и дать о себе знать» – принимаешь ты решение. Устроившись поудобнее на пуфике в холле, ты остаешься ждать кого-либо. \n \n Окинув взглядом холл, ты замечаешь огромные светящиеся экраны, яркие лампы, которые освещают весь холл, и много-много растений – «Они придают этому месту живость» – мелькает в твоей голове. \n \n Все же нужно что-то делать: можно поизучать это место или бездействовать дальше. ",
        keyboard=(
            Keyboard()
            .add(Text("Подойти к рецепции", {"cmd": "recepcia"}))
            .row()
            .add(Text("Бездействовать", {"cmd": "nothing"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_13)   



#РЕЦЕПЦИЯ-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=MenuState.MAIN_LIMB_13, payload={"cmd": "recepcia"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Возможно, у стойки рецепции есть что-то» – размышляешь ты и подходишь к стойке. \n \n На ней ты находишь листки, ручки, визитки компании и какие-то документы… Твое внимание останавливается на колокольчике. ",
        keyboard=(
            Keyboard()
            .add(Text("Дзынь", {"cmd": "dzin"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_33)   



@bot.on.private_message(state=MenuState.MAIN_LIMB_33, payload={"cmd": "dzin"})
async def info_item_handler(message: Message):
    await message.answer(
        "...раздается по всему холлу. \n \n Подождав пару минут, ты понимаешь, что это не привело ни к какому результату. \n \nПеред тобой стоит выбор: написать записку, уйти и ждать звонка или залезть за стойку и поискать что-то там. Как ты поступишь?",
        keyboard=(
            Keyboard()
            .add(Text("Написать записку", {"cmd": "write"}))
            .row()
            .add(Text("Залезть за стойку", {"cmd": "stoyka"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_34)   



@bot.on.private_message(state=MenuState.MAIN_LIMB_34, payload={"cmd": "stoyka"})
async def info_item_handler(message: Message):
    await message.answer(
        "Выбор заканчивается на том, что ты уже стоишь за стойкой. \n \n «Добрый день! Вас скоро пригласят наверх, а пока выпейте чаю!» – говоришь ты, принимая роль администратора. \n \n Оглядывая рецепцию, ты находишь номер телефона и загадочную клавиатуру, провод которой уходит куда-то в пол. \n \n Что же сделать: позвонить или более внимательно изучить клавиатуру?",
        keyboard=(
            Keyboard()
            .add(Text("Изучить странную клавиатуру", {"cmd": "super_secret"}))
            .row()
            .add(Text("Позвонить по телефону", {"cmd": "phone"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_35)   



@bot.on.private_message(state=[MenuState.MAIN_LIMB_35, MenuState.SECRET_SECRET_END], payload=[{"cmd": "super_secret"}, {"cmd": "secret_away"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Решив, что телефон подождет, ты прилипаешь к клавиатуре. \n \n Изучая ее, ты понимаешь, что ей никто и никогда не пользовался. С обратной стороны обозначено, что в нее «нужно ввести 6 ключей для чего-то...» \n \n Забыв про все и нацелив свое внимание на клавиатуру, ты думаешь, что можно сюда ввести… \n \n \n 💾От разработчика: Ты нашел возможность попасть в супер-секретную комнату. Чтобы в нее попасть, тебе нужно найти 6 ключей, которые спрятаны по всему квесту (Жми на кнопку: «Узнать о конкурсе» после прохождения сюжета!). \n \n Как только соберешь их все, смело возвращайся сюда и отправляй мне (Отправить нужно все 6 ключей без изменения, в нужном порядке и одним предложением).",
        keyboard=(
            Keyboard()
            .add(Text("Все же позвонить по телефону", {"cmd": "phone"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_SECRET_START)  



#-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=MenuState.MAIN_LIMB_4, payload={"cmd": "metro"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты решаешься поехать на метро. \n \n Быстро одевшись, ты бежишь на улицу. Через 10 минут ты уже в метро. Час пути и еще через 15 минут, ты стоишь у офиса компании. \n \n «Немного опаздываю, но думаю все хорошо» Вдох–выдох и ты входишь во внутрь. \n \n Перед тобой огромный холл, рецепция и тишина. Хорошо, что тебе дали точный адрес с этажем и кабинетом. Времени и так нет, поэтому пойду сам! \n \n Забегая в лифт, ты боковым зрением замечаешь силуэт человека. Двери еще не закрылись, можно выйти из лифта или это просто глюки?",
        keyboard=(
            Keyboard()
            .add(Text("Жму на кнопку 26 этаж", {"cmd": "push_button"}))
            .row()
            .add(Text("Выскочить из лифта", {"cmd": "go_elevator"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_5)  



@bot.on.private_message(state=MenuState.MAIN_LIMB_5, payload={"cmd": "go_elevator"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты успеваешь выскочить из лифта в последний момент.  \n \n Подойдя обратно в главный холл, ты действительно обнаруживаешь человека. Это девушка, которая подошла к рецепции. Ты подходишь к ней и объясняешь свою ситуацию. После того, как ты закончил, она лишь улыбнулась и сказала подниматься на 20 этаж в 9 кабинет. Сегодня собрание, поэтому место собеседования перенесли.",
        keyboard=(
            Keyboard()
            .add(Text("Бегом на 20-й этаж", {"cmd": "go_20"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_6)  



@bot.on.private_message(state=MenuState.MAIN_LIMB_5, payload={"cmd": "push_button"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Нажав на «кнопку 26 этаж», лифт начинает свое движение. \n \n На экране высвечивается число «26» и двери лифта открываются. Ты выходишь из лифта и осматриваешься. Направо указатели «16–28», налево «1–15». Еще раз перепроверив номер кабинета, ты поворачиваешь налево. \n \n Проносясь мимо «кабинета №5», ты на секунду замираешь, т.к отчетливо слышишь звуки выстрелов. Как-быть? ",
        keyboard=(
            Keyboard()
            .add(Text("Проверить кабинет №5", {"cmd": "check_5"}))
            .row()
            .add(Text("Собеседовании важнее", {"cmd": "sobesedovanie_important"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_7) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_7, payload={"cmd": "sobesedovanie_important"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты решаешь не вникать в подробности, а скорее попасть на собеседование. \n \n «Кабинет № 9», «Кабинет № 11» и, наконец, «Кабинет № 12».Ты чуть ли не бегом влетаешь в него… \n \n На столе стоит ноутбук, на котором 2% зарядки, в кабинете пусто. Ты решаешь подойти ближе к ноутбуку и замечаешь, что там мигает сообщение. Твоя рука опускается на мышку, но, к сожалению, ноутбук выключается. Ты в пятишься назад и замираешь в растерянности. \n \n Твой паралич длился недолго. Через несколько минут твой телефон начал вибрировать…",
        keyboard=(
            Keyboard()
            .add(Text("Взять трубку", {"cmd": "phone"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_8) 



#GAME-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=MenuState.MAIN_LIMB_7, payload={"cmd": "check_5"})
async def info_item_handler(message: Message):
    await message.answer(
        "Аккуратно приоткрыв дверь в кабинет и надев на себя «супер-геройский плащ», ты оказываешься в комнате с мониторами. Уже через пару секунд, ты понимаешь, что попал в комнату разработок игр, а звуки стрельбы всего лишь из игры. Ты не спеша обследуешь комнату и обнаруживаешь человека, сидящего за компьютером и играющим в какую-то стрелялку. Перед тобой возникает выбор…",
        keyboard=(
            Keyboard()
            .add(Text("Отвлечь", {"cmd": "distract"}))
            .row()
            .add(Text("Не отвлекать", {"cmd": "not_distract"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_9) 

@bot.on.private_message(state=MenuState.MAIN_LIMB_9, payload={"cmd": "not_distract"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты – лицо непонятное, новое, еще даже не принятое на работу. Слоняться по кабинетам в компании – затея не из лучших, поэтому ты решаешь аккуратно пройти мимо загадочной персоны дальше. \n \n Пройдя в соседнюю комнату, ты оказываешься в схожем помещении. Много мониторов, компьютеров, повсюду изображения доспехов, оружия, какие-то монстры и прочее. \n \n Окинув все взглядом, ты осознаешь, что попал в самое сердце игр – место, где игры придумывают. Ты вспоминаешь, что в средней школе тоже пытался создать игру, но идея быстро погибла",
        keyboard=(
            Keyboard()
            .add(Text("Изучить новую комнату", {"cmd": "explore"}))
            .row()
            .add(Text("Уйти", {"cmd": "go_away"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_10) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_10, payload={"cmd": "explore"})
async def info_item_handler(message: Message):
    await message.answer(
        "Любопытство берет вверх, и ты приближаешься к изображениям и компьютерам. Просмотрев все вариации магического доспеха на эльфа-защитника, ты переключаешься на холодное оружие: мечи, клинки, сабли… \n \n Тебя это не особо впечатляет и заметив открытый 3D редактор на соседнем компьютере, ты решаешься попробовать создать свое видение доспехов и оружия. \n \n Спустя пару часов ты слышишь шуршание из соседней комнаты и шаги в твою сторону. Ты совсем забыл про того мужчину!",
        keyboard=(
            Keyboard()
            .add(Text("Спрятаться", {"cmd": "hide_and_seek"}))
            .row()
            .add(Text("Ничего не делать", {"cmd": "nothing_1"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_11) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_9, payload={"cmd": "distract"})
async def info_item_handler(message: Message):
    await message.answer(
        "Простояв и понаблюдав в монитор, ты наконец решаешь потревожить загадочную персону. Аккуратно дотронувшись до плеча, персона вздрагивает и резко оборачивается на тебя. \n \n «Зачем так пугать?! И ты кто?» – спрашивает он. Ты рассказываешь ему свою историю, что по ошибке зашел сюда и опоздал на собеседование. Вместо упреков или недовольства, мужчина предлагает тебе присоединиться к нему и попробовать найти баги в игре. \n \n Согласишься ли ты помочь ему или самое время уйти?",
        keyboard=(
            Keyboard()
            .add(Text("Я с удовольствием помогу", {"cmd": "help"}))
            .row()
            .add(Text("Лучше уйти", {"cmd": "go_away"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_12) 



#NOT WAIT-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=MenuState.MAIN_LIMB_13, payload={"cmd": "taxi_go"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Прождать можно очень долго, а у меня собеседование через 10 минут» – думаешь ты, направляясь к холлу с лифтами. \n \n Нажав на кнопку, позади тебя открывается лифт, и ты входишь в него. Перед тобой множество кнопок. Каждая кнопка – это этаж. \n Тебе, конечно же, прислали номер этажа и номер кабинета, чтобы не потеряться. Или ты и так все помнишь?",
        keyboard=(
            Keyboard()
            .add(Text("Перепроверить этаж", {"cmd": "recheck"}))
            .row()
            .add(Text("Я точно знаю, что не ошибусь", {"cmd": "not_recheck"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_14) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_14, payload={"cmd": "recheck"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Лучше перепроверю» – говоришь ты про себя, доставая и открывая сообщение. «26 этаж, кабинет №12» гласит сообщение. \n \n Нажав кнопку 26, лифт начинает свое движение. На экране высвечивается число «26», и двери лифта открываются.  \n \n Ты выходишь из лифта и осматриваешься. Время еще есть, поэтому можно осмотреться или нужно пойти в кабинет?",
        keyboard=(
            Keyboard()
            .add(Text("Нужно пойти в кабинет", {"cmd": "go_in"}))
            .row()
            .add(Text("Можно осмотреться и пройтись", {"cmd": "go_look"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_23) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_23, payload={"cmd": "go_look"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты идешь в противоположную сторону от нужного кабинета и попадаешь в другой отдел, сам того не понимая. Другие цвета, таблички – все по-другому. Кажется, что тут все время кипит работа, даже сейчас, когда никого нет… \n \n Вдруг из-за угла до тебя доносятся звуки речи. \n \n Времени прошло достаточно, а значит, собеседование скоро начнется. Что же делать?",
        keyboard=(
            Keyboard()
            .add(Text("Проверить странные звуки", {"cmd": "strange"}))
            .row()
            .add(Text("Поспешить в кабинет", {"cmd": "go_in_2"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_28) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_28, payload={"cmd": "strange"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Ничего страшного не произойдет, если я проверю, что там» – решаешь ты и поворачиваешь за угол. \n \n Речь становится более отчетливой, и ты находишь ее источник. Это не человек, как ты предполагал, а колонка. \n \n «Наверное, это колонка с искусственным интеллектом…» – вслух говоришь ты. \n \n Через секунду ты слышишь ответ: \n «Да, я умная колонка Маруся!»",
        keyboard=(
            Keyboard()
            .add(Text("Подойти к колонке", {"cmd": "kolonka"}))
            .row()
            .add(Text("Пойти обратно", {"cmd": "go_away_kolonka"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_29) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_29, payload={"cmd": "kolonka"})
async def info_item_handler(message: Message):
    await message.answer(
        "Приблизившись к колонке, ты рассматриваешь ее. Она лишь моргает своими цифровыми глазами. \n \n Ты решаешь проверить, сможет ли Маруся отреагировать на твои движения, поэтому начинаешь махать ей, прыгать и хлопать в ладоши. За все эти выходки колонка успела дважды моргнуть и показать время. \n \n «Ты можешь реагировать на мои движения?» – спрашиваешь ты у колонки. \n «К сожалению, я не обладаю такими навыками на данный момент, но Вы можете научить меня» \n \n Можно еще задержаться и научить Марусю новому или посмотреть еще на ее навыки. Нужно выбрать что-то одно…",
        keyboard=(
            Keyboard()
            .add(Text("Попытаться обучить", {"cmd": "learn"}))
            .row()
            .add(Text("Посмотреть на все навыки колонки", {"cmd": "see_all"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_30) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_29, payload={"cmd": "go_away_kolonka"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ни сколько не удивившись ответу, ты шагаешь прочь от колонки. Но, не дойдя до угла, ты оборачиваешь и спрашиваешь у «Умной коробочки» – «Маруся, а скажи, как можно попасть к вам в команду, но без собеседования?» \n \n Выждав паузу, колонка выдала ответ – «Вы можете попасть к нам в команду очень просто, но это будет не легко. Вам нужно всего лишь обратиться в UX отдел, и Вы сможете работать со мной!»",
        keyboard=(
            Keyboard()
            .add(Text("Спросить номер UX отдела у колонки", {"cmd": "say"}))
            .row()
            .add(Text("Поблагодарить колонку и уйти", {"cmd": "thank"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_32) 



@bot.on.private_message(state=[MenuState.MAIN_LIMB_30, MenuState.SECRET_ROOM_1], payload=[{"cmd": "learn"}, {"cmd": "secret_away"}])
async def info_item_handler(message: Message):
    await message.answer(
        "«Маруся, а как тебя можно обучить?» – спрашиваешь ты, на что колонка не реагирует, а на ее экране появляется стрелка направо. Ты смотришь в сторону и замечаешь, что в комнате, которую ты раньше не замечал, зажегся свет и компьютер. \n \n Ты воспринимаешь этот жест как приглашение и усаживаешься за ЭВМ. Код, код и еще раз код. Сплошные нолики и единички. Беготня вокруг колонки. Ты тратишь на эту очень много времени, но в конце концов колонка начинает реагировать на твои хлопки, махи руками и прыжки. \n \n \n 💾От разработчика: Ты можешь не выбирать ответ, а ввести ключевое предложение, тогда ты получишь одну часть секретного ключа. Вводить предложение нужно без смайлика(🧷). Ищи ключевое предложение тут: https://vk.com/serezhamashoha",
        keyboard=(
            Keyboard()
            .add(Text("Помахать Маруси на прощание", {"cmd": "marysa_learn_1"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_31) 



@bot.on.private_message(state=[MenuState.MAIN_LIMB_23, MenuState.MAIN_LIMB_28], payload=[{"cmd": "go_in"}, {"cmd": "go_in_2"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Кабинет № 9», «Кабинет № 11» и наконец «Кабинет № 12». \n \n Замерев около него, ты собираешься с мыслями. Вероятно, это тот самый момент истины, думаешь ты. Вдруг ты осознаешь, что за все время хождения по офису компании, ты не встретил никого. \n \n «Хмм, странно, но сегодня же воскресенье» – обнадеживаешь себя ты и открываешь дверь в кабинет. И тут тоже пусто, однако ты замечаешь ноутбук и уведомление на нем. \n \n Как быть?",
        keyboard=(
            Keyboard()
            .add(Text("Изучить сообщение", {"cmd": "look_message"}))
            .row()
            .add(Text("Меня это не касается", {"cmd": "not_look_message"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_24) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_24, payload={"cmd": "look_message"})
async def info_item_handler(message: Message):
    await message.answer(
        "Подойдя к ноутбуку и пошевелив мышкой, ты читаешь сообщение: «Сегодня День Рождения ВКонтакте! Нужно что-то сделать для всех пользователей социальной сети! Пришли мне готовый проект к 11.00» \n \n Время 10.00. Зарядка 20%. Если не рискнуть и не помочь, то может случиться катастрофа, или оно мне и не нужно?",
        keyboard=(
            Keyboard()
            .add(Text("Рискнуть", {"cmd": "risk"}))
            .row()
            .add(Text("Ничего не делать", {"cmd": "nothing_2"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_26) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_26, payload={"cmd": "risk"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Хуже уже не будет» – решаешь ты и включаешь редактор кода. Вспоминаешь свои знания по «Python», «C++» и начинаешь писать квест-бота. \n \n У тебя выходит очень быстро, и ты справляешься за 57 минут. Минута на отправку сообщения неизвестному, и ноут гаснет. \n \n Ты слышишь шаги…",
        keyboard=(
            Keyboard()
            .add(Text("Надеяться на лучшее", {"cmd": "hope"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_27) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_24, payload={"cmd": "not_look_message"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Я пришел проходить собеседование, а не лазить по чужим компьютерам. Лучше сяду и буду ждать, когда ко мне кто-нибудь придет» – решаешь ты. \n \n Аккуратно отодвинув стул, ты садишься и смотришь на плакаты в офисе. Практически на всех плакатах есть фраза 🔑*все_это_про_MailRuGroup*. Это ты находишь любопытным и решаешь запомнить. \n \n Твоя фантазия охватывает тебя, и ты засыпаешь…",
        keyboard=(
            Keyboard()
            .add(Text("Zzz", {"cmd": "zzz"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_25) 



#ДИЗАЙН--------------------------------------------
@bot.on.private_message(state=MenuState.MAIN_LIMB_14, payload={"cmd": "not_recheck"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Я все помню, я уверен в себе» – говоришь ты про себя и нажимаешь на «25 этаж». Лифт начинает подъем. На экране высвечивается число «25», и двери лифта открываются. \n \n Ты выходишь из лифта и осматриваешься: с одной стороны все темное и серое, с другой – белое и светлое. «Прямо как в звездных войнах!» – подмечаешь ты. \n \n Твой внутренний Йода задает тебе вопрос. Какую стороны примешь ты, падаван?",
        keyboard=(
            Keyboard()
            .add(Text("Светлая сторона – я джедай", {"cmd": "light"}))
            .row()
            .add(Text("Темная стороная – я ситх", {"cmd": "dark"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_15) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_15, payload={"cmd": "light"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты выбираешь светлую сторону и идешь по ней. \n \n Пройдя кабинеты, ты попадешь в холл с компьютерами и мини-выставкой. Подойдя к ней, ты видишь различные варианты дизайнов. Есть одно но – они все белые и супер светлые. \n \n «Тут нужно чуть темнее, а тут чуть белее» – высказываешь ты свои замечания. Ты останавливаешься возле последней работы. Тебя в ней что-то привлекло и оттолкнуло одновременно. \n \n У тебя появляется желание поучаствовать в этой выставке, или лучше пойти далее?",
        keyboard=(
            Keyboard()
            .add(Text("Поучаствовать", {"cmd": "light_explore"}))
            .row()
            .add(Text("Пойти далее", {"cmd": "light_go"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_20) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_20, payload={"cmd": "light_explore"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты садишься за один из компьютеров в холле, открываешь редактор и начинаешь творить. Ты забываешь про собеседование, офис, отсутствие людей, мир… \n \n Спустя 3 часа ты приходишь в себя. Перед тобой на мониторе совершенный дизайн. В нем идеально все: гармония цвета, геометрия фигур, переливания и сочетания палитры. \n \n Ты печатаешь свой дизайн и вешаешь его рядом с остальными. После этого решаешь просто уйти…",
        keyboard=(
            Keyboard()
            .add(Text("Пойти к выходу", {"cmd": "light_explore_go"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_22) 



@bot.on.private_message(state=[MenuState.MAIN_LIMB_20, MenuState.SECRET_ROOM_3], payload=[{"cmd": "light_go"}, {"cmd": "secret_away"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Наверняка это желание мимолетное, решаешь ты и двигаешься дальше. \n \n Коридор заканчивается поворотом направо. Зайдя за угол, ты видишь слово «EXIT» и пожарную лестницу. \n \n  Простояв пару минут возле нее, ты решаешь повернуть назад и пойти прочь. \n \n \n 💾От разработчика: Ты можешь не выбирать ответ, а ввести ключевое предложение, тогда ты получишь одну часть секретного ключа. Вводить предложение нужно без смайлика(🧷). Ищи ключевое предложение тут: https://vk.com/theacademy",
        keyboard=(
            Keyboard()
            .add(Text("Уйти", {"cmd": "light_go_go"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_21) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_15, payload={"cmd": "dark"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты выбираешь темную сторону и идешь по ней. \n \n Проходя кабинеты, ты задерживаешься возле одного: «Кабинет оценки дизайна», дверь приоткрыта. Ты заглядываешь вовнутрь. Никого нет, только включенные компьютеры и много бегущих строк. \n \n Любопытно почитать, что там написано. Или лучше пойти далее?",
        keyboard=(
            Keyboard()
            .add(Text("Зайти в кабинет", {"cmd": "dark_in"}))
            .row()
            .add(Text("Пойти далее", {"cmd": "dark_go"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_16) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_16, payload={"cmd": "dark_in"})
async def info_item_handler(message: Message):
    await message.answer(
        "Любопытство берет вверх и ты оказываешься у мониторов. \n \n Оказывается, это отзывы людей о дизайне в реальном времени. Рядом на мониторе открыт чей-то дизайн. Ты в считаные секунды понимаешь, что можно изменить дизайн и сразу получить отзыв. Все это в реальном времени. \n \n Тебя охватывают две мысли: изменить готовый дизайн или нарисовать свой с нуля. Что же выбрать?",
        keyboard=(
            Keyboard()
            .add(Text("Нарисовать свой", {"cmd": "dark_me"}))
            .row()
            .add(Text("Изменить предыдущий", {"cmd": "dark_in_go"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_17) 



@bot.on.private_message(state=[MenuState.MAIN_LIMB_17, MenuState.SECRET_ROOM_5], payload=[{"cmd": "dark_in_go"}, {"cmd": "secret_away"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Времени немного, поэтому попробую изменить готовое. Ты садишься за монитор и видоизменяешь предыдущий дизайн. \n \n Выходит коряво, ты часто путаешься и ошибаешься. Приходится повторять много однотипных действий: смена шрифта, редактирование геометрии, изменение цвета. \n \n В конечном итоге у тебя получается неплохой дизайн. Даже многим пользователям он понравился, если судить по цифрам.\n \n \n 💾От разработчика: Ты можешь не выбирать ответ, а ввести ключевое предложение, тогда ты получишь одну часть секретного ключа. Вводить предложение нужно без смайлика(🧷). Ищи ключевое предложение тут: https://vk.com/mr.g0rod",
        keyboard=(
            Keyboard()
            .add(Text("Понаблюдать за отзывами", {"cmd": "dark_komment"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_19) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_17, payload={"cmd": "dark_me"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Хуже уже не будет» – говоришь ты и садишься за монитор. \n \n Как скульптор начинает творить свои шедевры, так и ты начинаешь создавать новый дизайн. Это темный дизайн, со своими особенностями, с острыми фигурами и космическими переливаниями оттенков. ",
        keyboard=(
            Keyboard()
            .add(Text("Творить", {"cmd": "dark_me_draw"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.MAIN_LIMB_18) 



#FINAL-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=MenuState.MAIN_LIMB_13, payload={"cmd": "nothing"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты не знаешь, сколько проходит времени, но явно много. Никого так и не было. «Может быть, сегодня они не работают? И мне по ошибке сказали приезжать сегодня» – думаешь ты, встаешь и направляешься к выходу. \n \n «Лучше приеду на буднях и узнаю, как и чего» \n \n Ты выходишь из компании, так и не побывав в ней. Собеседование не состоялось!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL)   



@bot.on.private_message(state=MenuState.MAIN_LIMB_34, payload={"cmd": "write"})
async def info_item_handler(message: Message):
    await message.answer(
        "«…-34-56 перезвоните, пожалуйста» – заканчиваешь ты писать записку. Кладешь ее на стойку и направляешься к выходу. \n \n Ты выходишь из компании, так в ней и не побывав. Собеседование не состоялось!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL)   



@bot.on.private_message(state=[MenuState.MAIN_LIMB_35, MenuState.SECRET_SECRET_START], payload={"cmd": "phone"})
async def info_item_handler(message: Message):
    await message.answer(
        "Взяв трубку, набрав телефон и дождавшись гудков, ты направляешься к пуфикам. После 7 гудков, трубку берет девушка и слушает тебя. Ты сообщаешь ей о том, что сегодня у тебя должно быть собеседование, но в компании пусто. От нее ты узнаешь, что все на совещании и сегодня ничего не получится провести. Она говорит, что тебе нужно прийти в офис завтра. \n \n  Завершив звонок, ты выходишь из офиса. Собеседование перенесено!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL)  



@bot.on.private_message(state=MenuState.MAIN_LIMB_6, payload={"cmd": "go_20"})
async def info_item_handler(message: Message):
    await message.answer(
        "20 этаж, «Кабинет №9». Ты заходишь внутрь. \n \n Там сидит мужчина и девушка. Они представляются менеджерами и предлагают начать собеседование. Тебе задают вопросы про веб-разработку, программирование, верстку… \n \n Спустя 2 часа, менеджер, подходит к тебе и жмет руку: «Поздравляю, вы приняты к нам!» \n \n Ты выходишь из кабинета и направляешься к выходу. Собеседование прошло успешно и тебя взяли!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL)  



@bot.on.private_message(state=MenuState.MAIN_LIMB_8, payload={"cmd": "phone"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Алле…» – в растерянности говоришь ты в трубку. \n \n С другого конца вещает женский голос. Он объясняет, что в связи с проблемами и трудностями все сотрудники были на собеседовании, поэтому собеседование провести никто не смог. Извинившись и сказав, приходить завтра она повесила трубку. \n \n Простояв еще немного и придя в себя, ты направился поскорее к выходу, пока тебя никто не увидел здесь. Собеседование перенесено!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=[MenuState.MAIN_LIMB_11, MenuState.SECRET_ROOM_2], payload=[{"cmd": "hide_and_seek"}, {"cmd": "secret_away"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Тебя посещает мысль «Спрятаться». За считанные секунды ты прикидываешь места: под столом, за вешалкой, встать как манекен посередине комнаты… Твои мысли разрушает тот самый мужчина, который уже успел подойти к тебе.  \n \n Он устало глядит на тебя, хочет что-то сказать, но переводит взгляд на монитор позади тебя. Пауза, которая длится минуту и дальше вопросы: «Что и как? Кто и почему?» \n \n Ты рассказываешь ему свою историю. Он качает головой, но все же улыбается… \n \n Спустя 10 минут диалога с ним, ты выходишь из кабинета и направляешься к выходу. Ему понравились твои рисунки, и он предложил пройти стажировку в компании! \n \n \n 💾От разработчика: Ты можешь не выбирать ответ, а ввести ключевое предложение, тогда ты получишь одну часть секретного ключа. Вводить предложение нужно без смайлика(🧷). Ищи ключевое предложение тут: https://vk.com/ranepa_mrg",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_FINAL_1) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_11, payload={"cmd": "nothing_1"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Я не ребенок и прятаться точно не буду» – решаешь ты и просто встаешь из-за стола, готовясь оправдываться. В комнату заходит мужчина, оглядывает тебя, потом монитор позади тебя. После этого пауза, которая длится минуту и дальше вопросы: «Что и как? Кто и почему?» \n \n Ты рассказываешь ему свою историю. Он качает головой, но все же улыбается… \n \n Спустя 10 минут диалога с ним, ты выходишь из кабинета и направляешься к выходу. Ему понравились твои рисунки и он предложил пройти стажировку в компании!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=[MenuState.MAIN_LIMB_12, MenuState.MAIN_LIMB_10, MenuState.SECRET_ROOM_4], payload=[{"cmd": "go_away"}, {"cmd": "secret_away"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Неуверенно качнув головой и сделав пару шагов назад, ты понимаешь, что игры – это не твое и они далеко в прошлом. \n \n Нужно было идти на собеседование, а не слоняться по офису… С надеждой, что еще можно пройти собеседование, ты отправляешься в «Кабинет №12». Открыв дверь, ты обнаруживаешь только выключенный ноутбук. \n \n Развернувшись, ты шагаешь к выходу. К сожалению, ты упустил свои возможности. \n \n \n 💾От разработчика: Ты можешь не выбирать ответ, а ввести ключевое предложение, тогда ты получишь одну часть секретного ключа. Вводить предложение нужно без смайлика(🧷). Ищи ключевое предложение тут: https://vk.com/pa_today",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_FINAL_2) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_12, payload={"cmd": "help"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты уверенно качаешь головой и прыгаешь в соседнее кресло. «Это онлайн стрелялка, твоя задача найти все невидимые текстуры на новой карте, которая пока что на альфа-тестировании» – говорит тебе твой оппонент.  \n \n Проходит пара часов, и ты встаешь из-за компьютера. «Все текстуры найдены и отмечены» – сообщаешь ты рядом сидящему мужчине: «Ты быстро справился! Ты говорил, что пришел на собеседование… Считай, что ты его только что прошел! Поздравляю с вступлением в штат тестировщиков!»  \n \n Ты выходишь из кабинета и удивленный направляешься к выходу. Тебя взяли на работу, хотя не так как ты предполагал.",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_30, payload={"cmd": "see_all"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты не решаешься научить Марусю новому, а решаешь поиграть с ней. Колонка рассказывает тебе о своих возможностях, читает сказки, включает музыку и еще много чего. \n \n В конечном итоге тебе это надоедает и ты решаешь уйти. Поблагодарив колонку и попрощавшись с ней, ты направляешься к лифтам. \n \n Ты не обращаешь внимания на указатели и не вспоминаешь о собеседовании, на которое ты так и не явился. Ты просто уезжаешь вниз. \n \n На первом этаже, ты направляешься к выходу. Собеседование не состоялось!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_31, payload={"cmd": "marysa_learn_1"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты решаешь, что и так задержался тут, поэтому нужно уходить. Окинув взглядом колонку в крайний раз, ты машешь ей рукой и делаешь пару шагов от колонки. \n \n «Спасибо, что научили меня новому! Если Вам и дальше хочется работать со мной, то вы можете прийти завтра и поговорить с моим создателем. Я уже уведомила его, и он ответил, что будет рад вас видеть!» – ответила Маруся. \n \n Постояв несколько минут в шоке, ты направляешься к выходу. Ты не попал на собеседование, зато попал в компанию!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_32, payload={"cmd": "say"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Вы можете сделать все через меня и оставить заявку. Внимание, Ваша заявка будет рассмотрена в течение двух календарных дней. Оставить заявку?» \n \n «Да» – отвечаешь ты и начинаешь диктовать свои данные колонке. \n \n Спустя 5 минут, после того как заявка была отправлена, ты направляешься к выходу. Собеседование не пройдено, зато есть шанс попасть в UX отдел!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_32, payload={"cmd": "thank"})
async def info_item_handler(message: Message):
    await message.answer(
        "Поблагодарив Марусю, ты покидаешь это место. Дойдя обратно до лобби с лифтам и увидя указатели «1–15», ты вспоминаешь о не состоявшемся собеседовании. «Надеюсь, что все будет хорошо…» – говоришь ты вслух и вызываешь лифт. \n \n Двери лифта открываются. В кабине стоят двое: мужчина и женщина. Они кидают на вас взгляд, выходят и жестом показывают идти с ними. Вы втроем доходите до «Кабинета №9», заходите внутрь, и начинается собеседование. \n \n Через 2 часа ты выходишь и направляешься к выходу. Собеседование прошло неидеально, но тем не менее тебя взяли на испытательный срок!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_27, payload={"cmd": "hope"})
async def info_item_handler(message: Message):
    await message.answer(
        "В комнату заходит девушка, с которой ты должен был разговаривать. Она окидывает взглядом тебя, потом переводит его на темный экран ноутбука. Подойдя к нему и включив, она читает сообщение: «Все супер! Вовремя скинули мне этот классный проект!» \n \n «Твоих рук дело?» – спрашивает она тебя. Ты киваешь головой. «Ну, что же, конечно, плохо, что ты без спроса ходил по офису, залез в рабочий ноутбук… Но тем не менее ты спас день рождения, а значит, добро пожаловать в команду!» \n \n Ты выходишь из кабинета и радостный направляешься к выходу. Ты спас день рождение ВК и тебя приняли!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_26, payload={"cmd": "nothing_2"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты решаешь, что наглости достаточно. Залезть в рабочий компьютер, ходить по офису одному… \n \n Ты не успеваешь закончить свои мысли, потому что в кабинет влетает девушка и подбегает к ноутбуку. Хватаясь за голову, она начинает звонить кому-то, говорить что-то сделать. После этого обращается к тебе и говорит, что сегодня провести собеседование не получится, т.к есть другие проблемы.  \n \n Ты выходишь из кабинета и направляешься к выходу. Собеседование не состоялось!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_25, payload={"cmd": "zzz"})
async def info_item_handler(message: Message):
    await message.answer(
        "Просыпаешься ты от того, что тебя тормошат рукой. Придя в себя, ты видишь девушку, с которой общался по поводу собеседования. Она извиняется за опоздание и говорит, что нужно было ей позвонить. Начинается собеседование.\n \n Спустя полтора часа, ты выходишь из кабинета и радостный направляешься к выходу. Ты принят! Жаль, что ты так и не узнаешь, что было в том сообщении…",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_22, payload={"cmd": "light_explore_go"})
async def info_item_handler(message: Message):
    await message.answer(
        "Но это сделать не удается, потому что позади тебя оказывается фигура. Это женщина, лет 40. Она внимательно смотрит на твой дизайн. \n \n Ты решаешь продолжить свой путь на выход, но она поворачивается к тебе и начинает говорить. \n \n Она узнает, когда и где ты сделал этот дизайн, где учился… \n \n Через 30 минут разговоров, ты направляешься к выходу. Тебе предложили место дизайнера в компании!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_21, payload={"cmd": "light_go_go"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты все также одиноко проходишь все кабинеты, спускаешься на лифте, проходишь через молчаливый холл и, наконец, попадаешь на улицу. \n \n «Может, это и к лучшему, что я не пошел на собеседование?» – размышляешь ты и направляешься домой…",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_16, payload={"cmd": "dark_go"})
async def info_item_handler(message: Message):
    await message.answer(
        "«Лучше не лезть куда не нужно» – решаешь ты и продолжаешь свое движение по пустому офису. Пройдя до конца и завернув за угол, ты оказываешь в холле и видишь человека! Он тоже замечает тебя и зовет рукой. Ты садишься возле него. Это оказывается главный дизайнер. \n \n Рассказав ему свою историю, ты узнаешь, что, оказывается, все сотрудники были на совещании. Ты говоришь ему, что пропустил собеседование… Немного помолчав, дизайнер сообщает тебе, что он предупредит и поговорит с коллегой и попросит перенести собеседование на следующий день. \n \n Ты выходишь из холла и направляешься к выходу. Нужно готовиться к завтрашнему собеседованию!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=MenuState.MAIN_LIMB_19, payload={"cmd": "dark_komment"})
async def info_item_handler(message: Message):
    await message.answer(
        "Убедившись, что цифры и отзывы не врут, ты встаешь из-за стола и выходишь в коридор. Там ты сталкиваешься с мужчиной, который явно бежал в этот кабинет. Он молниеносно окидывает тебя взглядом и пытается что-то сказать, но бег дал о себе знать. Переведя дыхание и придя в себя от бега, он начинает разговаривать с тобой. \n \n Диалог идеи о дизайне, о тебе, о твоей истории и будущем. В итоге ты освобождаешься от диалога и направляешься к выходу со слабой улыбкой. Собеседование не состоялось, зато тебе предложили стажировку в качестве дизайнера!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 


@bot.on.private_message(state=MenuState.MAIN_LIMB_18, payload={"cmd": "dark_me_draw"})
async def info_item_handler(message: Message):
    await message.answer(
        "Ты заканчиваешь работу и видишь положительные отзывы людей. Твой дизайн понравился! Вдруг откуда-то к тебе в кабинет влетает мужчина и смотрит на тебя. \n \n «ТЫ!» – говорит он тебе. От небольшого испуга, ты вжимаешься в кресло. «Ты молодец! Ты сделал то, что не могла сделать команда на протяжении 20 лет! Присоединяйся к нам в команду!» \n \n Ты выходишь из кабинета и радостный направляешься к выходу. Не такое собеседование ты ожидал, но зато ты принят!",
        keyboard=(
            Keyboard()
            .add(Text("Финал!", {"cmd": "all_final"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.FINAL) 



@bot.on.private_message(state=[MenuState.FINAL, MenuState.SECRET_FINAL_1, MenuState.SECRET_FINAL_2, MenuState.PROF_INFO], payload=[{"cmd": "all_final"},{"cmd": "prof_back"}])
async def info_item_handler(message: Message):
    await message.answer(
        "Спасибо за прохождение! Если хочешь узнать больше об ИТ-мире, то смело переходи сюда: https://vk.com/mrgforedu \n \n Кстати, этот тест был создан амбассадором экосистемы VK из РАНХиГС 😉",
        keyboard=(
            Keyboard()
            .add(Text("Узнать о профессии", {"cmd": "prof"}))
            .add(Text("Далее", {"cmd": "again"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.START_AGAIN)     



#INFORMATION-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=[MenuState.START_AGAIN, MenuState.PROF_AGAIN], payload=[{"cmd": "prof"}, {"cmd": "prof_end"}])
async def info_item_handler(message: Message):
    await message.answer(
        "В этом квесте было использовано много профессий. Мы собрали интересные факты для тебя здесь: \n \n 1. Инженер по тестированию мобильных приложений; \n \n 2. UX Исследователь; \n \n 3. Пиарщик; \n \n 4. Data Scientist; \n \n 5. DevOps Инженер; \n \n 6. PHP Developer; \n \n 7. Дизайнер. ",
        keyboard=(
            Keyboard()
            .add(Text("1", {"cmd": "prof_1"}))
            .add(Text("2", {"cmd": "prof_2"}))
            .add(Text("3", {"cmd": "prof_3"}))
            .add(Text("4", {"cmd": "prof_4"}))
            .row()
            .add(Text("5", {"cmd": "prof_5"}))
            .add(Text("6", {"cmd": "prof_6"}))
            .add(Text("7", {"cmd": "prof_7"}))
            .add(Text("Назад", {"cmd": "prof_back"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_INFO)   



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_1"})
async def end_handler(message: Message):
    await message.answer(
        "Инженер по тестированию мобильных приложений:\n \n Профессия «тестировщик» появилась недавно – около 10 лет назад, когда создание программного обеспечения перестало быть занятием избранных и превратилось в массовую индустрию. Первоначально разработчики самостоятельно проверяли выпускаемый продукт или просили родственников и знакомых найти погрешности в тестируемой версии программы. Однако в первом случае инерция мышления человека, совмещающего функцию автора и контролера, мешала выявить все недочеты и ошибки. Кроме того, процесс поверки отнимал много времени. Во втором случае отсутствие навыков у случайных тестировщиков не давало возможности проверить софт со всех сторон. Так на IT-рынке возникла потребность в специалистах, которые знали, как проводить тест ПО, чтобы процесс обнаружения ошибок стал системным и многоплановым. Вскоре тестировщики стали связующим и контрольным звеном между нуждами потребителя и ИТ-продуктом, транслируя бизнес-цели программистам. В настоящее время в некоторых проектах они даже имеют право блокировать версию софта, если она кажется им «сырой».",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),     
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN) 



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_2"})
async def end_handler(message: Message):
    await message.answer("UX Исследователь: \n \n В 1993 Д. Норман ввел понятие «пользовательский опыт» для своей команды в Apple Computer. Но сама сфера старше этого термина.  Сложно провести границу между так называемым человеческим фактором и тем, что мы называем пользовательским опытом, имея в виду дизайн интерактивных систем, ориентированный на человека.Bell Labs были одними из пионеров, сделавшими такой переход: они наняли психолога, Д.Е. Карлина, для разработки дизайна телефона в 1945 г. К 1950-м Bell Labs совершенно точно занимались UX, в частности, в работе над дизайном кнопочной клавиатуры с тональным набором. К 1990-му году, помимо Bell Communications Research действовало уже несколько компаний, делающих потрясающую UX работу, но эпизод с Bell Labs показателен и их можно признать командой номер 1 в мире. Опять-таки, они показали существенное превосходство раннего старта.",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN) 



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_3"})
async def end_handler(message: Message):
    await message.answer("Пиарщик: \n \n Принято считать, что термин «public relations» родился в Америке в 1807 году, когда третий президент Томас Джефферсон в черновике своего «Седьмого обращения к конгрессу» заменил выражение «состояние мысли» на «общественные отношения». Существует версия и о том, что одним из первых словосочетание «public relations» пустил в оборот юрист Дорман Итон в 1882 году, призывая выпускников Йельского университета посвятить себя служению общественному благу. История отечественных связей с общественностью насчитывает чуть более десяти лет. Большинство исследователей сходятся во мнении, PR – деятельность зародилась в России в конце 80-х годов, а как самостоятельная форма деловой активности кристаллизуется во второй половине 1990 – начале 1991 года.",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN) 



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_4"})
async def end_handler(message: Message):
    await message.answer("Data Scientist:  \n \n Data Science – это наука о данных, объединяющая разные области знаний: информатику, математику и системный анализ. \n \n Наука о данных зародилась намного раньше, во второй половине 20-го века. Первое упоминание этого понятия датируется 1974 годом, когда вышла книга Петера Наура. В этой публикации Data Science определяется как дисциплина по изучению жизненного цикла цифровых данных, от момента их появления до преобразования и использования в других областях знаний. Тем не менее, широкое употребление этот термин получил лишь в 1990-е годы, а общепризнанным стал только в начале 2000-х. В частности, в 2002 году междисциплинарный Комитет по данным для науки и техники начал выпускать журнала CODATA Data Science Journal, а в январе 2003 года вышел первый номер The Journal of Data Science Колумбийского университета.",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN) 



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_5"})
async def end_handler(message: Message):
    await message.answer("DevOps Инженер: \n \n DevOps движение возникло в 2009 году и было призвано решить проблемы взаимодействия команд разработки и эксплуатации программных продуктов. Именно в 2009 году Патрик Дебуа впервые решает создать конференцию одновременно и для «dev», и для «ops». Он называет её DevOpsDays. После завершения конференции ее участники продолжили обсуждать поднятые темы в Твиттере, где название мероприятия сократилось до хэштега #DevOps. А в итоге слово, стихийно возникшее как хэштег, прижилось настолько, что сегодня гугл находит его на миллионах страниц. Так что этим названием мы обязаны Патрику, хотя сам он совершенно не ожидал такого эффекта.",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN)   



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_6"})
async def end_handler(message: Message):
    await message.answer("PHP Developer: \n \n PHP - язык программирования, который используется в веб разработке. В частности, PHP применяется для создания сайтов и веб-приложений, а также для разработки сервисов, инструментов, модулей и скриптов, связанных с сайтами. Был создан в 1994 году Расмусом Лердорфом, самое первое воплощение PHP было простым набором CGI-скриптов, написанных на языке программирования Си. Изначально используя их для отслеживания посещений своего веб-резюме, он назвал этот набор скриптов «Personal Homepages Tools»(Инструменты для персональных домашних страниц), но более часто упоминалось название «PHP Tools». Со временем требовалось все больше улучшений функциональности, и Расмус переписал PHP Tools, создав более крупную и богатую реализацию.",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN)  



@bot.on.private_message(state=MenuState.PROF_INFO, payload={"cmd": "prof_7"})
async def end_handler(message: Message):
    await message.answer("Дизайнер: \n \n Еще в эпоху Возрождения, когда человек стал задумываться над эргономикой и удобством, красотой и приятным внешним видом предметов быта, орудий труда и процессов своей трудовой деятельности, появилось понятие дизайна. Не мудрено, что термин имеет итальянское происхождение. Понятие «designo intero» в переводе означает появление у художника идеи или замысла, которые воплощались в рисунках, эскизах и чертежах. \n \n Работа дизайнером в современном понимании стала востребована лишь в XIX веке во время стремительного роста промышленного производства. В этот период заводы и фабрики стали особенно остро нуждаться в проектно-изобразительной деятельности. Первые школы профессии дизайнера появились в середине XX века, когда специалисты стали востребованы и в широких кругах общественности.",
        keyboard=(
            Keyboard()
            .add(Text("Далее", {"cmd": "again"}))
            .add(Text("Назад", {"cmd": "prof_end"}))
        ),
    )
    await bot.state_dispenser.set(message.peer_id, MenuState.PROF_AGAIN) 



#SECRET-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(text=["Мы работаем не потому что надо, а потому что важно!", "мы работаем не потому что надо, а потому что важно!", "мы работаем не потому что надо,а потому что важно!", "Мы работаем не потому что надо,а потому что важно!"], state=MenuState.MAIN_LIMB_31)
async def info_item_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await check_handler(user)
    if collection.find_one({"_id": user[0].id})["Ключ_1"] == 0:
        text = "Здесь технологии создаются"
        user = await bot.api.users.get(message.from_id)
        await bd_handler(user, text)
        await message.answer(
            "🎉Поздравляю ты нашел секретную комнату №1! \n \n Всего таких комнат 6 по всему квесту: \n 1)5 комнат одинаковых – они содержат ключ-фразу; \n 2)1 комната супер-секретная – в ней нужно ввести все 6 фраз-ключей в правильном порядке. \n \n Если ты все это сделаешь, то автоматически будешь участвовать в розыгрыше главных призов! \n \n Это команта с ключ-фразой, которую необходимо запомнить! Помни, что во все секретные комнаты можно попасть только 1 раз! \n \n 🔑*Здесь_технологии_создаются_* ",
            keyboard=(
                Keyboard()
                .add(Text("Покинуть секретную комнату", {"cmd": "secret_away"}))
            ),
        )
        await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_ROOM_1)
    else:
        return "Вы уже активировали эту фразу!"



@bot.on.private_message(text=["У нас не будет просто, но будет интересно!", "у нас не будет просто, но будет интересно!", "у нас не будет просто,но будет интересно!", "У нас не будет просто,но будет интересно!"], state=MenuState.SECRET_FINAL_1)
async def secret_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await check_handler(user)
    if collection.find_one({"_id": user[0].id})["Ключ_2"] == 0:
        text = "во благо общества"
        user = await bot.api.users.get(message.from_id)
        await bd_handler(user, text)
        await message.answer(
            "🎉Поздравляю ты нашел секретную комнату №2! \n \n Всего таких комнат 6 по всему квесту: \n 1)5 комнат одинаковых – они содержат ключ-фразу; \n 2)1 комната супер-секретная – в ней нужно ввести все 6 фраз-ключей в правильном порядке. \n \n Если вы все это сделаете, то автоматически будете участвовать в розыгрыше главных призов! \n \n Это команта с ключ-фразой, которую необходимо запомнить! Помни, что во все секретные комнаты можно попасть только 1 раз! \n \n 🔑*во_благо_общества_* ",
            keyboard=(
                Keyboard()
                .add(Text("Покинуть секретную комнату", {"cmd": "secret_away"}))
            ),
        )
        await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_ROOM_2)
    else: 
        return "Вы уже активировали эту фразу!"



@bot.on.private_message(text=["Главная ценность это люди!", "главная ценность это люди!"], state=MenuState.MAIN_LIMB_21)
async def secret_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await check_handler(user)
    if collection.find_one({"_id": user[0].id})["Ключ_3"] == 0:
        text = "решают сложные задачи," 
        await bd_handler(user, text)
        await message.answer(
            "🎉Поздравляю ты нашел секретную комнату №3! \n \n Всего таких комнат 6 по всему квесту: \n 1)5 комнат одинаковых – они содержат ключ-фразу; \n 2)1 комната супер-секретная – в ней нужно ввести все 6 фраз-ключей в правильном порядке. \n \n Если вы все это сделаете, то автоматически будете участвовать в розыгрыше главных призов! \n \n Это команта с ключ-фразой, которую необходимо запомнить! Помни, что во все секретные комнаты можно попасть только 1 раз! \n \n 🔑*решают_сложные_задачи_* ",
            keyboard=(
                Keyboard()
                .add(Text("Покинуть секретную комнату", {"cmd": "secret_away"}))
            ),
        )
        await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_ROOM_3)
    else:
        return "Вы уже активировали эту фразу!"



@bot.on.private_message(text=["Мы работаем на результат!", "мы работаем на результат!"], state=MenuState.SECRET_FINAL_2)
async def secret_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await check_handler(user)
    if collection.find_one({"_id": user[0].id})["Ключ_4"] == 0:
        text = "а человек находится в"
        await bd_handler(user, text)
        await message.answer(
            "🎉Поздравляю ты нашел секретную комнату №4! \n \n Всего таких комнат 6 по всему квесту: \n 1)5 комнат одинаковых – они содержат ключ-фразу; \n 2)1 комната супер-секретная – в ней нужно ввести все 6 фраз-ключей в правильном порядке. \n \n Если вы все это сделаете, то автоматически будете участвовать в розыгрыше главных призов! \n \n Это команта с ключ-фразой, которую необходимо запомнить! Помни, что во все секретные комнаты можно попасть только 1 раз! \n \n 🔑*а_человек_находится_в_* ",
            keyboard=(
                Keyboard()
                .add(Text("Покинуть секретную комнату", {"cmd": "secret_away"}))
            ),
        )
        await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_ROOM_4)
    else:
        return "Вы уже активировали эту фразу!"



@bot.on.private_message(text=["Мы делаем жизнь людей проще!", "мы делаем жизнь людей проще!"], state=MenuState.MAIN_LIMB_19)
async def secret_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await check_handler(user)
    if collection.find_one({"_id": user[0].id})["Ключ_5"] == 0:
        text = "центре экосистемы"
        await bd_handler(user, text)
        await message.answer(
            "🎉Поздравляю ты нашел секретную комнату №5! \n \n Всего таких комнат 6 по всему квесту: \n 1)5 комнат одинаковых – они содержат ключ-фразу; \n 2)1 комната супер-секретная – в ней нужно ввести 6 фраз-ключей в правильном порядке. \n \n Если вы все это сделаете, то автоматически будете участвовать в розыгрыше главных призов! \n \n Это команта с ключ-фразой, которую необходимо запомнить! Помни, что во все секретные комнаты можно попасть только 1 раз! \n \n 🔑*центре_экосистемы_* ",
            keyboard=(
                Keyboard()
                .add(Text("Покинуть секретную комнату", {"cmd": "secret_away"}))
            ),
        )
        await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_ROOM_5)
    else:
        return "Вы уже активировали эту фразу!"



@bot.on.private_message(text=["Здесь_технологии_создаются_во_благо_общества_решают_сложные_задачи_а_человек_находится_в_центре_экосистемы_все_это_про_MailRuGroup", "Здесь_технологии_создаются_во_благо_общества_решают_сложные_задачи_а_человек_находится_в_центре_экосистемы_все_это_про_MailRuGroup"], state=MenuState.SECRET_SECRET_START)
async def secret_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    await check_handler(user)
    if collection.find_one({"_id": user[0].id})["Ключ_6"] == 0:
        text = "ФИНАЛ"
        await bd_handler(user, text)
        await message.answer(
            "🎉ПОЗДРАВЛЯЮ ТЫ СМОГ ДОБРАТЬСЯ ДО САМОГО ФИНАЛА!🎉 \n \n Если ты попал в эту комнату, значит у тебя есть все шансы, чтобы получить приз от ВКонтакте! Эта комната – поздравление для тех, кто вдоль и поперек изучил этот квест! \n \n \n 💾От разработчика: \n Спасибо тебе за прохождение нашего квеста! \n Держи кусочек праздничного тортика: 🍰",
            keyboard=(
                Keyboard()
                .add(Text("Покинуть супер-секретную комнату", {"cmd": "secret_away"}))
            ),
        )
        await bot.state_dispenser.set(message.peer_id, MenuState.SECRET_SECRET_END)
    else:
        return "Ты уже нашел всё кодовое предложение!"



#DOP-----------------------------------------------------------------------------------------------------------------------------
@bot.on.private_message(state=MenuState.START, payload={"cmd": "no"})
async def end_handler(_):
    return "Эх, жаль что ты так рано уходишь... Но ты всегда можешь вернуться и пройти квест!"



@bot.on.private_message(state=MenuState.START_1, payload={"cmd": "no_again"})
async def end_handler(_):
    return "Хорошо тебе отдохнуть! Была рада провести с тобой время)"



@bot.on.private_message(state=[MenuState.MAIN_LIMB_31, MenuState.MAIN_LIMB_21, MenuState.MAIN_LIMB_19, MenuState.SECRET_FINAL_1, MenuState.SECRET_FINAL_2, MenuState.SECRET_SECRET_START])
async def secret_sorry_handler(_):
    return"Увы, но это не та фраза( \n Ты можешь попробовать поискать еще или продолжить проходить сюжет",



@bot.on.private_message()
async def sorry_handler(_):
    return"Извини, но я не понимаю тебя :(",



bot.run_forever()