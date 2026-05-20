# ====================
# РАЗДЕЛ 1. ВЫЗОВ МОДУЛЕЙ, СОЗДАНИЕ ОКНА ПРОГРАММЫ, КЛЮЧЕВЫЕ ПЕРЕМЕННЫЕ
# ====================

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode ('dark')
app = ctk.CTk()
app.title ('Ceasar Code')
app.geometry ('600x500+800+450')
app.resizable (False, False)
app.attributes ('-alpha', 0.9)

low_eng_chars = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
up_eng_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_rus_chars = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
up_rus_chars = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

main = ctk.CTkFrame(app)
main.pack(fill = 'both', expand = True)

# ====================
# РАЗДЕЛ 2. ФУНКЦИИ - ИСПОЛНИТЕЛИ
# ====================

def switch_to(page):
    for child in main.winfo_children():
        child.pack_forget()
    page.pack(fill = 'both', expand = True)

def clear_all():
    def go_to_page9():
        switch_to(page9)
        page9.after(5000, lambda: switch_to(page3))

    page3.code.set('code')
    page4.language.set('rus')
    page5.step.delete(0, 'end')
    page6.text.delete(0, 'end')
    go_to_page9()

def farewell():
    switch_to(page10)
    page10.after(5000, app.destroy)

def check_step():
    def go_to_page6():
        switch_to(page6)
        page6.after(200, lambda: page6.text.focus_force())

    step = page5.step.get()
    entry = page5.step

    if len(step) == 0:
        messagebox.showinfo('Ошибочка', 'В поле пусто')
        entry.delete (0, 'end')
    elif step.isdigit() == False:
        messagebox.showinfo('Ошибочка', 'Допускаются только цифры')
        entry.delete (0, 'end')
    elif int(step) < 1:
        messagebox.showinfo('Ошибочка', 'Нужен хотя бы 1 шаг')
        entry.delete (0, 'end')
    elif int(step) > 26:
        messagebox.showinfo('Ошибочка', 'Допустимый максимум - 26 шагов')
        entry.delete (0, 'end')
    else:
        go_to_page6()

def check_text():
    language = page4.language.get()
    text = page6.text.get()
    entry = page6.text

    if len(text) == 0:
        messagebox.showinfo('Ошибочка', 'Нужно ввести хоть что-то')
    elif len(text) > 100:
        messagebox.showinfo('Ошибочка', 'Допускается не более 100 символов')

    elif language == 'rus':
        for i in text:
            if i.isalpha() and i.lower() not in low_rus_chars:
                messagebox.showinfo('Ошибочка', 'Не допускаются буквы латиницы')
                entry.delete (0, 'end')
                break
        else:
            creating()

    elif language == 'eng':
        for i in text:
            if i.isalpha() and i.lower() not in low_eng_chars :
                messagebox.showinfo('Ошибочка', 'Не допускаются буквы кириллицы')
                entry.delete (0, 'end')
                break
        else:
            creating()

def creating():
    def go_to_page7():
        switch_to(page7)
        page7.after(5000, lambda: switch_to(page8))

    result = ''
    text = page6.text.get()
    step = page5.step.get()
    code = page3.code.get()
    language = page4.language.get()

    for i in text:
        if i.isalpha():
            if language == 'rus':
                if code == 'code':
                    if i.isupper():
                        x = up_rus_chars.index(i)
                        result += up_rus_chars[x + int(step)]
                    else:
                        x = low_rus_chars.index(i)
                        result += low_rus_chars[x + int(step)]
                if code == 'decode':
                     if i.isupper():
                        x = up_rus_chars.index(i)
                        result += up_rus_chars[x - int(step)]
                     else:
                        x = low_rus_chars.index(i)
                        result += low_rus_chars[x - int(step)]

            if language == 'eng':
                if code == 'code':
                    if i.isupper():
                        x = up_eng_chars.index(i)
                        result += up_eng_chars[x + int(step)]
                    else:
                        x = low_eng_chars.index(i)
                        result += low_eng_chars[x + int(step)]
                if code == 'decode':
                    if i.isupper():
                        x = up_eng_chars.index(i)
                        result += up_eng_chars[x - int(step)]
                    else:
                        x = low_eng_chars.index(i)
                        result += low_eng_chars[x - int(step)]
        else:
            result += i

    page8.label1.configure(text = text)
    page8.label2.configure(text = result)

    go_to_page7()

