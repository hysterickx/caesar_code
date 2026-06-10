DARK_COLOR = '#0d0a0c'
LIME_COLOR = '#99ff66'
BLACK_COLOR = '#000000'
WHITE_COLOR = '#ffffff'

BIG_FONT = ('Constantia', 30)
MID_FONT = ('Constantia', 25)
LIT_FONT = ('Constantia', 20)

BOX_PARAMS = {
    "font": MID_FONT,
    "text_color": WHITE_COLOR,
    "fg_color": LIME_COLOR,
    "border_color": WHITE_COLOR,
    "hover_color": LIME_COLOR,
    "border_width_checked": 5,
    "border_width_unchecked": 1
}

ENTRY_PARAMS_1 = {
    "width": 100,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": BIG_FONT
}

ENTRY_PARAMS_2 = {
    "width": 500,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": BIG_FONT
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": WHITE_COLOR,
    "button_hover_color": LIME_COLOR,
    "button_text_color": BLACK_COLOR
}

BTN_PARAMS = {
    "width": 70,
    "height": 50,
    "corner_radius": 50,
    "fg_color": LIME_COLOR,
    "hover_color": WHITE_COLOR,
    "text_color": BLACK_COLOR,
    "font": LIT_FONT
}

STATIC_MESSAGES = {
    'greetings': [
        ('Приветствую!', LIME_COLOR),
        ('Эта программа поможет тебе', WHITE_COLOR),
        ('создать Шифр Цезаря', LIME_COLOR),
        ('а также дешифровать его!', WHITE_COLOR)
    ],
    'rules': [
        ('Шифр Цезаря - это метод шифрования', LIME_COLOR),
        ('при котором каждая буква текста', WHITE_COLOR),
        ('заменяется другой, отстоящей', LIME_COLOR),
        ('на фиксированное количество позиций', WHITE_COLOR),
        ('правее по алфавиту', LIME_COLOR),
        ('', LIME_COLOR),
        ('Например, при шифровке с шагом равным 3', WHITE_COLOR),
        ('«А» превращается в «Г»', LIME_COLOR),
        ('а при дешифровке с шагом равным 5', WHITE_COLOR),
        ('«Ж» превращается в «В»', LIME_COLOR)
    ]
}

ACTIVE_MESSAGES = {
    'waiting': [
        'Жду ответа от сервера...', 'Посылаю запрос...',
        'Нужно немного подождать...', 'Дай-ка подумать...',
        'Получаю твой ответ...'
    ],
    'loading': [
        'Генерирую цикл...',
        'Создаю всё с нуля...',
        'Очищаю всё лишнее...',
        'Отлично! Начинаем...',
        'Дай мне пару секундочек!'
    ],
    'farewell': [
        'До новых встреч!',
        'Заглядывай ко мне ещё!',
        'Был рад поработать с тобой!',
        'Ты это, заходи, если что...',
        'Надеюсь, еще увидимся!'
    ]
}

ERROR_MESSAGES = {
    'empty': 'В поле пусто',
    'not_digit': 'Нужно ввести именно число',
    'too_small': 'Шаг не может быть меньше 1',
    'too_big': 'Шаг не может быть больше 26',
    'too_many': 'Слишком большой текст',
    'only_rus': 'Не допускаются английские буквы',
    'only_eng': 'Не допускаются русские буквы'
}

low_eng_chars = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
up_eng_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_rus_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
up_rus_chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'