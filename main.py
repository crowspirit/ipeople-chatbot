import telebot
from telebot import types
import config  # Імпорт конфігураційного файлу (припускаючи, що це файл з токеном бота)
import random
import time
# Створення об'єкту бота
bot = telebot.TeleBot(config.TOKEN)  # Використання токену бота з конфігураційного файлу

# Словник для відстеження статусу чатів
id_status_dict = {
    "831025623": False,
    "893937933": False,
    "564156636": False,
    "386886091": False,
    "143717296": False, #https://t.me/zhenia_1
    "172976473": False,
    "350478157": False, #https://t.me/Savchuk_Serhii
    "1349467692": False, #Pavlo

    "540901087": False,  #https://t.me/yaryna1
    "1283527316": False, #https://t.me/RotaterPlay
    "1298941033": False, #Саня
    "693686422": False, #https://t.me/Starstrackk
    "1009729019": False, #iPeople Келецька
    "1135214984": False, #iPeople Service
    "2069078525": False, #iPeople Service Podillya
    "6962931214": False #Service TheMall
}
names = ["Олександр", "Дмитро", "Павло", "Богдан", "Андрій", "Роман"]
timer_user = {}
def end_timer(user):
    try:
        n = 300
        timer_user[str(user)] = n
        for i in range(n):
            time.sleep(1)
            timer_user[user] = timer_user[user]-1
        timer_user.pop(user)
        bot.send_message(next(key for key, value in id_status_dict.items() if value == str(user)), "Користувач покинув чат",reply_markup=types.ReplyKeyboardRemove() )
        bot.send_message(user, "Менеджер покинув чат", reply_markup=get_keyboard())
        id_status_dict[next(key for key, value in id_status_dict.items() if value == str(user))] = False
    except:
        pass
selected_name = random.choice(names)
# Функція для створення клавіатури
def get_keyboard():
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = types.KeyboardButton(text="🗨️ - Менеджер")
    webAppTest = types.WebAppInfo("https://www.ipeople.in.ua/")
    buttons3 = types.KeyboardButton(text="🌐 - Наш сайт", web_app=webAppTest)
    buttons4 = types.KeyboardButton(text="🏪 - Магазини")
    buttons5 = types.KeyboardButton(text="📱 - Передзвоніть мені")
    buttons6 = types.KeyboardButton(text="🔧 - Ремонт")
    markup_menu.add(buttons3, buttons, buttons6, buttons4, buttons5)
    return markup_menu

def get_keyboard_city():
    city = ["Київ","Львів","Одеса","Вінниця","Івано-франківськ","Полтава","Тернопіль","Дніпро","Самбір","Біла Церква","Харків","Рівне","Житомир","Хмельницький", "Калинівка" ,"Бар" ,"Ужгород" , "Червоноград" ,]
    # keyboard = types.InlineKeyboardMarkup()
    buttons = []
    for i in city:
        button = types.InlineKeyboardButton(text=i, callback_data=f"city_{i}")
        if len(buttons) == 0 or len(buttons[-1]) == 2: # якщо останній рядок заповнений
            buttons.append([button])
        else:
            buttons[-1].append(button)
    return types.InlineKeyboardMarkup(buttons)
