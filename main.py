import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from random import choice


class StaticPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller

        page_config = cfg.STATIC_PAGES_DATA[page_name]

        label_data = cfg.STATIC_MESSAGES[page_config['message_key']]

        for idx, (text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=page_config['font']
            )
            label.place(
                relx=0.5,
                rely=page_config['rely_start']
                    + (idx * page_config['rely_step']),
                anchor='c'
            )

        commands_map = {
            'exit': controller.exit_app,
            'rules': lambda: controller.switch_to('RulesPage'),
            'start': controller.create_app
        }

        for idx, (text, cmd_key) in enumerate(
            page_config['buttons']
        ):
            button = ctk.CTkButton(
                self,
                text=text,
                command=commands_map[cmd_key],
                **cfg.BTN_PARAMS
            )
            button.place(
                relx=0.35 + (idx * 0.3),
                rely=page_config['btn_rely'],
                anchor='c'
            )


class ChoicePage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller
        self.page_name = page_name
        self.page_config = cfg.CHOICE_PAGES_DATA[page_name]

        label = ctk.CTkLabel(
            self,
            text=self.page_config['question'],
            text_color=cfg.LIME_COLOR,
            font=cfg.BIG_FONT
        )
        label.place(relx=0.5, rely=0.3, anchor='c')

        self.choice_var = ctk.StringVar(
            value=self.page_config['default_value']
        )

        for idx, (value, text) in enumerate(
            self.page_config['options']
        ):
            box = ctk.CTkRadioButton(
                self,
                text=text,
                variable=self.choice_var,
                value=value,
                **cfg.BOX_PARAMS
            )
            box.place(
                relx=0.3 + (idx * 0.4),
                rely=self.page_config['box_rely'],
                anchor='c'
            )

        button_data = [
            ('Назад', lambda: self.controller.switch_to(
                self.page_config['back_page'])),
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
                rely=0.85, anchor='c'
            )

    def send_info(self):
        info = self.choice_var.get()
        self.controller.transfer_info(self.page_name, info)
        self.controller.switch_to(self.page_config['next_page'])

    def update_data(self):
        self.choice_var.set(self.page_config['default_value'])


class InputPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.DARK_COLOR)
        self.controller = controller
        self.page_name = page_name
        self.page_config = cfg.ENTRY_PAGES_DATA[page_name]

        for text, color, font, rely in self.page_config['labels']:
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
            **self.page_config['entry_params']
        )
        self.entry.place(
            relx=0.5,
            rely=0.55,
            anchor='c'
        )

        back_page = self.page_config['back_page']

        button_data = [
            ('Назад', lambda: self.controller.switch_to(back_page)),
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
        info = self.entry.get()
        self.controller.transfer_info(self.page_name, info)

    def get_status(self, status, result=None):
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

        if self.page_config['next_action'] == 'switch':
            self.controller.switch_to('TextPage')

        elif self.page_config['next_action'] == 'finalize':
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

            result = self.generate_code()

            return 'success', result

    def generate_code(self):
        mode = self.main_data['mode']
        language = self.main_data['language']
        step = int(self.main_data['step'])
        text =  self.main_data['text']

        direction = 1 if mode == 'encrypt' else -1
        shift = step * direction

        alphabet_map = {
            ('rus', True): cfg.up_rus_chars,
            ('rus', False): cfg.low_rus_chars,
            ('eng', True): cfg.up_eng_chars,
            ('eng', False): cfg.low_eng_chars
        }

        result = ''
        for char in text:
            if char.isalpha():
                alphabet = alphabet_map.get((language, char.isupper()))
                x = alphabet.index(char)
                new_index = (x + shift) % len(alphabet)
                result += alphabet[new_index]
            else:
                result += char

        return result


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

        page_types = [
            (cfg.STATIC_PAGES_DATA, StaticPage),
            (cfg.CHOICE_PAGES_DATA, ChoicePage),
            (cfg.ENTRY_PAGES_DATA, InputPage)
        ]

        for config_dict, page_class in page_types:
            for page_name in config_dict.keys():
                self.pages[page_name] = page_class(
                    master=self.main_frame,
                    controller=self,
                    page_name=page_name
                )

        for page_class in (MessagePage, FinalPage):
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