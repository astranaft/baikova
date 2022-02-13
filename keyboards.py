import telebot

keyboardMain = telebot.types.ReplyKeyboardMarkup(True)
keyboardMain.row('Агрессия у подростка')
keyboardMain.row('Буллинг в классе')
keyboardMain.row('Стресс у подростка')
keyboardMain.row('Школьная тревожность')
keyboardMain.row('Конфликты с родителями')
keyboardMain.row('Неуверенность в себе')
keyboardMain.row('Неразделенная любовь')
keyboardMain.row('Связь со специалистом:')


prob1 = telebot.types.ReplyKeyboardMarkup(True)
prob1.row('Крикотерапия')
prob1.row('Гневный человек')
prob1.row('Рисование гнева')
prob1.row('Письмо гнева')
prob1.row('🔹 Главная')

prob2 = telebot.types.ReplyKeyboardMarkup(True)
prob2.row('Способ 1')
prob2.row('Способ 2')
prob2.row('Способ 3')
prob2.row('🔹 Главная')

prob3 = telebot.types.ReplyKeyboardMarkup(True)
prob3.row('Прогрессивное расслабление мышц')
prob3.row('Визуализация')
prob3.row('Диафрагмальное дыхание')
prob3.row('Выезд на природу/йога')
prob3.row('🔹 Главная')

prob4 = telebot.types.ReplyKeyboardMarkup(True)
prob4.row('Телефон горячей линии')
prob4.row('Телефон школьного психолога')
prob4.row('🔹 Главная')

prob5 = telebot.types.ReplyKeyboardMarkup(True)
prob5.row('Фильм')
prob5.row('"Храбрый герой"')
prob5.row('"Остров спокойствия"')
prob5.row('"Изображаем страх"')
prob5.row('🔹 Главная')

prob6 = telebot.types.ReplyKeyboardMarkup(True)
prob6.row('Шаг 1')
prob6.row('Шаг 2')
prob6.row('Шаг 3')
prob6.row('Шаг 4')
prob6.row('🔹 Главная')

prob7 = telebot.types.ReplyKeyboardMarkup(True)
prob7.row('Окружение')
prob7.row('Литература')
prob7.row('Зона комфорта')
prob7.row('Долой самокритику!')
prob7.row('🔹 Главная')

prob8 = telebot.types.ReplyKeyboardMarkup(True)
prob8.row('Решение 1')
prob8.row('Решение 2')
prob8.row('Решение 3')
prob8.row('Решение 4')
prob8.row('🔹 Главная')







kategor1 = telebot.types.ReplyKeyboardMarkup(True)
kategor1.row('СК (син.крис)','Гашиш')
kategor1.row('MEPHEDRONE крис','РОСС')




oplata = telebot.types.ReplyKeyboardMarkup(True)
oplata.row('Qiwi')
oplata.row('Bitcoin')

oplata_oplatil = telebot.types.ReplyKeyboardMarkup(True)
oplata_oplatil.row('Оплатил','Отменить')

admin = telebot.types.ReplyKeyboardMarkup(True)
admin.row('Изменить Карту','Изменить Qiwi', 'изменить bitcoin')
admin.row('Количество пользователей')
admin.row('🔹 Главная')


yes_no = telebot.types.ReplyKeyboardMarkup(True)
yes_no.row('Да','Нет')