# ====================
# РАЗДЕЛ 3. ФУНКЦИИ - СТРОИТЕЛИ
# ====================

def create_greetings(main):
    frame1 = ctk.CTkFrame(main)
    frame1.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame1, text = 'Приветствую! \n\n\n Эта программа поможет вам \n\nсоздать Шифр Цезаря\n\nА также - дешифровать его',
    font = ('Constantia', 25))
    label.place(relx = 0.5, rely = 0.4, anchor = 'c')

    button = ctk.CTkButton (frame1, width = 70, height = 50, corner_radius = 40, text = 'Отлично!', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page2))
    button.place(relx = 0.5, rely = 0.8, anchor = 'c')

    return frame1

def create_rules(main):
    frame2 = ctk.CTkFrame(main)
    frame2.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame2, text = '''Шифр Цезаря - это метод шифрования,
при котором каждая буква текста 
заменяется другой, отстоящей 
на фиксированное количество позиций,
правее по алфавиту.


Например, при шифровке с шагом равным 3
«А» превращается в «Г»,
а при дешифровке с шагом равным 5
«Ж» превращается в «В».''', font = ('Constantia', 25))
    label.place(relx = 0.5, rely = 0.4, anchor = 'c')

    button = ctk.CTkButton (frame2, width = 70, height = 50, corner_radius = 40, text = 'Понятно', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page3))
    button.place(relx = 0.5, rely = 0.85, anchor = 'c')

    return frame2

def is_code(main):
    frame3 = ctk.CTkFrame(main)
    frame3.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame3, text = 'Нужно зашифровать\n\nили\n\nдешифровать код?', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    frame3.code = ctk.StringVar(value = 'code')

    box = ctk.CTkRadioButton (frame3, text = 'Зашифровать', font = ('Constantia', 23), fg_color = '#996633',
    border_color = '#FFFFFF', hover_color = '#996633', border_width_unchecked = 1, variable = frame3.code, value = 'code')
    box.place(relx = 0.3, rely = 0.6, anchor = 'c')

    box = ctk.CTkRadioButton (frame3, text = 'Дешифровать', font = ('Constantia', 23), fg_color = '#996633',
    border_color = '#FFFFFF', hover_color = '#996633', border_width_unchecked = 1, variable = frame3.code, value = 'decode')
    box.place(relx = 0.7, rely = 0.6, anchor = 'c')

    button = ctk.CTkButton (frame3, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page4))
    button.place(relx = 0.65, rely = 0.8, anchor = 'c')

    button = ctk.CTkButton (frame3, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page2))
    button.place(relx = 0.35, rely = 0.8, anchor = 'c')

    return frame3

def is_language(main):
    def go_to_page5():
        switch_to(page5)
        page5.after(200, lambda: page5.step.focus_force())

    frame4 = ctk.CTkFrame(main)
    frame4.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame4, text = 'На каком языке ваш текст?', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.25, anchor = 'c')

    frame4.language = ctk.StringVar(value = 'rus')

    box = ctk.CTkRadioButton (frame4, text = 'Русский', font = ('Constantia', 23), fg_color = '#996633',
    border_color = '#FFFFFF', hover_color = '#996633', border_width_unchecked = 1, variable = frame4.language, value = 'rus')
    box.place(relx = 0.3, rely = 0.5, anchor = 'c')

    box = ctk.CTkRadioButton (frame4, text = 'Английский', font = ('Constantia', 23), fg_color = '#996633',
    border_color = '#FFFFFF', hover_color = '#996633', border_width_unchecked = 1, variable = frame4.language, value = 'eng')
    box.place(relx = 0.7, rely = 0.5, anchor = 'c')

    button = ctk.CTkButton (frame4, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = go_to_page5)
    button.place(relx = 0.65, rely = 0.75, anchor = 'c')

    button = ctk.CTkButton (frame4, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page3))
    button.place(relx = 0.35, rely = 0.75, anchor = 'c')

    return frame4