def get_keyboard_shops(shop):
    print(shop)
    shops = {
        #Київ
        "вул. Антоновича, 12": '<a href="https://maps.app.goo.gl/mYjeLT9YMT87y2NG9">📍 вул.Антоновича, 12</a>\n🗓️ Пн-Сб 10:00 - 20:00, Нд 12:00 - 18:00\n📞 +380688880003\nТг: @ipeople_12',
        "вул. Велика Васильківська, 16": '<a href="https://maps.app.goo.gl/UAMmjvqbmro5g5ZN9">📍 вул. Велика Васильківська, 16</a>\n🗓️(Без вихідних) 10:00 - 20:00\n📞 +380940000009\nТг: @ipeople_vasylkivska',
        "ТРЦ \"Атмосфера\"": '<a href="https://maps.app.goo.gl/oqjH69dMebcz3d899">📍 ТРЦ \"Атмосфера\"</a>\n🗓️ Пн - Нд 10:00 - 21:00\n📞 +380969441414\nТг:',
        "ТРЦ \"LAVINA MALL\"": '<a href="https://maps.app.goo.gl/5zfXGwQv1hfYiNqT9">📍 ТРЦ \"LAVINA MALL\"</a>\n🗓️ Пн - Нд 10:00 - 22:00\n📞 +380964447484\nТг: ',
        "ТРЦ \"Retroville\"": '<a href="https://maps.app.goo.gl/hYn5tsMwaeBWmiDj7">📍 ТРЦ \"Retroville\"</a>\n🗓️ Пн - Нд 10:00 - 22:00\n📞 +380964449434\nТг: @Retroville1',
        "ТРЦ \"Respublika Park\"": '<a href="https://maps.app.goo.gl/RXrTeDEdGqu41h586">📍 ТРЦ \"Respublika Park\"</a>\n🗓️ Пн - Нд 10:00 - 22:00\n📞 +380964447454\nТг: @ipeople_respublika',
        # Львів
        "вул. Городоцька, 2": '<a href="https://maps.app.goo.gl/Hjj7uxwvVvc4W3nDA">📍 вул. Городоцька, 2</a>\n🗓️ Пн-Сб 10:00 - 20:00, Сб 11:00 - 20:00, Нд 12:00 - 18:00\n📞 +380977272772\nТг: @ipeople_gorodotska',
        "Пр. Свободи 41": '<a href="https://maps.app.goo.gl/eEiF6LoQoQi55sbs9">📍 Пр. Свободи 41 (біля Оперного у дворі)</a>\n🗓️Пн-Сб 10:00 - 20:00, Сб 11:00 - 20:00, Нд 12:00 - 18:00\n📞 +380671676667\nТг: ',
        "ТРЦ \"New Point\"": '<a href="https://maps.app.goo.gl/gSprPtE3cMVroaJh6">📍 ТРЦ \"New Point\"</a>\n🗓️ Пн-Нд 10:00 - 21:00 \n📞 +380989339337\nТг: @ipeople_newpoint',
        "ТОЦ \"Fabrik\"": '<a href="https://maps.app.goo.gl/EvCF5nxFuSY8ejAE9">📍 ТОЦ \"Fabrik\"</a>\n🗓️ Пн-Сб 10:00 - 20:00, Сб 11:00 - 20:00, Нд 12:00 - 18:00\n📞 +380960785393\nТг: @fabrik_ipeople ',
        "вул. Щирецька, 36 ": '<a href="https://maps.app.goo.gl/5zfXGwQv1hfYiNqT9">📍 вул. Щирецька, 36 "Південний"</a>\n🗓️ Пн-Сб 10:00 - 20:00, Сб 11:00 - 20:00, Нд 12:00 - 18:00\n📞 +380981049949 \nТг: @ipeople_expo',
        "ТЦ \"Форум\"": '<a href="https://maps.app.goo.gl/Pyb5ggRk8J9d9teh6">📍 ТЦ \"Форум\"</a>\n🗓️ Пн-Сб 10:00 - 20:00, Сб 11:00 - 20:00, Нд 12:00 - 18:00\n📞 0934498357\nТг: ',
        "ТРЦ \"King Cross Leopolis\"": '<a href="https://maps.app.goo.gl/qWpELkC8yWK4utVw6">📍 ТРЦ \"King Cross Leopolis\"</a>\n🗓️ Пн - Нд 10:00 - 21:00\n📞 +380971091099\nТг: ',
        # Одеса
        "вул. Дерибасівська, 16": '<a href="https://maps.app.goo.gl/1ZpKmCuFqLYxLXqq7">📍 вул. Дерибасівська, 16</a>\n🗓️ Пн - Нд 10:00 - 21:00\n📞 +380739997777\nТг: @ipeople_odessa',
        # Рівне
        "ТРЦ \"Екватор\"": '<a href="https://maps.app.goo.gl/6vbAp35QiopMkvj48">📍 ТРЦ \"Екватор\"</a>\n🗓️ Пн - Нд 10:00 - 22:00\n📞 0673032217 \nТг: @ipeopleEkvator',
        "ТРЦ \"Злата Плаза\"": '<a href="https://maps.app.goo.gl/25jq722STn2UvFto9">📍 ТРЦ \"Злата Плаза\"</a>\n🗓️ Пн - Нд 10:00 - 21:00\n📞 +380675531653\nТг: @iPeopleZlataPlaza',
        # Дніпро
        "ТРЦ \"Каскад\"": '<a href="https://maps.app.goo.gl/DdtaDfSYL6MBna3p9">📍 ТРЦ \"Каскад\"</a>\n🗓️ Пн - Нд 10:00 - 20:00\n📞 +380977170797\nТг: @ipeoplecascade',
        # Самбір
        "ТЦ \"Атлант\"": '<a href="https://maps.app.goo.gl/NM6HeGcGjqeniacQ7">📍 ТЦ \"Атлант\"</a>\n🗓️ Пн - Нд 10:00 - 19:00\n📞 +380672465999\nТг: @sambiripeople',
        # Біла церква
        "ТРЦ \"Гермес\"": '<a href="https://maps.app.goo.gl/NQvryNhQovhrwaGW7">📍 ТРЦ \"Гермес\"</a>\n🗓️ Пн - Нд 09:00 - 20:00\n📞 +380984545757\nТг: @BilaTserkvaiPeople',
        # Харків
        "ТЦ \"Французький Бульвар\"": '<a href="https://maps.app.goo.gl/CtF2JcFu6Ygdwe4c6">📍 ТЦ \"Французький Бульвар\"</a>\n🗓️ Пн - Нд 10:00 - 19:00\n📞 +380737017771\nТг: @IpeopleFB',
        # Хмельницький
        "ТЦ \"Квартал\"": '<a href="https://maps.app.goo.gl/WYqDW4ARXKaLB8sQ6">📍 ТЦ \"Квартал\"</a>\n🗓️ Пн - Нд 10:00 - 20:00 Без вихідних\n📞 +380682131210\nТг: @iPeople_kvartal',
        # Червоноград
        "ТРЦ \"Кристинопіль\"": '<a href="https://maps.app.goo.gl/TRrEZeQeJBjVC6Sz9">📍 ТРЦ \"Кристинопіль\"</a>\n🗓️ Пн - Сб 10:00 - 19:00 Нд 12:00 - 18:00\n📞 +380670777221\nТг: @iPeople_Krystynopil',
         "ТРЦ \"Майдан\"": '<a href="https://maps.app.goo.gl/tSe1d4ycTXDGEXrw9">📍 ТРЦ \"Майдан\"</a>\n🗓️ Пн - Сб 10:00 - 19:00 Нд 12:00 - 18:00\n📞 +380985654900\nТг: @iPeople_store',
        # Калинівка
        "вул. Незалежності, 7": '<a href="https://maps.app.goo.gl/4VtCyGdU7G7v4DYp6">📍 вул. Незалежності, 7</a>\n🗓️ Пн - Сб 10:00 - 19:00 Нд 12:00 - 18:00\n📞 +380989111223\nТг: ',
        # Івано франківськ
        "Любомира Гузара, 4": '<a href="https://maps.app.goo.gl/b9Qr7WwSt2TQQpLn7">📍 Любомира Гузара, 4</a>\n🗓️ Пн - Сб 10:00 - 20:00 Нд 11:00 - 19:00\n📞 +380677660676\nТг: ',
        #Житомир
        "вул. Київська, 59": '<a href="https://maps.app.goo.gl/hj5rFoMQPvqBgJ626">📍 вул. Київська, 59</a>\n🗓 Пн. - Нд.: 10.00 – 21.00\n📞 +380670081884\nТг: ',
        "вул. Бориса Лятошинського, 23": '<a href="https://maps.app.goo.gl/6XhRany9NeETXNUB9">📍 вул. Бориса Лятошинського, 23</a>\n🗓 Пн. - Нд: 10.00 – 20.00\n📞 +380684442484\nТг: ',
        #Ужгород
        "вул. Корзо, 23": '<a href="https://maps.app.goo.gl/UTehUgRazL5vxtbHA">📍 вул. Корзо, 23</a>\n🗓 Пн. - Сб: 10.00 – 19.00 Нд 10:00 - 17:00\n📞 +380668887939\nТг: ',
        #Тернопіль
        "вул. Руська 16": '<a href="https://maps.app.goo.gl/txsboDspzwZdGdRF8">📍 вул. Руська 16</a>\n🗓 Пн - Нд 10:00 - 19:00\n📞 +380989576900\nТг: @ipeople_ternopil',

        #Бар
        "вул. Героїв Майдану 20а": '<a href="https://maps.app.goo.gl/WX2DcNeNSRkbB8Rr5">📍 вул. Героїв Майдану 20а</a>\n🗓 Пн - Нд 10:00 - 19:00Вт. - Пт.: 10.00 – 18.00 Субота: 10.00 – 17.00 Неділя;Понеділок - Вихідний\n📞 +380678719870\nТг: ',
        #Вінниця
        "вул. Соборна 53а": '<a href="https://maps.app.goo.gl/GqzK1dFHKFydXGNt5">📍 вул. Соборна 53а</a>\n🗓 Без вихідних: 10:00 – 20:00\n📞 +380960689999\nТг: @soborna53',
        "вул. Келецька 58": '<a href="https://maps.app.goo.gl/BydHiaxhy1k63Rkm6">📍 вул. Келецька 58</a>\n🗓 Без вихідних: 10.00 – 20.00\n📞 +380961524224\nТг: @iPeople_Keletska58',
        "вул. Коцюбинського 9": '<a href="https://maps.app.goo.gl/zbnydF8zgLPKrCvE6">📍 вул. Коцюбинського 9 (Папаніна)</a>\n🗓 Пн - Нд 10:00 - 19:00\n📞 +380688549954\nТг: @iPeople_Papanina',
        "ТЦ \"Premier Tower\"": '<a href="https://maps.app.goo.gl/V3CAjmR1koqkLgJk7">📍 ТЦ \"Premier Tower\"</a>\n🗓 Пн - Нд 10:00 - 19:00\n📞 +380733007033\nТг: @ipeople_PT',
        "ТЦ \"The Mall\"": '<a href="https://maps.app.goo.gl/kvXBEVuZkPdET755A">📍 ТЦ \"The Mall\"</a>\n🗓 Пн - Нд 10:00 - 19:00\n📞 +380737003009\nТг: @TheMall77',
        "вул. Зодчих, 10": '<a href="https://maps.app.goo.gl/kvXBEVuZkPdET755A">📍 вул. Зодчих, 10 (Поділля)</a>\n🗓 Пн - Нд 10:00 - 19:00\n📞 +380680010868\nТг: @iPeoplePodillya',
         #Полтава
        "ТЦ \"Екватор\"": '<a href="https://maps.app.goo.gl/pKLSngCW3ckgLz1T6">📍 ТЦ \"Екватор\"</a>\n🗓️ Пн - Нд 10:00 - 22:00\n📞 +380673032217 \nТг: ',
        "ТРЦ \"Конкорд\"": '<a href="https://maps.app.goo.gl/9tSSJScVwUkt4UpF9">📍 ТРЦ \"Конкорд\"</a>\n🗓️ Пн - Нд 10:00 - 22:00\n📞 +380687711220 \nТг: ',
    }
    return shops[shop]



