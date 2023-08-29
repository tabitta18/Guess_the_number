import random
import eel

# Инициализация Eel
eel.init('web')

# Генерация случайного числа
number_to_guess = random.randint(1, 50)

# Функция для проверки угаданного числа
@eel.expose
def check_guess(guess):
    guess = int(guess)
    if guess < number_to_guess:
        return "Мало"
    elif guess > number_to_guess:
        return "Много"
    else:
        return "Верно!"

# Запуск Eel с веб-интерфейсом
eel.start('index.html', size=(720, 480))
