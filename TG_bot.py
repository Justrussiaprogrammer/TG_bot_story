import telebot
from telebot import types


name = 'tg_bot_for_adventures'
teg = 'project_story_teller_bot'
token = '6533445420:AAGFKLphrbGpVaNlK7BNsDRM-vIn0lmbBCY'
bot = telebot.TeleBot(token)

start_text = ('Приветствую вас в боте интерактивного приключения! Здесь реализуется мини-история, в течении '
              'которой вам придется окунуться в повседневность игровой разработчицы, и попытаться прийти к одному'
              ' из возможных финалов!\n'
              'Для получения новых сообщений используйте команду /next.\n'
              'Если вам требуется помощь, или вам непонятно что-то в работе программы, используйте команду /help')
help_text = ("Вот список команд бота:\n"
             "/start - выводит стартовое сообщение\n"
             "/next - получить новое событие\n"
             "/reboot - начать историю заново\n"
             "/info - получить информацию о текущем состоянии игры\n"
             "/fridge - показывает количество продуктов в холодильнике\n"
             "/echo - квест-пасхалка, влияющяя на игровой процесс\n"
             "/help - команда для получения этого сообщения\n")
next_text = "Что же поделать теперь?"
hack_try = "Не надо пытаться сломать систему! У нее лапки!"
name_space_error = "Используй 1 пробел!"
hello_text = " начинает свою маленькую историю!"

all_activities_names = ["Зарядка", "Гигиена", "Еда", "Идти в школу", "Изучать Python", "Смотреть Ютуб",
                        "Гулять с друзьями", "Спортзал", "Делать уроки", "Сходить в магазин",
                        "Готовиться ко сну", "Делать игру", "Проверить темную зону"]

code_activities = dict()
for i in range(3, 16):
    code_activities[all_activities_names[i - 3]] = i

all_activities_texts = dict()
exercise_text = "Аааах, проснулись - потянулись! Все как надо!"
bath_text = "Чистота - залог здоровья! Помою зубы и другие вроде важные части тела"
food_text = "А почему бы не поесть? Кто рано встает, тому Бог подаёт!"
school_text = "Ну, пора в школу!"
python_text = "Python всегда пригодится, пройду-ка курс по нему"
youtube_text = "Посмотрю-ка моего любимого ютубера, расслаблюсь"
street_text = "Пора выйти потрогать траву, пообщаюсь с людьми. А то так можно совсем к стулу прирасти!"
gym_text = "Спорт - всему голова! Ну и вообще заряжает, если голову правильно использовать"
homework_text = "Пионер - всем ребятам пример! Я вроде ничем не хуже..."
store_text = "Что-то маловато продуктов в холодильнике осталось. Пойду пополню запасы!"
sleep_text = "Пойду спать готовиться, что-то сегодня сложный день выдался. Завтра вообще-то тоже надо что-то делать!"
game_text = ("А вот и самое главное - моя будущая игра. Я столько тружусь, чтобы она когда-нибудь вышла в свет! Пора за"
             " работу!")
dark_text = ("В̵͉̘͛͒́̈́͜͝ы̶̞͙̱̄͝ ̵͂̑̇̈́̌͟п̵̲̘̱̪̀͒о̶̟̭͙͔̘̀͌̔̔̍д̵̫̄ќ̶̥͚̜̿л̵̭̻̜̝͌͝ͅю̴̹̍͆̃͝ч̷̤̟͆̃͡и̸̹̞͂̀̉л̸"
             "̤̑̇ѝ̵̤͎с̶̨̳̗͎̀ь̶̦͚͉͚͂́̏̏́ ̷̼̪̀к̷̠̏ ̶̛̜̘́͑ͅс̶͖̳̇̇̇̈́͆е̷̺̤͕͍̑̅͂͌͠р̵̧͓͎͛в̵̩̪̺͕̬̄̃̈ѐ̵̺̭͚̺̻р̴̲̉̍̆̾͠ў̸̈"
             "̻̣.̶̨̭͚̣̲̔͂͘̚͠ ̷̙͔̖͙̹̾͆̽̇Д̷̨̡̟̟̯̈́͛̆̐͘о̶̡̥͈̃б̸̡̨̘̟̌ͅр̵̧̢̤̻̰̎͌о̷̡̩̗͈͕̔̊̂ ̷̧̭̼̀п̵̡̞́͂̑̋̔о̷̻̩̉̏̈́̚ж̶̔̇"
             "̗̝͋̎̚а̴͙̔́̀͋̐ͅл̸̢̳̳̱͉̀̾̀͐о̶̞̽̈́͟в̴̳̼̹̟͊͟͝͡а̷̮̀̓̅т̸̱̀̾́ь̷̘͊͗̚ͅ ̶͔́̚в̶̪̥́̑͐̑͠ ̷̢̟̈́̈́͝Ӭ̵̟̹̘́̈́̈х"
             "̵̡͔͍̉͛̿о̴̰̭̰̬̓̈́̄͗͘")