# Обробник команди /start
@bot.message_handler(commands=['start'])
def info(message):
    # Надсилання привітання та створення клавіатури
    if str(message.chat.id) in id_status_dict.keys():
        bot.send_message(message.chat.id,'Ви менеджер')
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Інструкція користування", callback_data=f"info"))
        bot.send_message(message.chat.id, "👋Привіт, це бот підтримки iPeople)\nОберіть доступні команди👇",reply_markup=get_keyboard())
        bot.send_message(message.chat.id, "Для отримання інструкції з користування натисніть кнопку нижче👇",reply_markup=keyboard)
        # bot.edit_message_reply_markup(message.chat.id,messages.id,reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.chat.id,"🗨️ Зв'язатись з менеджером - натисніть цю кнопку, щоб почати розмову з нашим менеджером.\n\n🌐 Наш сайт - відвідайте наш сайт для отримання додаткової інформації про наші продукти та послуги. \n\n🏪 Магазини - знайдіть найближчий магазин iPeople та дізнайтеся про години роботи та його контактн данні.\n\n📱 Передзвоніть мені -  використовуйте цю кнопку, щоб залишити свій номер телефону.\n\n🔧 Ремонт - отримайте інформацію про наші послуги ремонту та підтримки.\n\nЯкщо у вас виникнуть будь-які питання, не соромтеся звертатися до нас.\n\nОбери доступні команди👇")

