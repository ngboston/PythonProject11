# Завдання 1
# Маємо текстовий файл. Створіть новий файл та перепишіть з вихідного файлу всі слова, що складаються не менше, ніж із семи літер.

print("\nTask 1")

def filter_long_words(input_file, output_file):
    """
    Зчитує слова з вхідного файлу, фільтрує слова довжиною 7 і більше символів,
    та записує їх у вихідний файл.

    Args:
        input_file (str): Шлях до вхідного текстового файлу.
        output_file (str): Шлях до вихідного текстового файлу.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                words = line.split()
                for word in words:

                    cleaned_word = word.strip('.,!?";:\'()[]{}')
                    if len(cleaned_word) >= 7:
                        outfile.write(cleaned_word + '\n')
        print(f"Слова довжиною 7+ символів успішно записані у файл {output_file}")

    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


input_file_path = "input.txt"
output_file_path = "output.txt"

filter_long_words(input_file_path, output_file_path)

# Завдання 2
# Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має збігатися з порядком рядків у заданому файлі.

print("\nTask 2")

def copy_file_lines(input_file, output_file):
    """
    Копіює рядки з input_file в output_file, зберігаючи порядок.

    Args:
        input_file (str): Шлях до вхідного файлу.
        output_file (str): Шлях до вихідного файлу.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                outfile.write(line)
        print(f"Рядки з '{input_file}' успішно скопійовані в '{output_file}'.")
    except FileNotFoundError:
        print("Помилка: Один або обидва файли не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


input_file_path = 'input.txt'
output_file_path = 'output.txt'

copy_file_lines(input_file_path, output_file_path)


# Завдання 3
# Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має бути зворотним до порядку рядків у заданому файлі.


print("\nTask 3")

def reverse_file_lines(input_file, output_file):
    """
    Переписує рядки з input_file в output_file у зворотному порядку.

    Args:
        input_file (str): Шлях до вхідного файлу.
        output_file (str): Шлях до вихідного файлу.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Помилка: файл '{input_file}' не знайдено.")
        return

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in reversed(lines):
            outfile.write(line)


input_file_path = 'input.txt'
output_file_path = 'output.txt'

reverse_file_lines(input_file_path, output_file_path)
print(f"Рядки з файлу '{input_file_path}' успішно переписані у зворотному порядку в файл '{output_file_path}'.")


# Завдання 4
# Маємо текстовий файл. Додайте до нього рядок із дванадцяти зірочок (************), помістивши його після останнього з рядків, в яких немає коми. Якщо таких рядків немає, додайте новий після всіх рядків файлу. Результат запишіть до іншого файлу.


print("\nTask 4")

def add_stars_after_last_no_comma(input_file, output_file):
    """
    Додає рядок з 12 зірочок після останнього рядка без коми.

    Args:
        input_file (str): Шлях до вхідного файлу.
        output_file (str): Шлях до вихідного файлу.
    """

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        last_no_comma_index = -1
        for i, line in enumerate(lines):
            if ',' not in line:
                last_no_comma_index = i

        if last_no_comma_index != -1:
            lines.insert(last_no_comma_index + 1, '************\n')
        else:
            lines.append('************\n')

        with open(output_file, 'w') as f:
            f.writelines(lines)

        print(f"Рядок зірочок успішно додано до файлу '{output_file}'.")

    except FileNotFoundError:
        print(f"Помилка: Файл '{input_file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


input_file_path = 'input.txt'
output_file_path = 'output.txt'


with open(input_file_path, 'w') as f:
    f.write("рядок 1\nрядок 2, з комою\nрядок 3\nрядок 4, з комою\nрядок 5")

add_stars_after_last_no_comma(input_file_path, output_file_path)


with open(output_file_path, 'r') as f:
    print("\nВміст вихідного файлу:")
    print(f.read())


# Завдання 5
# Маємо текстовий файл. Підрахуйте кількість слів, що починаються з символу, який задає користувач.


print("\nTask 5")

def count_words_starting_with_char(filename, char):
    """
    Підраховує кількість слів у файлі, що починаються з заданого символу.

    Args:
        filename (str): Шлях до текстового файлу.
        char (str): Символ, з якого повинні починатися слова.

    Returns:
        int: Кількість слів, що починаються з заданого символу.
    """

    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:

                    while word and not word[0].isalpha():
                        word = word[1:]
                    if word and word[0].lower() == char.lower():
                        count += 1
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
    return count


filename = input("Введіть шлях до текстового файлу: ")
char = input("Введіть символ, з якого повинні починатися слова: ")


word_count = count_words_starting_with_char(filename, char)
print(f"Кількість слів, що починаються з '{char}': {word_count}")


# Завдання 6
# Маємо текстовий файл. Перепишіть до іншого файлу всі його рядки замінюючи в них символ * на символ &, і навпаки.


print("\nTask 6")

def replace_chars(input_file, output_file):
  """
  Зчитує рядки з вхідного файлу, замінює символи '*' на '&' і навпаки,
  та записує змінені рядки у вихідний файл.

  Args:
    input_file: Шлях до вхідного текстового файлу.
    output_file: Шлях до вихідного текстового файлу.
  """
  try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
      for line in infile:
        modified_line = line.replace('*', '#').replace('&', '*').replace('#', '&')
        outfile.write(modified_line)
    print(f"Файл '{input_file}' успішно оброблено. Результат записано у '{output_file}'.")
  except FileNotFoundError:
    print(f"Помилка: Файл '{input_file}' не знайдено.")
  except Exception as e:
    print(f"Сталася помилка: {e}")


input_filename = "input.txt"
output_filename = "output.txt"


with open(input_filename,'w') as f:
  f.write('Привіт* & світ!\n')
  f.write('Python & це * чудово!\n')
  f.write('123 * 456 & 789\n')

replace_chars(input_filename, output_filename)


# Завдання 7
# Маємо масив рядків. Запишіть їх у файл, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку.


print("\nTask 7")

def zapisati_ryadky_u_fayl(masyv_ryadkiv, imya_faylu):
  """
  Записує масив рядків у файл, де кожен рядок розташований на окремому рядку.

  Args:
    masyv_ryadkiv: Масив рядків для запису у файл.
    imya_faylu: Ім'я файлу для запису.
  """

  try:
    with open(imya_faylu, 'w') as fayl:
      for ryadok in masyv_ryadkiv:
        fayl.write(ryadok + '\n')
    print(f"Рядки успішно записані у файл '{imya_faylu}'")
  except Exception as e:
    print(f"Виникла помилка при записі у файл: {e}")


masyv_ryadkiv = ["Перший рядок", "Другий рядок", "Третій рядок", "Четвертий рядок"]
imya_faylu = "output.txt"

zapisati_ryadky_u_fayl(masyv_ryadkiv, imya_faylu)


# Завдання 8
# Маємо масив рядків. Запишіть їх у файл, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку.


print("\nTask 8")

def zapis_masyvu_u_fayl(masyv_ryadkiv, imya_faylu):
  """
  Записує масив рядків у файл, кожен елемент на окремому рядку.

  Args:
    masyv_ryadkiv: Масив рядків для запису.
    imya_faylu: Ім'я файлу, в який потрібно записати масив.
  """
  try:
    with open(imya_faylu, 'w') as fayl:
      for ryadok in masyv_ryadkiv:
        fayl.write(ryadok + '\n')
    print(f"Масив рядків успішно записано у файл '{imya_faylu}'")
  except Exception as e:
    print(f"Помилка при записі у файл: {e}")


masyv_ryadkiv = ["Перший рядок", "Другий рядок", "Третій рядок"]
imya_faylu = "output.txt"
zapis_masyvu_u_fayl(masyv_ryadkiv, imya_faylu)


# Завдання 9
# Маємо текстовий файл. Підрахуйте кількість символів у ньому.


print("\nTask 9")

def count_characters(filename):
  """Підраховує кількість символів у текстовому файлі.

  Args:
    filename: Шлях до текстового файлу.

  Returns:
    Кількість символів у файлі.
  """

  try:
    with open(filename, 'r') as file:
      content = file.read()
      return len(content)
  except FileNotFoundError:
    return "Файл не знайдено."


file_path = 'your_file.txt'
char_count = count_characters(file_path)

print(f"Кількість символів у файлі '{file_path}': {char_count}")


# Завдання 10
# Маємо текстовий файл. Підрахуйте кількість рядків у ньому.


print("\nTask 10")

def count_lines(filename):
  """Підраховує кількість рядків у текстовому файлі."""

  try:
    with open(filename, 'r') as file:
      line_count = 0
      for line in file:
        line_count += 1
    return line_count
  except FileNotFoundError:
    return f"Файл '{filename}' не знайдено."


file_name = 'your_file.txt'
number_of_lines = count_lines(file_name)

if isinstance(number_of_lines, int):
  print(f"Кількість рядків у файлі '{file_name}': {number_of_lines}")
else:
  print(number_of_lines)
