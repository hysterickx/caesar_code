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
            (
                'Выйти',
                self.controller.exit_app
            ),
            (
                'Вперёд!',
                lambda: self.controller.switch_to('RulesPage')
            )
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

        self.mode_var = ctk.StringVar(value='encrypt')

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

    def update_data(self):
        self.mode_var.set('encrypt')


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

        self.lang_var = ctk.StringVar(value='rus')
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

    def update_data(self):
        self.lang_var.set('rus')


class StepPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        label_data = [
            ('Введите шаг сдвига', cfg.LIME_COLOR, cfg.BIG_FONT, 0.3),
            ('(от 1 до 33)', cfg.WHITE_COLOR, cfg.LIT_FONT, 0.4)
        ]

        for text, color, font, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(
                relx=0.5,
                rely=rely,
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
            error_message = ctk.CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[status],
                **cfg.MSG_PARAMS
            )

            self.wait_window(error_message)
            self.entry.delete(0, 'end')
            self.entry.focus()
            return

        self.controller.switch_to('TextPage')

    def update_data(self):
        self.entry.delete(0, 'end')


class TextPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        label_data = [
            (
                'Введите ваш текст',
                cfg.LIME_COLOR, cfg.BIG_FONT, 0.3
            ),
            (
                '(не более 50 символов)',
                cfg.WHITE_COLOR, cfg.LIT_FONT, 0.4
            )
        ]

        for text, color, font, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(
                relx=0.5,
                rely=rely,
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
            (
                'Назад',
                lambda: self.controller.switch_to('StepPage')
            ),
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
            error_message = ctk.CTkMessagebox(
                self.controller,
                message=cfg.ERROR_MESSAGES[status],
                **cfg.MSG_PARAMS
            )

            self.wait_window(error_message)
            self.entry.delete(0, 'end')
            self.entry.focus()
            return

        self.controller.transfer_final_info(
            self.entry.get(),
            result
        )

    def update_data(self):
        self.entry.delete(0, 'end')


class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        frames = {}

        frame_data = [
            ('text_frame', 0),
            ('result_frame', 0.3)
        ]

        for name, rely in frame_data:
            frame = ctk.CTkFrame(
                self,
                fg_color=cfg.DARK_COLOR
            )
            frame.place(
                relx=0, rely=rely ,
                relwidth=1.0, relheight=0.3
            )
            frames[name] = frame

        self.labels = {}

        label_data = [
            ('text_label', cfg.WHITE_COLOR, frames['text_frame']),
            ('result_label', cfg.LIME_COLOR, frames['result_frame'])
        ]

        for name, color, frame in label_data:
            label = ctk.CTkLabel(
                frame,
                text_color=color,
                font=cfg.MID_FONT,
                wraplength=550,
                justify='center'
            )
            label.pack(
                pady=10,
                padx=10,
                fill='both',
                expand=True,
            )
            self.labels[name] = label

        label = ctk.CTkLabel(
            self,
            text='Хотите повторить?',
            text_color=cfg.WHITE_COLOR,
            font=cfg.BIG_FONT
        )
        label.place(
            relx=0.5,
            rely=0.8,
            anchor='c'
        )

        button_data = [
            ('Не хочу', self.controller.exit_app, 0.35, 0.92),
            (
                'Давай',
                lambda: self.controller.create_app(restart=True),
                0.65, 0.92
            ),
            ('copy', lambda: copy(self.result), 0.5, 0.65)
        ]

        for text, command, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=relx,
                rely=rely,
                anchor='c'
            )

    def get_result(self, text, result):
        self.result = result
        self.labels['text_label'].configure(
            text=f'Твой изначальный текст:\n{text}'
        )
        self.labels['result_label'].configure(
            text=f'Результат шифрования:\n{result}'
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


class MainLogic:
    def __init__(self):
        self.main_data = {
            'mode': 'encrypt',
            'language': 'rus',
            'step': '',
            'text': ''
        }

    def get_info(self, page, info):
        if page in ('ModePage', 'LanguagePage'):
            self.main_data[page[:-4].lower()] = info
            return 'success', []

        if page == 'StepPage':
            if not info:
                return 'empty', []

            if not info.isdigit():
                return 'not_digit', []

            step_val = int(info)
            if not (1 <= step_val <= 33):
                if step_val < 1:
                    return 'too_small', []
                return 'too_big', []

            self.main_data['step'] = info
            return 'success', []

        if page == 'TextPage':
            if not info:
                return 'empty', []

            if len(info) > 50:
                return 'too_many', []

            language = self.main_data['language']

            if language == 'rus':
                allowed_chars = cfg.low_rus_chars + cfg.up_rus_chars
            else:
                allowed_chars = cfg.low_eng_chars + cfg.up_eng_chars

            if any(char.isalpha()
                    and char not in allowed_chars for char in info):
                return f'only_{language}', []

            self.main_data['text'] = info
            mode = self.main_data['mode']
            step = int(self.main_data['step'])

            direction = 1 if mode == 'encrypt' else -1
            shift = step * direction

            alphabet_map = {
                ('rus', True): cfg.up_rus_chars,
                ('rus', False): cfg.low_rus_chars,
                ('eng', True): cfg.up_eng_chars,
                ('eng', False): cfg.low_eng_chars
            }

            result = ''
            for char in info:
                if char.isalpha():
                    alphabet = alphabet_map.get((language, char.isupper()))
                    x = alphabet.index(char)
                    new_index = (x + shift) % len(alphabet)
                    result += alphabet[new_index]
                else:
                    result += char

            return 'success', result


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Caesar Code')
        self.geometry('600x500+800+450')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.main_logic = MainLogic()
        self.is_first_load = True
        self.pages = {}
        self.current_frame = None

        for page_class in(
            GreetingsPage, RulesPage,
            MessagePage, ModePage, LanguagePage,
            StepPage, TextPage, FinalPage
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

    def transfer_final_info(self, text, result):
        self.pages['MessagePage'].change_message('waiting')
        self.switch_to('MessagePage')
        self.pages['FinalPage'].get_result(text, result)
        self.after(3000, lambda: self.switch_to('FinalPage'))

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

            for page in self.pages.values():
                if hasattr(page, 'update_data'):
                    page.update_data()

            self.after(3000, lambda: self.switch_to("ModePage"))
            return

        self.switch_to("ModePage")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()