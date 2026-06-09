import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from random import choice
import re


class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        for idx, (text, color) in enumerate(
            cfg.STATIC_MESSAGES['greetings']
        ):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=cfg.BIG_FONT
            )
            label.place(
                relx=0.5,
                rely=0.15 + (idx * 0.17),
                anchor='c'
            )

        button_data = [
            ('Выйти', self.controller.exit_app),
            ('Вперёд!', lambda: self.controller.switch_to('RulesPage'))
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.85,
                anchor='c'
            )


class RulesPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        for idx, (text, color) in enumerate(
            cfg.STATIC_MESSAGES['rules']
        ):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=cfg.MID_FONT
            )
            label.place(
                relx=0.5,
                rely=0.05 + (idx * 0.08),
                anchor='c'
            )

        button_data = [
            ('Выйти', self.controller.exit_app),
            ('Отлично', self.controller.create_app)
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.9,
                anchor='c'
            )


class ModePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        label = ctk.CTkLabel(
            self,
            text='Нужно зашифровать\n\n или\n\n дешифровать код?',
            text_color=cfg.LIME_COLOR,
            font=cfg.BIG_FONT
        )

        label.place(
            relx=0.5,
            rely=0.3,
            anchor='c'
        )

        self.mode_var = ctk.StringVar(value = 'encrypt')

        box_data = [
            ('encrypt', 'Зашифровать'),
            ('decrypt', 'Дешифровать')
        ]

        for idx, (value, text) in enumerate(box_data):
            box = ctk.CTkRadioButton(
                self,
                text=text,
                variable=self.mode_var,
                value=value,
                **cfg.BOX_PARAMS
            )

            box.place(
                relx=0.3 + (idx*0.4),
                rely=0.65,
                anchor='c'
            )

        button_data = [
            ('Назад', lambda: self.controller.switch_to('RulesPage')),
            ('Далее', self.send_info)
        ]


        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )

            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.85,
                anchor='c'
            )

    def send_info(self):
        page = 'ModePage'
        info = self.mode_var.get()

        self.controller.transfer_info(page, info)
        self.controller.switch_to('LanguagePage')


class LanguagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        label = ctk.CTkLabel(
            self,
            text='На каком языке\n\nваш текст?',
            text_color=cfg.LIME_COLOR,
            font=cfg.BIG_FONT
        )

        label.place(
            relx=0.5,
            rely=0.3,
            anchor='c'
        )

        self.lang_var = ctk.StringVar(value = 'rus')

        box_data = [
            ('rus', 'Русский'),
            ('eng', 'Английский')
        ]

        for idx, (value, text) in enumerate(box_data):
            box = ctk.CTkRadioButton(
                self,
                text=text,
                variable=self.lang_var,
                value=value,
                **cfg.BOX_PARAMS
            )

            box.place(
                relx=0.3 + (idx*0.4),
                rely=0.6,
                anchor='c'
            )

        button_data = [
            ('Назад', lambda: self.controller.switch_to('ModePage')),
            ('Далее', self.send_info)
        ]


        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )

            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.85,
                anchor='c'
            )

    def send_info(self):
        page = 'LanguagePage'
        info = self.lang_var.get()

        self.controller.transfer_info(page, info)
        self.controller.switch_to('StepPage')


class StepPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        label = ctk.CTkLabel(
            self,
            text='Введите шаг сдвига',
            text_color=cfg.LIME_COLOR,
            font=cfg.BIG_FONT
        )

        label.place(
            relx=0.5,
            rely=0.3,
            anchor='c'
        )

        label = ctk.CTkLabel(
            self,
            text='(от 1 до 30)',
            text_color=cfg.WHITE_COLOR,
            font=cfg.LIT_FONT
        )

        label.place(
            relx=0.5,
            rely=0.4,
            anchor='c'
        )

        self.entry = ctk.CTkEntry(
            self,
            **cfg.ENTRY_PARAMS_1
        )

        self.entry.place(
            relx=0.5,
            rely=0.55,
            anchor='c'
        )

        button_data = [
            ('Назад', lambda: self.controller.switch_to('LanguagePage')),
            ('Далее', self.send_info)
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )

            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.75,
                anchor='c'
            )

    def send_info(self):
        page = 'StepPage'
        info = self.entry.get()

        self.controller.transfer_info(page, info)

    def get_status(self, status):
        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[status],
                **cfg.MSG_PARAMS
            )

            self.wait_window(error_message)
            self.entry.delete(0, 'end')
            self.entry.focus()
            return

        self.controller.switch_to('TextPage')


class TextPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        label = ctk.CTkLabel(
            self,
            text='Введите ваш текст',
            text_color=cfg.LIME_COLOR,
            font=cfg.BIG_FONT
        )

        label.place(
            relx=0.5,
            rely=0.3,
            anchor='c'
        )

        label = ctk.CTkLabel(
            self,
            text='(не более 100 символов)',
            text_color=cfg.WHITE_COLOR,
            font=cfg.LIT_FONT
        )

        label.place(
            relx=0.5,
            rely=0.4,
            anchor='c'
        )

        self.entry = ctk.CTkEntry(
            self,
            **cfg.ENTRY_PARAMS_2
        )

        self.entry.place(
            relx=0.5,
            rely=0.55,
            anchor='c'
        )

        button_data = [
            ('Назад', lambda: self.controller.switch_to('StepPage')),
            ('Далее', self.send_info)
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )

            button.place(
                relx=0.35 + (idx * 0.3),
                rely=0.75,
                anchor='c'
            )

    def send_info(self):
        page = 'TextPage'
        info = self.entry.get()

        self.controller.transfer_info(page, info)

    def get_status(self, status, result):
        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[status],
                **cfg.MSG_PARAMS
            )

            self.wait_window(error_message)
            self.entry.delete(0, 'end')
            self.entry.focus()
            return




class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        self.label = ctk.CTkLabel(
            self,
            text='',
            text_color=cfg.LIME_COLOR,
            font=cfg.BIG_FONT
        )
        self.label.place(
            relx=0.5,
            rely=0.5,
            anchor='c'
        )

    def change_message(self, status):
        self.label.configure(
            text=choice(cfg.ACTIVE_MESSAGES[status])
        )


class MainLogic():
    def __init__(self):

        self.main_data = {
            'mode': 'encrypt',
            'language': 'rus',
            'step': '1',
            'text': ''
        }

    def get_info(self, page, info):
        if page == 'ModePage':
            self.main_data['mode'] = info
            return {}, []

        if page == 'LanguagePage':
            self.main_data['language'] = info
            return {}, []

        if page == 'StepPage':
            if len(info) == 0:
                return 'empty', []

            if not info.isdigit():
                return 'not_digit', []

            if int(info) < 1:
                return 'too_small', []

            if int(info) > 30:
                return 'too_big', []

            self.main_data['step'] = info
            return 'success', []

        if page == 'TextPage':
            if len(info) == 0:
                return 'empty', []

            if len(info) > 100:
                return 'too_many', []

            if self.main_data['language'] == 'rus' and re.search(r'[a-z]', info, re.IGNORECASE):
                return 'only_rus', []

            if self.main_data['language'] == 'eng' and re.search(r'[а-яё]', info, re.IGNORECASE):
                return 'only_eng', []

            self.main_data['text'] = info

            print(self.main_data)

            mode = self.main_data['mode']
            language = self.main_data['language']
            step = self.main_data['step']
            text = self.main_data['text']
            low_rus = cfg.low_rus_chars
            up_rus = cfg.up_rus_chars
            low_eng = cfg.low_eng_chars
            up_eng = cfg.up_eng_chars
            result = ''

            for char in text:
                if char.isalpha():
                    if language == 'rus':
                        if mode == 'encrypt':
                            if char.isupper():
                                x = up_rus.index(char)
                                result += up_rus[x + int(step)]
                            else:
                                x = low_rus.index(char)
                                result += low_rus[x + int(step)]
                        if mode == 'decrypt':
                             if char.isupper():
                                x = up_rus.index(char)
                                result += up_rus[x - int(step)]
                             else:
                                x = low_rus.index(char)
                                result += low_rus[x - int(step)]

                    if language == 'eng':
                        if mode == 'encrypt':
                            if char.isupper():
                                x = up_eng.index(char)
                                result += up_eng[x + int(step)]
                            else:
                                x = low_eng.index(char)
                                result += low_eng[x + int(step)]
                        if mode == 'decrypt':
                            if char.isupper():
                                x = up_eng.index(char)
                                result += up_eng[x - int(step)]
                            else:
                                x = low_eng.index(char)
                                result += low_eng[x - int(step)]
                else:
                    result += char

            print(result)

            return 'success', result


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title ('Caesar Code')
        self.geometry ('600x500+800+450')
        self.resizable (False, False)
        self.attributes ('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.main_logic = MainLogic()
        self.is_first_load = True
        self.pages = {}
        self.current_frame = None

        for page_class in(
            GreetingsPage, RulesPage,
            MessagePage, ModePage, LanguagePage,
            StepPage, TextPage
        ):
            page_name = page_class.__name__
            self.pages[page_name] = page_class(
                master=self.main_frame,
                controller=self
            )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def transfer_info(self, page, info):
        status, result = self.main_logic.get_info(page, info)
        if page == 'StepPage':
            self.pages['StepPage'].get_status(status)
        if page == 'TextPage':
            self.pages['TextPage'].get_status(status, result)

    def exit_app(self):
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

    def create_app(self, restart=False):
        if restart:
            self.is_first_load = True

        if self.is_first_load:
            self.pages['MessagePage'].change_message('loading')
            self.switch_to('MessagePage')
            self.is_first_load = False
            self.after(3000, lambda: self.switch_to("ModePage"))
            return

        self.switch_to("ModePage")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()