def create_step(main):

    frame5 = ctk.CTkFrame(main)
    frame5.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame5, text = 'Введите шаг сдвига\n\n(от 1 до 26)', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    frame5.step = ctk.CTkEntry (frame5, width = 100, height = 30, corner_radius = 40, justify = 'c', font = ('Cambria', 27))
    frame5.step.place(relx = 0.5, rely = 0.5, anchor = 'c')

    button = ctk.CTkButton (frame5, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = check_step)
    button.place(relx = 0.65, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (frame5, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page4))
    button.place(relx = 0.35, rely = 0.7, anchor = 'c')

    return frame5

def create_text(main):

    frame6 = ctk.CTkFrame(main)
    frame6.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame6, text = 'Введите ваш текст\n(не более 100 символов)', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    frame6.text = ctk.CTkEntry (frame6, width = 500, height = 30, corner_radius = 40, justify = 'c', font = ('Cambria', 27))
    frame6.text.place(relx = 0.5, rely = 0.5, anchor = 'c')

    button = ctk.CTkButton (frame6, width = 70, height = 50, corner_radius = 40, text = 'Далее', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = check_text)
    button.place(relx = 0.65, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (frame6, width = 70, height = 50, corner_radius = 40, text = 'Назад', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = lambda: switch_to(page5))
    button.place(relx = 0.35, rely = 0.7, anchor = 'c')

    return frame6

def waiting(main):
    frame7 = ctk.CTkFrame(main)
    frame7.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame7, text = 'Дайте мне\nнемного подумать...', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    return frame7

def final(main):
    frame8 = ctk.CTkFrame(main)
    frame8.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame8, text = 'Изначальный текст:', corner_radius = 40, fg_color = '#996633', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.1, anchor = 'c')

    frame8.label1 = ctk.CTkLabel (frame8, text = '', wraplength = 550, justify = 'center', font = ('Constantia', 27))
    frame8.label1.place(relx = 0.5, rely = 0.25, anchor = 'c')

    label = ctk.CTkLabel (frame8, text = 'Результат шифрования:', corner_radius = 40, fg_color = '#996633', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.45, anchor = 'c')

    frame8.label2 = ctk.CTkLabel (frame8, text = '', wraplength = 550, justify = 'center', font = ('Constantia', 27))
    frame8.label2.place(relx = 0.5, rely = 0.6, anchor = 'c')

    label = ctk.CTkLabel (frame8, text = 'Хотите повторить?', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.8, anchor = 'c')

    button = ctk.CTkButton (frame8, width = 90, height = 50, corner_radius = 40, text = 'Да', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = clear_all)
    button.place(relx = 0.35, rely = 0.9, anchor = 'c')

    button = ctk.CTkButton (frame8, width = 70, height = 50, corner_radius = 40, text = 'Нет', fg_color = '#996633',
    hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 25), command = farewell)
    button.place(relx = 0.65, rely = 0.9, anchor = 'c')

    return frame8

def repeat(main):
    frame9 = ctk.CTkFrame(main)
    frame9.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame9, text = 'Отлично!\n\nЗапускаю процесс...', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    return frame9

def end(main):
    frame10 = ctk.CTkFrame(main)
    frame10.pack(fill = 'both', expand = True)

    label = ctk.CTkLabel (frame10, text = 'До новых встреч!', font = ('Constantia', 27))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    return frame10

page1 = create_greetings(main)
page2 = create_rules(main)
page3 = is_code(main)
page4 = is_language(main)
page5 = create_step(main)
page6 = create_text(main)
page7 = waiting(main)
page8 = final(main)
page9 = repeat(main)
page10 = end(main)

switch_to(page1)

app.mainloop()
