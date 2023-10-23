from tkinter import IntVar
import customtkinter
from main import MorseCode, HexCode


def start_code_morse():
    message = Text_1.get('1.0', 'end')
    text_morse = MorseCode.code_morse(message)
    Text_2.insert('end', text_morse)


def start_encode_morse():
    message = Text_1.get('1.0', 'end')
    morse_text = MorseCode.encode_morse(message)
    Text_2.insert('end', morse_text)

def start_code_hex():
    message = Text_1.get('1.0', 'end')
    text_hex = HexCode.code_hex(message)
    Text_2.insert('end', text_hex)

def start_encode_hex():
    message = Text_1.get('1.0', 'end')
    hex_text = HexCode.encode_hex(message)
    Text_2.insert('end', hex_text)

# def start_code_caesar():
#     message = Text_1.get('1.0', 'end')
#     text_caesar = CaesarCode.code_caesar(message)
#     Text_2.insert('end', text_caesar)
#
# def start_encode_caesar(entry):
#     message = Text_1.get('1.0', 'end')
#     shift = entry.get()
#     caesar_text = CaesarCode.encode_caesar(message, shift)
#     Text_2.insert('end', caesar_text)


def check():
    if (step.get() == 1) and (code.get() == 1):
        start_code_morse()
    elif (step.get() == 2) and (code.get() == 1):
        start_encode_morse()
    elif (step.get() == 1) and (code.get() == 2):
        start_code_hex()
    elif (step.get() == 2) and (code.get() == 2):
        start_encode_hex()


customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title("Шифратор/Дешифратор")
root.geometry("950x650")
step = IntVar(value=0)
code = IntVar(value=0)
encrypted_label = customtkinter.CTkLabel(root)
encrypted_label.pack()
frame = customtkinter.CTkFrame(
    root,
    width=800,
    height=160)

Text_1 = customtkinter.CTkTextbox(
    root,
    width=370,
    height=305,
    font=('CTkTextFont', 16))
Text_2 = customtkinter.CTkTextbox(
    root,
    width=370,
    height=305,
    font=('CTkTextFont', 16))
Label_1 = customtkinter.CTkLabel(
    root,
    text='Введите текст: ',
    font=('CTkTextFont', 15))
Label_2 = customtkinter.CTkLabel(
    root,
    text='Результат конвертирования: ',
    font=('CTkTextFont', 15))
Label_3 = customtkinter.CTkLabel(
    frame,
    text='Выберите шифр:',
    font=('CTkTextFont', 19))
Label_4 = customtkinter.CTkLabel(
    frame,
    text='Выберите действие:',
    font=('CTkTextFont', 19))
Check_1 = customtkinter.CTkRadioButton(
    frame,
    value=1,
    variable=step,
    text='Шифровать',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
Check_2 = customtkinter.CTkRadioButton(
    frame,
    value=2,
    variable=step,
    text='Дешифровать',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
S_Check_1 = customtkinter.CTkRadioButton(
    frame,
    value=1,
    variable=code,
    text='Азбука Морзе',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
S_Check_2 = customtkinter.CTkRadioButton(
    frame,
    value=2,
    variable=code,
    text='HEX-шифр',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
S_Check_3 = customtkinter.CTkRadioButton(
    frame,
    value=3,
    variable=code,
    text='Азбука Морзе',
    font=('CTkTextFont', 15),
    radiobutton_height=13,
    radiobutton_width=13,
    corner_radius=20,
    border_width_checked=4,
    border_width_unchecked=3)
Btn_1 = customtkinter.CTkButton(
    root,
    command=check,
    height=40,
    width=120)

frame.place(x=75, y=20)
Label_3.place(x=15, y=5)
S_Check_1.place(x=15, y=50)
S_Check_2.place(x=15, y=75)
S_Check_3.place(x=15, y=100)

Label_4.place(x=600, y=5)
Check_1.place(x=635, y=60)
Check_2.place(x=635, y=85)
Label_1.place(x=85, y=200)
Text_1.place(x=75, y=230)
Label_2.place(x=518, y=200)
Text_2.place(x=505, y=230)
Btn_1.place(x=413, y=570)

root.mainloop()
