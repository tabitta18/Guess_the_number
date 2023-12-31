import random

def guess_number():
    secret_number = random.randint(1, 50)
    attempts = 0

    print("Давай сыграем в игру 'Угадай число'.")

    while True:
        guess = int(input("Угадай число от 1 до 50: "))
        attempts += 1

        if guess < secret_number:
            print("Слишком маленькое число. Попробуйте еще раз.")
        elif guess > secret_number:
            print("Слишком большое число. Попробуйте еще раз.")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_number()
