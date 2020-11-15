# coding: utf8
import encrypt as e
import PySimpleGUI as sg

e_text_in = sg.Output()
d_text_out = sg.Output()
d_text_in = sg.Output()
e_text_out = sg.Output()

layout = [
    [sg.Text("Текст из файла"), sg.InputText(), sg.FileBrowse('Выбрать файл'), sg.Submit('Вставить для кодирования'), sg.Submit('Вставить для декодирования')],
    [sg.Text('Ключ'), sg.InputText()],
    [e_text_in, sg.Submit('Закодировать'), d_text_out],
    [d_text_in, sg.Submit('Декодировать'), e_text_out],
    ]

window = sg.Window('4 Lab', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break

    elif event == "Вставить для кодирования":
        with open(values[0], 'r') as fileIn:
            e_text_in.update(fileIn.read())

    elif event == "Вставить для декодирования":
        with open(values[0], 'r') as fileIn:
            d_text_in.update(fileIn.read())

    elif event == "Закодировать":
        # Убираем символ переноса строки из кодированного текста (реализация Get())
        # Так же меняем пробел на нижнее подчеркивание по заданию
        e_text = e_text_in.Get()[:-1].replace(' ', '_')
        key = values[1]
        if len(e_text) > 0 and len(key) > 0 and len(key) == 5:
            d_text_out.update(e.encrypt_vigenere(e_text, key))
        else:
            d_text_out.update('Введите текст в поле и задайте ключ длиной 5 символов')

    elif event == "Декодировать":
        # Убираем символ переноса строки из кодированного текста (реализация Get())
        # Так же меняем пробел на нижнее подчеркивание по заданию
        d_text = d_text_in.Get()[:-1].replace(' ', '_')
        key = values[1]
        if len(d_text) > 0 and len(key) > 0 and len(key) == 5:
            e_text_out.update(e.decrypt_vigenere(d_text, key))
        else:
            e_text_out.update('Введите текст в поле и задайте ключ длиной 5 символов')
