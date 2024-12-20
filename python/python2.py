from random import randint

user_number = int(input("Введите число от 1 до 100: "))
pc_number = randint(1, 100)

while(user_number != pc_number):
    if(user_number < pc_number):
        print("Введенное число меньше загаданного. Попробуйте еще раз.")
    else:
        print("Введенное число больше загаданного.")

    user_number = int(input("Попробуйте ввести число еще раз: "))

print("Вы угадали! Загаданное число:", pc_number)