@bot.callback_query_handler(func=lambda call: "info" == call.data)
def handle_teachers_callback(call):
    bot.edit_message_text("🗨️ Зв'язатись з менеджером - натисніть цю кнопку, щоб почати розмову з нашим менеджером.\n\n🌐 Наш сайт - відвідайте наш сайт для отримання додаткової інформації про наші продукти та послуги. \n\n🏪 Магазини - знайдіть найближчий магазин iPeople та дізнайтеся про години роботи та його контактн данні.\n\n📱 Передзвоніть мені -  використовуйте цю кнопку, щоб залишити свій номер телефону.\n\n🔧 Ремонт - отримайте інформацію про наші послуги ремонту та підтримки.\n\nЯкщо у вас виникнуть будь-які питання, не соромтеся звертатися до нас.\n\nОбери доступні команди👇",call.message.chat.id,call.message.id)

@bot.callback_query_handler(func=lambda call: "manager" == call.data or "service" == call.data)
def handle_teachers_callback(call):
    if "manager" == call.data:
        keyboard = types.InlineKeyboardMarkup()
        button_today = types.InlineKeyboardButton(text="Прийняти✅", callback_data=f"{call.message.chat.id}")
        keyboard.add(button_today)
        bot.send_message(config.chat_id_help, f"Новий запит від:\n{call.message.from_user.first_name}  {call.message.from_user.last_name} (@{call.message.from_user.username})\n{call.message.text[:-33]}", reply_markup=keyboard)
        bot.send_message(call.message.chat.id, "Ваш запит прийнято. Зачекайте, будь ласка доки менеджер приєднається до чату.")
        bot.delete_message(call.message.chat.id,call.message.id)
    elif "service" == call.data:
        keyboard = types.InlineKeyboardMarkup()
        button_today = types.InlineKeyboardButton(text="Прийняти✅", callback_data=f"{call.message.chat.id}")
        keyboard.add(button_today)
        bot.send_message(config.chat_id_service, f"Новий запит від:\n{call.message.from_user.first_name}  {call.message.from_user.last_name} (@{call.message.from_user.username})\n{call.message.text[:-33]}", reply_markup=keyboard)
        bot.send_message(call.message.chat.id, "Ваш запит прийнято. Зачекайте, будь ласка доки менеджер приєднається до чату.")
        bot.delete_message(call.message.chat.id,call.message.id)

