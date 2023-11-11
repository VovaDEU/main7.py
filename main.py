import random
import PySimpleGUI as sg
target_number = random.randint(1, 100)
def guess_number(values1,target_number):
    values1 = int(values1)


    try:


        if values1< target_number:
            print("Загадане число більше.")
        elif values1> target_number:
            print("Загадане число менше.")
        else:
            print(f"Вітаємо! Ви вгадали число {target_number}")

    except ValueError:
        print("Будь ласка, введіть ціле число.")
sg.theme('DarkAmber')   # Add a touch of color
layout = [  [sg.Text('Спробуйте вгадати число від 1 до 100:')],
            [sg.Text('Вгадайте число'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    guess_number(values[0],target_number)


window.close()