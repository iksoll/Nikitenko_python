print("Элементы меньше 15")
array = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]

for i  in array:
    if i < 15:
        print(i)

number = int(input("Введите число:"))
if (number < 0):
    print("Число отрицательное")
elif (number == 0):
    print("Число ноль")
else:
    print("Число положительное")

def calc(action, num1, num2):
    if action == "+":
        return num1 + num2
    elif action == "-":
        return num1 - num2
    elif action == "*":
        return num1 * num2
    elif action == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Нельзя делить на ноль"
    else:
        return "Неверное действие"

action = input("Введите действие (+, -, *, /): ")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
calc_result = calc(action, num1, num2)

print("Результат:", calc_result)

for i in range(10, 0, -1):
    print(i)

    import math

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    Возвращает список корней (0, 1 или 2 корня).
    """
    if a == 0:
        if b == 0:
            return "Уравнение не имеет решений" if c != 0 else "Бесконечное множество решений"
        return [-c / b]

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        return []

print("Решение квадратного уравнения ax^2 + bx + c = 0")
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_quadratic(a, b, c)

if isinstance(result, str):
    print(result)
elif len(result) == 2:
    print(f"Уравнение имеет два корня: x1 = {result[0]}, x2 = {result[1]}")
elif len(result) == 1:
    print(f"Уравнение имеет один корень: x = {result[0]}")
else:
    print("Уравнение не имеет действительных корней.")