all_activities_texts["Зарядка"] = exercise_text
all_activities_texts["Гигиена"] = bath_text
all_activities_texts["Еда"] = food_text
all_activities_texts["Идти в школу"] = school_text
all_activities_texts["Изучать Python"] = python_text
all_activities_texts["Смотреть Ютуб"] = youtube_text
all_activities_texts["Гулять с друзьями"] = street_text
all_activities_texts["Спортзал"] = gym_text
all_activities_texts["Делать уроки"] = homework_text
all_activities_texts["Сходить в магазин"] = store_text
all_activities_texts["Готовиться ко сну"] = sleep_text
all_activities_texts["Делать игру"] = game_text
all_activities_texts["Проверить темную зону"] = dark_text


count_streets = 0
position_streets = 0
street_dialogs = [[], []]
street_dialogs[0].append("Я позвонила друзьям и мы договорились встретиться возле школы."
                         " Мы гуляли по городу, пару раз заходили в придорожные кафешки, болтали о том, о сем")
street_dialogs[0].append("Когды мы проходили под мостом возле ж/д станции, я заметила свежее графити, исполненное на"
                         "практически всем пространстве потолка. Это место уже долгие годы расписывают все кому не"
                         " лень, но обычно рисунки не были такими большими")
street_dialogs[0].append("К тому же, это не было картиной или лозунгом, а скорее напоминало тег - Сверху большими"
                         " черными буквами с белой оконтовкой было написано '/45_43_48_4F'")
street_dialogs[0].append("Я спросила у идущей рядом подруги, не знает ли она, что это такое\n"
                         "- Говорят, какие-то странные люди платят райтерам, чтобы они как-то позаметнее нарисовали"
                         " заказ\n- Может опять какие-то котики, может похуже что-нибудь. Не бери в голову, короче")
street_dialogs[0].append("На самом деле такой рекламы было навалом, но меня смущала латинская F на конце. Может ошибся"
                         " человек, который рисовал номер. Может это часть тега Телеграма. Но почему-то мне казалось,"
                         " что тут все не так просто")
street_dialogs[0].append("Но вскоре стало не до странной надписи, мысли закрутились, и я забыла о странном граффити."
                         " Вскоре закончилась и прогулка, и я вернулась домой")
street_dialogs[1].append("Я позвонила друзьям и мы договорились встретиться возле школы."
                         " Мы гуляли по городу, пару раз заходили в придорожные кафешки, болтали о том, о сем")
street_dialogs[1].append("Я отлично погуляла, приятно провела время и вернулась домой")


influence = dict()
influence["Зарядка"] = [1, 0, 0, 0, 0, 0]
influence["Гигиена"] = [1, 0, 0, 0, 0, 0]
influence["Еда"] = [0, 0, 0, 0, 0, 0]
influence["Идти в школу"] = [0, 0, 0, 1, 1, 0]
influence["Изучать Python"] = [0, 0, 1, 0, 0, 0]
influence["Смотреть Ютуб"] = [0, 0, 0, 0, 0, 1]
influence["Гулять с друзьями"] = [1, 0, 0, 0, 1, 1]
influence["Спортзал"] = [1, 1, 0, 0, 0, 0]
influence["Делать уроки"] = [0, 0, 0, 1, 0, 0]
influence["Сходить в магазин"] = [1, 0, 0, 0, 0, 0]
influence["Готовиться ко сну"] = [1, 0, 0, 0, 0, 0]
influence["Делать игру"] = [0, 0, 2, 0, 0, 1]
influence["Проверить темную зону"] = [0, 0, 1, 0, 0, 0]