@bot.callback_query_handler(func=lambda call: "call" in call.data)
def handle_teachers_callback(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.from_user.id, call.message.text)

# //////////////------------------------------------магазини--------------------------------------

@bot.message_handler(func=lambda message: message.text == "🏪 - Магазини")
def info(message):
    if str(message.chat.id)[0] != "-":
        bot.send_message(message.chat.id, "Виберіть місто:", reply_markup=get_keyboard_city(),parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: "city" in call.data)
def handle_teachers_callback(call):
    cities = {"Київ": ["вул. Антоновича, 12","вул. Велика Васильківська, 16","ТРЦ \"Атмосфера\"","ТРЦ \"LAVINA MALL\"","ТРЦ \"Retroville\"","ТРЦ \"Respublika Park\""],
              "Львів": ["вул. Городоцька, 2","Пр. Свободи 41","ТРЦ \"New Point\"","ТОЦ \"Fabrik\"", "вул. Щирецька, 36 ","ТЦ \"Форум\"","ТРЦ \"King Cross Leopolis\""],
              "Одеса": ["вул. Дерибасівська, 16"],
              "Вінниця": ["вул. Соборна 53а","вул. Келецька 58","ТЦ \"Premier Tower\"","ТЦ \"The Mall\"", "вул. Коцюбинського 9","вул. Зодчих, 10"],
              "Івано-франківськ":["Любомира Гузара, 4"],
              "Полтава":[  "ТЦ \"Екватор\"","ТРЦ \"Конкорд\"" ],
              "Тернопіль":[ "вул. Руська 16"],
              "Дніпро":["ТРЦ \"Каскад\""],
              "Самбір":["ТЦ \"Атлант\""],
              "Біла Церква":["ТРЦ \"Гермес\""],
              "Харків":["ТЦ \"Французький Бульвар\""],
              "Рівне":["ТРЦ \"Екватор\"","ТРЦ \"Злата Плаза\""],
              "Ужгород":["вул. Корзо, 23"],
              "Бар":["вул. Героїв Майдану 20а"],
              "Житомир":["вул. Київська, 59","вул. Бориса Лятошинського, 23"],
              "Червоноград":["ТРЦ \"Кристинопіль\"", "ТРЦ \"Майдан\""],
              "Калинівка": ["вул. Незалежності, 7"],
              "Хмельницький":["ТЦ \"Квартал\""]
              }
    keyboard = types.InlineKeyboardMarkup()
    for i in cities[call.data.split("_")[1]]:
        print(i)
        keyboard.add(types.InlineKeyboardButton(text=i, callback_data=f"shop_{i}"))
    bot.edit_message_text("Виберіть магазин:", call.message.chat.id, call.message.id)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.id,reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: "shop" in call.data)
