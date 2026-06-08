import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from random import choice


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


class CodePage(ctk.CTkFrame):
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
                relx=0.33 + (idx*0.4),
                rely=0.6,
                anchor='c'
            )

        button_data = [
            ('Назад', lambda: self.controller.switch_to('RulesPage')),
            ('Далее', lambda: self.controller.switch_to('LanguagePage'))
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


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title ('Caesar Code')
        self.geometry ('600x500+800+450')
        self.resizable (False, False)
        self.attributes ('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.is_first_load = True
        self.main_data = {
            'mode': 'encrypt',
            'lang': 'ru',
            'step': 1,
            'text': ''
        }

        self.pages = {}
        self.current_frame = None

        for page_class in(
            GreetingsPage, RulesPage,
            MessagePage, CodePage):
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
            self.after(3000, lambda: self.switch_to("CodePage"))
            return

        self.switch_to("CodePage")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()