morning_activities = ["Зарядка", "Гигиена", "Еда"]
morning_additional = ["Идти в школу", "Изучать Python"]
noon_activities = ["Смотреть Ютуб", "Гулять с друзьями", "Еда", "Сходить в магазин"]
noon_additional = ["Изучать Python", "Спортзал", "Делать уроки"]
evening_activities = ["Смотреть Ютуб", "Гулять с друзьями", "Еда", "Сходить в магазин"]
evening_additional = ["Делать игру", "Спортзал", "Делать уроки", "Готовиться ко сну"]
quest = ["Проверить темную зону"]

all_activities = [morning_activities, morning_additional, noon_activities, noon_additional, evening_activities,
                  evening_additional]

situations = dict()
situations[(0, 0)] = ("Назовись, незнакомка! Через пробел введи свое имя и титул", 2)
situations[(0, 1)] = ("Сегодня я проснулась рано, так как впереди меня ждет куча дел!\n"
                      "Что бы поделать в первую очередь?", 1)
situations[(0, 2)] = ("Прошло достаточно много времени. Сделала ли я все, что от меня зависело?\n"
                      "Посмотрим, и в первую очередь на часы", -1)
situations[(1, 0)] = ("Опа, а тут и утро закончилось! Не будем медлить, пришла пора позаниматься чем-нибудь"
                      " интересньким!\nЧем займемся в этот раз?", 1)
situations[(1, 1)] = ("Пока что день проходит хорошо. Надеюсь так и будет дальше😀", -1)
situations[(1, 2)] = ("То за одно хваталась, то за другое. И вот уже начинает темнеть. ", -1)
situations[(2, 0)] = ("Ничего себе! Уже вечер! Пора подумать, чем бы можно было заняться теперь", 1)
situations[(2, 1)] = ("Хоть и хотелось поделать сегодня как можно больше дел, но время не бесконечно. День"
                      " заканчивается, но завтра я вернусь с новыми силами, чтобы стать ещё лучше!", -1)
situations[(2, 2)] = ("День окончен, город спит. На этом закончилась и наша игра. Для просмотра информации"
                      " воспользуйтесь командой /info, или загляните в файл girl's_chronicles.txt", -1)

all_food_names = ["Каша", "Яичница с беконом", "Овощной салат", "Фруктовый салат", "Готовый комплекс", "Энергетик",
                  "Чипсы с чаем", "Торт"]

cost = dict()
cost["Каша"] = 100
cost["Яичница с беконом"] = 300
cost["Овощной салат"] = 400
cost["Фруктовый салат"] = 500
cost["Готовый комплекс"] = 200
cost["Энергетик"] = 50
cost["Чипсы с чаем"] = 80
cost["Торт"] = 800

influence["Каша"] = [2, 0, 0, 0, 0, 0]
influence["Яичница с беконом"] = [1, 0, 0, 0, 0, 0]
influence["Овощной салат"] = [1, 0, 0, 0, 0, 0]
influence["Фруктовый салат"] = [1, 0, 0, 0, 0, 0]
influence["Готовый комплекс"] = [1, 0, 0, 0, 0, 0]
influence["Энергетик"] = [0, 0, 0, 0, 0, 0]
influence["Чипсы с чаем"] = [0, 0, 0, 0, 0, 0]
influence["Торт"] = [0, 0, 0, 0, 0, 1]

fridge = dict()
fridge["Каша"] = 1
fridge["Яичница с беконом"] = 1
fridge["Овощной салат"] = 1
fridge["Фруктовый салат"] = 0
fridge["Готовый комплекс"] = 0
fridge["Энергетик"] = 1
fridge["Чипсы с чаем"] = 2
fridge["Торт"] = 0

characteristics = [0] * 6

stage = 0
scene = 0
activity_type = -1
money = 1000
is_quest_activated = False
my_name = "Не_знаю_кто"
title = "анон"
last_message = "//Нету\\\\"

right_variants = dict()
right_variants[1] = {"/next"}
right_variants[5] = {"Еда"}


@bot.message_handler(commands=['start'])
def my_start(message):
    bot.send_message(message.from_user.id, start_text)


