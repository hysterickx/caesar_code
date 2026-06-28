import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pyperclip import copy
import config as cfg
from random import choice
from functools import partial


class StaticPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        page_config = cfg.STATIC_PAGES_DATA[page_name]

        label_data = page_config['labels']
        for text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx, rely=rely, anchor='c')

        button_data = page_config['buttons']
        for text, cmd_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(
                    controller.handle_command, cmd_key
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')


class ChoicePages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller
        self.page_name = page_name
        page_config = cfg.CHOICE_PAGES_DATA[page_name]

        label_txt = page_config['label_txt']
        label = ctk.CTkLabel(
            self,
            text=label_txt,
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_LARGE
        )
        label.place(relx=0.5, rely=0.3, anchor='c')

        self.default_value = page_config['default_value']
        self.choice_var = ctk.StringVar(
            value=self.default_value
        )

        box_data = page_config['boxes']
        for text, value, relx, rely in box_data:
            box = ctk.CTkRadioButton(
                self,
                text=text,
                variable=self.choice_var,
                value=value,
                **cfg.BOX_PARAMS
            )
            box.place(relx=relx, rely=rely, anchor='c')

        button_data = page_config['buttons']
        for text, cmd_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(
                    self.send_info, cmd_key
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')

    def send_info(self, cmd_key):
        user_input = self.choice_var.get()
        page = self.page_name
        self.controller.handle_command(
            cmd_key, page, user_input
        )

    def update_ui(self):
        self.choice_var.set(self.default_value)


class InputPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller
        self.page_name = page_name
        page_config = cfg.INPUT_PAGES_DATA[page_name]

        label_data = page_config['labels']
        for text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx, rely=rely, anchor='c')

        entry_data = page_config['entry_params']
        self.entry = ctk.CTkEntry(
            self,
            **entry_data
        )
        self.entry.place(relx=0.5, rely=0.55, anchor='c')

        button_data = page_config['buttons']
        for text, cmd_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(
                    self.send_info, cmd_key
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')

    def send_info(self, cmd_key):
        page = self.page_name
        user_input = self.entry.get()
        self.controller.handle_command(
            cmd_key, page, user_input
        )

    def show_error(self, status):
        error_message = CTkMessagebox(
            app,
            message=cfg.ERROR_MESSAGES[status],
            **cfg.MSG_PARAMS
        )
        self.wait_window(error_message)
        self.entry.delete(0, 'end')
        self.entry.focus()

    def set_focus(self):
        self.entry.focus()

    def update_ui(self):
        self.entry.delete(0, 'end')


class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.labels = {}
        label_data = cfg.FINAL_PAGE_DATA['labels']
        for name, text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font,
                wraplength=550,
                justify='center'
            )
            label.place(relx=relx, rely=rely, anchor='c')
            self.labels[name] = label

        button_data = cfg.FINAL_PAGE_DATA['buttons']
        cmd_map = {
            'exit': lambda: controller.handle_command(
                'close_app'
            ),
            'start': lambda: controller.handle_command(
                'start_app', restart=True
            ),
            'copy': lambda: copy(self.result)
        }
        for text, cmd_key, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=cmd_map[cmd_key],
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx,rely=rely,anchor='c')

    def show_result(self, result, user_input):
        self.result = result
        input_label = self.labels['input_label']
        result_label = self.labels['result_label']

        input_label.configure(
            text=f'Твой изначальный текст:\n{user_input}'
        )
        result_label.configure(
            text=f'Результат шифрования:\n{result}'
        )


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.label = ctk.CTkLabel(
            self,
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_LARGE
        )
        self.label.place(relx=0.5, rely=0.5, anchor='c')

    def change_message(self, stage):
        self.label.configure(
            text=choice(cfg.DELAY_MESSAGES[stage])
        )


class MainLogic:
    def __init__(self):
        self.main_data = {
            'mode': 'encrypt',
            'language': 'rus',
            'step': '',
            'text': ''
        }

    def check_input(self, page, info):
        if page == 'ModePage':
            self.main_data['mode'] = info
            return 'LanguagePage'

        if page == 'LanguagePage':
            self.main_data['language'] = info
            return 'StepPage'

        if page == 'StepPage':
            if not info:
                return 'empty'

            if not info.isdigit():
                return 'not_digit'

            step_val = int(info)
            if not (1 <= step_val <= 33):
                if step_val < 1:
                    return 'too_small'
                return 'too_big'

            self.main_data['step'] = info
            return 'TextPage'

        if page == 'TextPage':
            if not info:
                return 'empty'

            if len(info) > 50:
                return 'too_many'

            language = self.main_data['language']

            if language == 'rus':
                allowed_chars = cfg.low_rus_chars + cfg.up_rus_chars
            else:
                allowed_chars = cfg.low_eng_chars + cfg.up_eng_chars

            for char in info:
                if char.isalpha() and char not in allowed_chars:
                    return f'only_{language}'

            self.main_data['text'] = info
            return self.create_code()

    def create_code(self):
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
                alphabet = alphabet_map.get(
                    (language, char.isupper())
                )
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
        self.logic = MainLogic()
        self.is_first_load = True

        self.pages = {}
        self.current_frame = None
        page_types = [
            ('GreetingsPage', StaticPages),
            ('RulesPage', StaticPages),
            ('ModePage', ChoicePages),
            ('LanguagePage', ChoicePages),
            ('StepPage', InputPages),
            ('TextPage', InputPages),
            ('FinalPage', FinalPage),
            ('MessagePage', MessagePage)
        ]

        for page_name, page_class in page_types:
            self.pages[page_name] = page_class(
                self.main_frame,
                self,
                page_name
            )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)
        if hasattr(self.current_frame, "set_focus"):
            self.current_frame.set_focus()

    def handle_command(self, target, *args, **kwargs):
        if hasattr(self, target):
            method = getattr(self, target)
            if callable(method):
                method(*args, **kwargs)
                return
        self.switch_to(target)

    def transfer_info(self, page, user_input):
        status = self.logic.check_input(page, user_input)
        if status in cfg.ERROR_MESSAGES:
            self.pages[page].show_error(status)
        elif status in self.pages:
            self.switch_to(status)
        else:
            self.transfer_result(status, user_input)

    def transfer_result(self, result, user_input):
        self.pages['MessagePage'].change_message('waiting')
        self.switch_to('MessagePage')
        self.pages['FinalPage'].show_result(result, user_input)
        self.after(3000, lambda: self.switch_to('FinalPage'))

    def close_app(self):
        self.pages['MessagePage'].change_message('farewell')
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

    def start_app(self, restart=False):
        if restart:
            self.is_first_load = True

        if self.is_first_load:
            self.pages['MessagePage'].change_message('loading')
            self.switch_to('MessagePage')
            self.is_first_load = False

            for page in self.pages.values():
                if hasattr(page, 'update_ui'):
                    page.update_ui()

            self.after(3000, lambda: self.switch_to("ModePage"))
            return

        self.switch_to("ModePage")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()