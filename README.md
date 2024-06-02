# Проект "Интерактивное приключение"

Выполнил Павлов Кирилл

Приветствуем вас в проекте мини-игры "День разработчика"!
Здесь находиться описание основных компонентов реализованного чат-бота

## Легенда проекта

Мы проходим небольшое путешествие от лица школьницы-разработчика игр, и видим основные аспекты её жизни. Присутствуют
разнообразные выборы, от которых будет зависеть титул или даже набор титулов, которые игрок получит в процессе игры.
Титулы зарабатываются в зависимости от показателей, которые меняются из-за разных выборов, которые делает персонаж в
течение дня. Внутри спрятана пасхалка, которую можно обнаружить как минимум 2 разными способами. Поэтому игру можно
пройти как минимум несколькими способами - дерзайте, исследуйте развилки, которые вам предоставляет сюжет

## Игра

Осуществляется или через кнопки, или через текст, или через команду "/next". Команда отправляет пользователю новое
сообщение или начало цепочки команд, иначе пользователю предлагается выбрать вариант через кнопку или ввести текст.
Данные сохраняются в файл "girl's_chronicles.txt", его можно воспринимать как логи программы и как законченную историю.


## Тонкости работы программы:

Команды, доступные пользователю:
- /start - выводит стартовое сообщение
- /next - выдает пользователю новое событие
- /reboot - перезапускает историю
- /info - даёт информацию о текущем состоянии игры
- /fridge - показывает количество продуктов в холодильнике
- /echo - начинает квест-пасхалку
- /help - команда для информации по всем командам


Основы движения сюжета - переменной activity_type, которая отвечает за текущее действие. Коды переменной activity_type:
- -1 - нет активности
- 0 - сброс истории
- 1 - выбор активностей
- 2 - приветствие
- 3 - занятие спортом
- 4 - гигиена
- 5 - прием пищи
- 6 - поход в школу
- 7 - изучение Python
- 8 - просмотр ютуб
- 9 - гуляние с друзьями
- 10 - спортзал
- 11 - выполнение домашней работы
- 12 - поход в магазин
- 13 - подготовка ко сну
- 14 - создание игру
- 15 - квест

## Соответствие критериям 
1. Реализована мини-игра, которая не ломается и выполняет поставленные ей задачи
2. Бот может заканчивать работу с большим количеством выводов, который не ограничен 10 вариантами.
3. В программе присутствует большое количество циклов
4. Бот использует много функций для корректной работы: my_start(), my_reboot(), my_next(), my_info(), my_fridge(),
my_echo(), my_help(), game_manager(), reboot_situation(), choice_situation(), hello_situation(), food_situation(),
street_situation(), build_keyboard(), write_text(), get_good_variants(), change_characteristics()
5. программе используется множество методов списков, множеств и строк
6. Словари используются разумно
7. Данные вывода записываются в файл
8. Проверена защита от попыток ломания, бот держит большинство вводов, корректно обрабатывает все ожидаемые варианты.
9. Ошибки pep8 отсутствуют
