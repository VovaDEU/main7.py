import random
import PySimpleGUI as sg

class NumberGuesser:
    def __init__(self, target_number):
        self.target_number = target_number

    def guess_number(self, user_guess):
        try:
            user_guess = int(user_guess)

            if user_guess < self.target_number:
                sg.popup("Загадане число більше.")
            elif user_guess > self.target_number:
                sg.popup("Загадане число менше.")
            else:
                sg.popup(f"Вітаємо! Ви вгадали число {self.target_number}")
                return True  # Додали повернення True, щоб зупинити гру після вгадування

        except ValueError:
            sg.popup("Будь ласка, введіть ціле число.")

def main():
    target_number = random.randrange(1, 101)
    game = NumberGuesser(target_number)
    max_attempts = 10  # Максимальна кількість спроб
    attempt_count = 0

    while attempt_count < max_attempts:
        user_input = sg.popup_get_text("Спробуйте вгадати число від 1 до 100:")

        if user_input is None:
            break  # Користувач натиснув "Відміна" або закрив вікно

        if game.guess_number(user_input):
            break  # Якщо гравець вгадав, виходимо з гри

        attempt_count += 1

    if attempt_count == max_attempts:
        sg.popup(f"Гру завершено. Було вичерпано {max_attempts} спроб. Загадане число було {target_number}.")

if __name__ == "__main__":
    main()