def handle_teachers_callback(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id,get_keyboard_shops(call.data.split("_")[1]),parse_mode="HTML")
    # bot.edit_message_text(get_keyboard_shops(call.data.split("_")[1]), call.message.chat.id, call.message.id,parse_mode="Markdown")
    # bot.edit_message_reply_markup(call.message.chat.id, call.message.id,reply_markup=types.ReplyKeyboardRemove())
#////-----------------------------HELP CHAT--------------------------------------------------------------------------------------------------------------//////


@bot.message_handler(func=lambda message: message.text == "🔧 - Ремонт")
def info(message):
    if str(message.chat.id)[0] != "-":
        remove_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        remove_markup.add(types.KeyboardButton(text="Повернутись⬅️"))
        bot.send_message(message.chat.id, "Задайте ваше питання.", reply_markup=remove_markup)
        bot.register_next_step_handler(message, chat_service)

# Обробник для натискання кнопки "Зв'язатись з менеджером"
@bot.message_handler(func=lambda message: message.text == "🗨️ - Менеджер")
def info(message):
    if str(message.chat.id)[0] != "-":
        remove_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        remove_markup.add(types.KeyboardButton(text="Повернутись⬅️"))
        bot.send_message(message.chat.id, "Задайте ваше питання.", reply_markup=remove_markup)
        bot.register_next_step_handler(message, chat_help)

