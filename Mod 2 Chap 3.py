# Завдання 1
# Користувач вводить з клавіатури число від 1 до 100. Якщо
# число кратне 3 (ділиться на 3 без остачі), виведіть слово «Fizz».
# Якщо число кратне 5, виведіть слово «Buzz». Якщо число
# кратне 3 та 5, потрібно вивести «Fizz Buzz». Якщо число не
# кратне ні 3, ані 5, виведіть тільки число.
# Якщо користувач ввів значення не в діапазоні від 1 до
# 100, виведіть повідомлення про помилку.

print("\nTask 1")

number = int(input("Введіть число від 1 до 100:  "))
if number < 1 or number > 100:
    print("Помилка! Число повинно бути в діапазоні від 1до 100.")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# Завдання 2
# Напишіть програму, яка на вибір користувача піднесе
# введене ним число до степеня від нульового до сьомого
# включно.

print("\nTask 2")

number = int(input("Введіть число: "))

for i in range(8):
    result = number ** i
    print(f"(number) в степені {i} рівне {result}")


# Завдання 3
# Напишіть програму підрахунку вартості розмови для
# різних мобільних операторів. Користувач вводить вартість
# розмови та вибирає, з якого на який оператор він дзвонить.
# Виведіть вартість розмови на екран.

print("\nTask 3")

def calculate_call_cost(call_cost, operator_from, operator_to):
    tariff_rates = {
        "МТС": 1.5,
        "Билайн": 1.2,
        "Мегафон": 1.8,
        "Теле2": 1.0
    }

    if operator_from not in tariff_rates:
        print("Помилка! Неправельно введено оператор вихідного дзвінка.")
        return None
    if operator_to not in tariff_rates:
        print("Помилка! Невірно вказаний оператор приймаючий звінок.")
        return None

    if call_cost <= 0:
        print("Помилка! Вартість зозмови повинна бути додатня.")
        return None

    rate_from = tariff_rates[operator_from]
    rate_to = tariff_rates[operator_to]
    total_cost = call_cost * rate_from / rate_to

    return total_cost


call_cost = float(input("Введіть вартість розмови: "))
operator_from = input("Введіть оператора вихідного дзвінка (Київстар, Vodafone Україна, lifecell, 3Mob): ").strip().capitalize()
operator_to = input("Введіть оператора приймаючопо розмову (Київстар, Vodafone Україна, lifecell, 3Mob): ").strip().capitalize()

result = calculate_call_cost(call_cost, operator_from, operator_to)
if result is not None:
    print(f"Вартисть розмови: {result}")




# Завдання 4
# Зарплата менеджера становить 200$ + відсоток від продажу:
# продаж до 500$ – 3%, 500 –1000$ – 5%, понад 1000$ – 8%. Користувач вводить з клавіатури рівень продажу для трьох
# менеджерів. Визначте їхню зарплату, а також найкращого менеджера,
# нарахуйте йому премію 200$ та виведіть підсумки на екран.

print("\nTask 4")

def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission = sales * 0.03
    elif sales <= 1000:
        commission = sales * 0.05
    else:
        commission = sales * 0.08
        total_salary = base_salary + commission
        return total_salary

sales_manager_1 = float(input("Введіть рівень продажу для менеджера 1: "))
sales_manager_2 = float(input("Введіть рівень продажу для менеджера 2: "))
sales_manager_3 = float(input("Введіть рівень продажу для менеджера 3: "))
salary_manager_1 = calculate_salary(sales_manager_1)
salary_manager_2 = calculate_salary(sales_manager_2)
salary_manager_3 = calculate_salary(sales_manager_3)
salaries = [salary_manager_1, salary_manager_2, salary_manager_3]
best_manager_index = salaries.index(max(salaries))
salaries[best_manager_index] += bonus

print("\nЗарплати менеджерів:")
print(f"Менеджер 1: ${salary_manager_1:.2f}")
print(f"Менеджер 2: ${salary_manager_2:.2f}")
print(f"Менеджер 3: ${salary_manager_3:.2f}")
print(f"\nНайкращий менеджер: Менеджер {best_manager_index + 1} з зарплатою: ${salaries[best_manager_index]:.2f}")