@bot.message_handler(commands=['reboot'])
def my_reboot(message):
    global activity_type

    activity_type = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Подтверждаю")
    btn2 = types.KeyboardButton("Нет, это ошибка!")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Вы точно хотите начать с начала?", reply_markup=markup)


@bot.message_handler(commands=['next'])
def my_next(message):
    game_manager(message)


@bot.message_handler(commands=['info'])
def my_info(message):
    global my_name, last_message, characteristics

    text = ('Привет, ' + my_name + "!" + '\nТекущая стадия: ' + str(stage) + ', сцена: ' + str(scene)
            + "\nПоследнее сообщение: <" + last_message + ">\n\nТекущие характеристики персонажа:\n")
    text = text + "Final_health: " + str(characteristics[0]) + '\n'
    text = text + "Final_physical: " + str(characteristics[1]) + '\n'
    text = text + "Final_prog_skills: " + str(characteristics[2]) + '\n'
    text = text + "Final_school_skills: " + str(characteristics[3]) + '\n'
    text = text + "Final_communication_skills: " + str(characteristics[4]) + '\n'
    text = text + "Final_happiness: " + str(characteristics[5])
    bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=['fridge'])
def my_fridge(message):
    global fridge

    text = 'Вот содержимое холодильника на данный момент:\n'
    for food in fridge:
        text = text + food + ': ' + str(fridge[food]) + '\n'

    bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=['echo'])
def my_echo(message):
    global all_activities, quest

    all_activities[5].extend(quest)
    bot.send_message(message.from_user.id, "Ауууу! Квест начался!")


@bot.message_handler(commands=['help'])
def my_help(message):
    bot.send_message(message.from_user.id, help_text)


@bot.message_handler(content_types=['text'])
def game_manager(message):
    global activity_type, situations, stage, scene, characteristics

    try:
        if activity_type == -1 and message.text == "/next":
            activity_type = situations[(stage, scene)][1]
            write_text(message, situations[(stage, scene)][0])
            if stage != 2 or scene != 2:
                scene += 1
                if scene == 3:
                    stage += 1
                    scene = 0
                if stage == 2 and scene == 2:
                    text = "Игра завершена. Ваши титулы по её окончанию:"
                    is_title = False
                    if characteristics[0] > 9:
                        text = text + '\n' + '- Ничего себе ты в жизни здоровая!'
                        is_title = True
                    if characteristics[1] > 1:
                        text = text + '\n' + '- Я фитоняша, да да я'
                        is_title = True
                    if characteristics[2] > 3:
                        text = text + '\n' + '- EMPRESS просто плачет в сторонке'
                        is_title = True
                    if characteristics[3] > 2:
                        text = text + '\n' + '- Отличниками не рождаются, отличниками становятся'
                        is_title = True
                    if characteristics[4] > 2:
                        text = text + '\n' + '- Я оратор, и сейчас я расскажу вам ваше мнение обо мне'
                        is_title = True
                    if characteristics[5] > 3:
                        text = text + '\n' + '- Идущая к просветлению'
                        is_title = True
                    if not is_title:
                        text = text + '\n' + '- Таких нет'
                    write_text(message, text)
        elif activity_type == 0:
            reboot_situation(message)
            activity_type = -1
        elif activity_type == 1:
            choice_situation(message)
        elif activity_type == 2:
            hello_situation(message)
        elif activity_type == 5:
            food_situation(message)
        elif activity_type == 9:
            street_situation(message)
        else:
            bot.send_message(message.from_user.id, hack_try, reply_markup=types.ReplyKeyboardRemove())
    except Exception:
        text = 'Программа вышла из чата. Просьба призвать богов ИКТ, они помогут'
        bot.send_message(message.from_user.id, text, reply_markup=types.ReplyKeyboardRemove())


