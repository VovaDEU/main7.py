Прибирання непотрібного функціоналу:

Видалимо клас InputHandler, оскільки PySimpleGUI може бути використаний без додаткових обгорток.
Замінимо виклик print у класі NumberGuesser на виклик sg.popup, щоб повідомлення виводилося в графічному вікні.

Оптимізація:
Змінимо використання random.randint на random.randrange(1, 101), щоб уникнути додаткової операції віднімання.
Замінимо безмежний цикл while True на цикл із обмеженням кількості спроб або можливість виходу з гри.

Коментарі:
Додамо коментарі до частин коду, які пояснюють його функціональність.

Компіляція в .exe:
Через інструмент pyinstaller компіляція в exe. (exe файл програми знаходится в dist)
