from random import shuffle

carts = [
    'шестерка', 
    'семерка', 
    'восьмерка', 
    'девятка', 
    'десятка', 
    'валет', 
    'дама', 
    'король', 
    'туз'
]

shuffle(carts)
score = 0

while True:
    user_input = input("Хотите взять карту? (y / n): ")

    if user_input.lower() == 'n':
        print("Игра закончена.")
        print(f"Ваш счет: {score}")
        break
    else:
        card = carts.pop()
        print(f"Взяли карту: {card}")
        if card == 'валет':
            score += 2
        elif  card == 'дама':
            score += 3
        elif card == 'король':
            score += 4
        elif card == 'туз':
            score += 11
        else:
            score += 1
        
        print(f"Текущий счет: {score}")
        if (score > 21):
            print("Вы проиграли!")
            break
        elif (score == 21):
            print("Вы выиграли!")
            break
        else:
            continue