def reboot_situation(message):
    global stage, scene, fridge, characteristics, activity_type, money, is_quest_activated, my_name, title, \
        last_message, right_variants, position_streets, count_streets

    if message.text == "Подтверждаю":
        fridge = dict()
        fridge["Каша"] = 1
        fridge["Яичница с беконом"] = 1
        fridge["Овощной салат"] = 1
        fridge["Фруктовый салат"] = 0
        fridge["Готовый комплекс"] = 0
        fridge["Энергетик"] = 1
        fridge["Чипсы с чаем"] = 2
        fridge["Торт"] = 0

        characteristics = [0] * 6

        stage = 0
        scene = 0
        position_streets = 0
        count_streets = 0
        activity_type = -1
        money = 1000
        is_quest_activated = False
        my_name = "Не_знаю_кто"
        title = "анон"
        last_message = "//Нету\\\\"

        right_variants = dict()
        right_variants[-1] = {"/next"}
        right_variants[1] = {"/next"}
        right_variants[5] = {"Еда"}
        f = open("girl's_chronicles.txt", 'w')
        f.close()
        bot.send_message(message.from_user.id, "Вы начали игру заново", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Нет, это ошибка!":
        bot.send_message(message.from_user.id, "Отмена перезагрузки", reply_markup=types.ReplyKeyboardRemove())
    else:
        write_text(message, hack_try)


def choice_situation(message):
    global stage, activity_type, all_activities, all_activities_texts, right_variants, characteristics, influence, \
        code_activities

    if message.text not in right_variants[1]:
        bot.send_message(message.from_user.id, hack_try)
    elif message.text == "/next":
        right_variants[1] = set()
        for word in all_activities[2 * stage]:
            right_variants[1].add(word)
        build_keyboard(message, right_variants[1])
    elif message.text in all_activities[2 * stage + 1]:
        change_characteristics(message)
        right_variants[1] = {"/next"}
        write_text(message, all_activities_texts[message.text])
        activity_type = -1
    elif message.text in right_variants[1]:
        change_characteristics(message)
        right_variants[1].discard(message.text)
        write_text(message, all_activities_texts[message.text])
        if message.text == "Еда":
            for word in all_activities[2 * stage + 1]:
                right_variants[1].add(word)
            activity_type = code_activities[message.text]
            food_situation(message)
        elif message.text == "Гулять с друзьями":
            activity_type = code_activities[message.text]
        else:
            build_keyboard(message, right_variants[1])
    else:
        bot.send_message(message.from_user.id, hack_try)


def hello_situation(message):
    global situations, activity_type, my_name, title

    if message.text.count(' ') != 1:
        bot.send_message(message.from_user.id, name_space_error, reply_markup=types.ReplyKeyboardRemove())
    else:
        activity_type = -1
        text = message.text + hello_text
        my_name, title = message.text.split()
        write_text(message, text)


def food_situation(message):
    global activity_type, fridge, right_variants

    if message.text not in right_variants[5]:
        bot.send_message(message.from_user.id, hack_try)
    elif message.text == "Еда":
        right_variants[5] = set()
        for food in fridge:
            if fridge[food] > 0:
                right_variants[5].add(food)
        build_keyboard(message, get_good_variants(fridge))
    elif message.text in right_variants[5]:
        change_characteristics(message)
        fridge[message.text] -= 1
        right_variants[5] = {"Еда"}
        activity_type = 1
        text = "Наверное, " + message.text + " лучший вариант"
        write_text(message, text)
        build_keyboard(message, right_variants[1])
    else:
        bot.send_message(message.from_user.id, hack_try)


def street_situation(message):
    global activity_type, position_streets, count_streets, street_dialogs

    if message.text != "/next":
        bot.send_message(message.from_user.id, hack_try)
    else:
        write_text(message, street_dialogs[count_streets][position_streets])
        position_streets += 1
        if len(street_dialogs[count_streets]) == position_streets:
            activity_type = 1
            build_keyboard(message, right_variants[1])
            count_streets += 1
            position_streets = 0


def build_keyboard(message, this_dict):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for key in this_dict:
        new_btn = types.KeyboardButton(key)
        markup.add(new_btn)

    bot.send_message(message.from_user.id, "Надо выбрать что-то из списка:", reply_markup=markup)


def write_text(message, string):
    global last_message

    last_message = string
    f = open("girl's_chronicles.txt", 'a')
    f.write(string + '\n')
    f.close()
    bot.send_message(message.from_user.id, string, reply_markup=types.ReplyKeyboardRemove())


def get_good_variants(some_dict):
    answer = list()
    for pair in some_dict:
        if some_dict[pair] > 0:
            answer.append(pair)

    return answer


def change_characteristics(message):
    global characteristics, influence

    changes = influence[message.text]
    for i in range(6):
        characteristics[i] += changes[i]


bot.polling(none_stop=True)