# Функція для обробки чату
def chat_help(message):
    if message.text[0] == '/':
        remove_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        remove_markup.add(types.KeyboardButton(text="Повернутись⬅️"))
        bot.send_message(message.chat.id, "Надішліть повідомлення, а не команду.", reply_markup=remove_markup)
        bot.register_next_step_handler(message, chat_call)
        return
    elif message.text == 'Повернутись⬅️':
        bot.send_message(message.chat.id,"Ви повернулись до головного меню.",reply_markup=get_keyboard())
        return
    keyboard = types.InlineKeyboardMarkup()
    button_today = types.InlineKeyboardButton(text="Прийняти✅", callback_data=f"{message.chat.id}")
    keyboard.add(button_today)
    bot.send_message(config.chat_id_help, f"Новий запит від:\n{message.from_user.first_name}  {message.from_user.last_name} (@{message.from_user.username})\n{message.text}", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Ваш запит прийнято. Зачекайте, будь ласка доки менеджер приєднається до чату.")

#////-----------------------------SERVICE CHAT--------------------------------------------------------------------------------------------------------------//////

# Функція для обробки чату
def chat_service(message):
    if message.text[0] == '/':
        remove_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        remove_markup.add(types.KeyboardButton(text="Повернутись⬅️"))
        bot.send_message(message.chat.id, "Надішліть повідомлення, а не команду.", reply_markup=remove_markup)
        bot.register_next_step_handler(message, chat_call)
        return
    elif message.text == 'Повернутись⬅️':
        bot.send_message(message.chat.id,"Ви повернулись до головного меню.",reply_markup=get_keyboard())
        return
    keyboard = types.InlineKeyboardMarkup()
    button_today = types.InlineKeyboardButton(text="Прийняти✅", callback_data=f"{message.chat.id}")
    keyboard.add(button_today)
    bot.send_message(config.chat_id_service, f"Новий запит від:\n{message.from_user.first_name}  {message.from_user.last_name} (@{message.from_user.username})\n{message.text}", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Ваш запит прийнято. Зачекайте, будь ласка доки менеджер приєднається до чату.", reply_markup=get_keyboard())

# Обробник для inline-кнопок
@bot.callback_query_handler(func=lambda call: "1" != call.data)
def handle_teachers_callback(call):
    if id_status_dict[str(call.from_user.id)] == False:
        print(call.from_user.id)
        bot.delete_message(call.message.chat.id, call.message.id)
        id_status_dict[str(call.from_user.id)] = call.data
        print(id_status_dict)
        markup_end = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_end_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = types.KeyboardButton(text="Завершити чат❌")
        buttons1 = types.KeyboardButton(text="Завершити чат через 5 хв")
        markup_end.add(buttons, buttons1)
        markup_end_user.add(buttons)
        bot.send_message(call.from_user.id, call.message.text, reply_markup=markup_end)
        bot.send_message(str(call.data), f"Менеджер {selected_name} приєднався до чату", reply_markup=markup_end_user)

# Обробник для повідомлень від користувачів
@bot.message_handler(content_types=['text', 'photo', 'sticker','video','voice','contact','document','video_note'],func=lambda message: str(message.chat.id) in id_status_dict.keys() or str(message.chat.id) in list(id_status_dict.values()))
def info(message):
    print(list(id_status_dict.values()))
    if message.content_type == 'text':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            if message.text == "Завершити чат❌":
                bot.send_message(id_status_dict[str(message.chat.id)], "Менеджер покинув чат", reply_markup=get_keyboard())
                bot.send_message(message.chat.id, "Сеанс завершено", reply_markup=types.ReplyKeyboardRemove())
                id_status_dict[str(message.chat.id)] = False
            elif message.text == "Завершити чат через 5 хв":
                bot.send_message(message.chat.id, "Відлік почався", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton(text="Завершити чат❌")))
                bot.send_message(id_status_dict[str(message.chat.id)], "Якщо ви недішлете повідомлення протягом 5 хвилин чат завершиться.")
                end_timer(id_status_dict[str(message.chat.id)])
            else:
                bot.send_message(id_status_dict[str(message.chat.id)], message.text)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            if message.text == "Завершити чат❌":
                bot.send_message(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)), "Користувач покинув чат",reply_markup=types.ReplyKeyboardRemove() )
                bot.send_message(message.chat.id, "Сеанс завершено", reply_markup=get_keyboard())
                id_status_dict[next(key for key, value in id_status_dict.items() if value == str(message.chat.id))] = False
            elif str(message.chat.id) in timer_user.keys():
                print(timer_user)
                timer_user.pop(str(message.chat.id))
                bot.send_message(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)), message.text, reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton(text="Завершити чат❌"),types.KeyboardButton(text="Завершити чат через 5 хв")))
            else:
                bot.send_message(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)), message.text)
        elif str(message.chat.id) in list(id_status_dict.values()):
            for key, value in id_status_dict.items():
                if value == str(message.chat.id):
                    bot.send_message(key, message.text)
                    break
    elif message.content_type == 'photo':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_photo(id_status_dict[str(message.chat.id)],message.photo[-1].file_id)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_photo(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.photo[-1].file_id)
    elif message.content_type == 'sticker':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_photo(id_status_dict[str(message.chat.id)],message.sticker.file_id)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_photo(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.sticker.file_id)
    elif message.content_type == 'video':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_video(id_status_dict[str(message.chat.id)],message.video.file_id)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_video(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.video.file_id)
    elif message.content_type == 'voice':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_video(id_status_dict[str(message.chat.id)],message.voice.file_id)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_video(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.voice.file_id)
    elif message.content_type == 'contact':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_contact(id_status_dict[str(message.chat.id)],message.contact.phone_number,'контакт')
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_contact(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.contact,'контакт')
    elif message.content_type == 'document':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_document(id_status_dict[str(message.chat.id)],message.document.file_id)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_document(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.document.file_id)
    elif message.content_type == 'video_note':
        if str(message.chat.id) in id_status_dict.keys() and id_status_dict[str(message.chat.id)] != False:
            bot.send_video_note(id_status_dict[str(message.chat.id)],message.video_note.file_id)
        elif str(message.chat.id) in list(id_status_dict.values()) and str(message.chat.id) in list(id_status_dict.values()):
            bot.send_video_note(next(key for key, value in id_status_dict.items() if value == str(message.chat.id)),message.video_note.file_id)

