COLOR_DARK = '#0d0a0c'
COLOR_LIME = '#99ff66'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#ffffff'

FONT_VERY_LARGE = ('Constantia', 35, 'bold')
FONT_LARGE = ('Constantia', 30)
FONT_MEDIUM = ('Constantia', 25)
FONT_SMALL = ('Constantia', 20)

low_eng_chars = 'abcdefghijklmnopqrstuvwxyz'
up_eng_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_rus_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
up_rus_chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

BOX_PARAMS = {
    "font": FONT_MEDIUM,
    "text_color": COLOR_WHITE,
    "fg_color": COLOR_LIME,
    "border_color": COLOR_WHITE,
    "hover_color": COLOR_LIME,
    "border_width_checked": 5,
    "border_width_unchecked": 1
}

MINI_ENTRY_PARAMS = {
    "width": 100,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": FONT_LARGE
}

ENTRY_PARAMS = {
    "width": 500,
    "height": 30,
    "border_width": 0,
    "corner_radius": 40,
    "justify": 'c',
    "font": FONT_LARGE
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": COLOR_WHITE,
    "button_hover_color": COLOR_LIME,
    "button_text_color": COLOR_BLACK
}

BTN_PARAMS = {
    "width": 70,
    "height": 50,
    "corner_radius": 50,
    "fg_color": COLOR_LIME,
    "hover_color": COLOR_WHITE,
    "text_color": COLOR_BLACK,
    "font": FONT_SMALL
}

STATIC_PAGES_DATA = {
    'GreetingsPage': {
        'labels': [
            ('Приветствую!', COLOR_LIME, FONT_LARGE, 0.5, 0.15),
            ('Эта программа поможет тебе', COLOR_WHITE, FONT_LARGE, 0.5, 0.3),
            ('создать Шифр Цезаря', COLOR_LIME, FONT_LARGE, 0.5, 0.45),
            ('а также дешифровать его!', COLOR_WHITE, FONT_LARGE, 0.5, 0.6)
        ],
        'buttons': [
            ('Выйти', 'close_app', 0.35, 0.9),
            ('Далее', 'RulesPage', 0.65, 0.9)
        ]
    },
    'RulesPage': {
        'labels': [
            ('Шифр Цезаря - это метод шифрования', COLOR_LIME, FONT_SMALL, 0.5, 0.1),
            ('при котором каждая буква текста', COLOR_WHITE, FONT_SMALL, 0.5, 0.18),
            ('заменяется другой, отстоящей', COLOR_LIME, FONT_SMALL, 0.5, 0.26),
            ('на фиксированное количество позиций', COLOR_WHITE, FONT_SMALL, 0.5, 0.34),
            ('правее по алфавиту', COLOR_LIME, FONT_SMALL, 0.5, 0.42),
            ('', COLOR_LIME, FONT_SMALL, 0.5, 0.5),
            ('Например, при шифровке с шагом равным 3', COLOR_WHITE, FONT_SMALL, 0.5, 0.58),
            ('«А» превращается в «Г»', COLOR_LIME, FONT_SMALL, 0.5, 0.66),
            ('а при дешифровке с шагом равным 5', COLOR_WHITE, FONT_SMALL, 0.5, 0.74),
            ('«Ж» превращается в «В»', COLOR_LIME, FONT_SMALL, 0.5, 0.82)
        ],
        'buttons': [
            ('Начнём', 'start_app', 0.5, 0.9)
        ]
    }
}

CHOICE_PAGES_DATA = {
    'ModePage': {
        'label_txt': 'Нужно зашифровать\n\n или\n\n дешифровать код?',
        'default_value': 'encrypt',
        'boxes': [
            ('Зашифровать', 'encrypt', 0.3, 0.6),
            ('Дешифровать', 'decrypt', 0.7, 0.6)
        ],
        'buttons': [
            ('Назад', 'RulesPage', 0.35, 0.8),
            ('Далее', 'transfer_info', 0.65, 0.8)
        ]
    },
    'LanguagePage': {
        'label_txt': 'На каком языке\n\nваш текст?',
        'default_value': 'rus',
        'boxes': [
            ('Русский', 'rus', 0.3, 0.6),
            ('Английский', 'eng', 0.7, 0.6)
        ],
        'buttons': [
            ('Назад', 'ModePage', 0.35, 0.8),
            ('Далее', 'transfer_info', 0.65, 0.8)
        ]
    }
}

INPUT_PAGES_DATA = {
    'StepPage': {
        'labels': [
            ('Введите шаг сдвига', COLOR_LIME, FONT_LARGE, 0.5, 0.3),
            ('(от 1 до 33)', COLOR_WHITE, FONT_SMALL, 0.5, 0.4)
        ],
        'buttons': [
            ('Назад', 'LanguagePage', 0.35, 0.8),
            ('Далее', 'transfer_info', 0.65, 0.8)
        ]
    },
    'TextPage': {
        'labels': [
            ('Введите ваш текст', COLOR_LIME, FONT_LARGE, 0.5, 0.3),
            ('(не более 50 символов)', COLOR_WHITE, FONT_SMALL, 0.5, 0.4)
        ],
        'buttons': [
            ('Назад', 'StepPage', 0.35, 0.8),
            ('Далее', 'transfer_info', 0.65, 0.8)
        ]
    }
}

FINAL_PAGE_DATA = {
    'frames': [
        ('input_frame', 0, 0, 1.0, 0.3),
        ('result_frame', 0, 0.3, 1.0, 0.3)
    ],
    'labels': [
        ('input_frame', 'input_label', COLOR_WHITE, FONT_MEDIUM),
        ('result_frame', 'result_label', COLOR_LIME, FONT_LARGE)
    ],
    'static_txt': 'Хотите повторить?',
    'buttons': [
        ('Не хочу', 'close_app', 0.35, 0.8),
        ('Давай', 'start_app', 0.65, 0.8)
    ]
}

DELAY_MESSAGES = {
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
    'too_big': 'Шаг не может быть больше 33',
    'too_many': 'Слишком большой текст',
    'only_rus': 'Не допускаются английские буквы',
    'only_eng': 'Не допускаются русские буквы'
}