# ------------------------------------передзвоніть мені-----------------------------------------
@bot.message_handler(func=lambda message: message.text == "📱 - Передзвоніть мені")
def info(message):
    print(1212)
    if str(message.chat.id)[0] != "-":
        remove_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        remove_markup.add(types.KeyboardButton(text="Повернутись⬅️"))
        bot.send_message(message.chat.id, "Надішліть свій номер.", reply_markup=remove_markup)
        bot.register_next_step_handler(message, chat_call)

# Функція для обробки чату
def chat_call(message):
    if message.text[0] == '/':
        remove_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        remove_markup.add(types.KeyboardButton(text="Повернутись⬅️"))
        bot.send_message(message.chat.id, "Надішліть свій номер, а не команду.", reply_markup=remove_markup)
        bot.register_next_step_handler(message, chat_call)
        return
    elif message.text == 'Повернутись⬅️':
        bot.send_message(message.chat.id,"Ви повернулись до головного меню.",reply_markup=get_keyboard())
        return
    keyboard = types.InlineKeyboardMarkup()
    button_today = types.InlineKeyboardButton(text="Прийняти✅", callback_data=f"call_{message.chat.id}")
    keyboard.add(button_today)
    bot.send_message(config.chat_id_call, f"Телефонний дзвінок:\n{message.from_user.first_name}  {message.from_user.last_name} (@{message.from_user.username})\n{message.text}", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Ми прийняли ваш запит. Зачекайте, будь ласка доки менеджер вам зателефонує.",reply_markup=get_keyboard())


# ----------------------------деволт повідомлення-----------------------------------------------
@bot.message_handler(content_types=['text'], func=lambda message: message.chat.id[0] != '-')
def prop(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="Менеджеру", callback_data=f"manager")
    button_2 = types.InlineKeyboardButton(text="Ремонт", callback_data=f"service")
    keyboard.add(button_1,button_2)
    bot.send_message(message.chat.id,f"<i>{message.text}</i>\n\nКому надіслати це повідомлення?", reply_markup=keyboard, parse_mode='HTML')
# Запуск бота
bot.polling(none_stop=True, timeout=999999)
