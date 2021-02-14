# Проект 0
import numpy

hidden_number = numpy.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def guess_number(hidden_number):  # функция угадать загаданное компьютером число
    count = 0  # счетчик попыток
    start = 1  # нижняя граница поиска
    finish = 100  # верхняя граница поиска
    number = 0  # предполагаемое число

    while number != hidden_number:  # цикл попыток
        number = (start + finish) // 2  # предполагаемое число
        count += 1  # увеличиваем счетчик
        if number == hidden_number:  # если угадали...
            break  # ...завершаем цикл
        elif number < hidden_number:  # если предполагаемое число меньше загаданного числа...
            start = number + 1  # ...увеличиваем нижнюю границу поиска
        elif number > hidden_number:  # если предполагаемое число больше загаданного числа...
            finish = number - 1  # ...уменьшаем нижнюю границу поиска

    return count  # возвращаем счетчик попыток


print(f"Вы угадали число {hidden_number} за {guess_number(hidden_number)} попыток.")


def iteration_count(guess_number):  # функция повтора угадать загаданное число
    iteration_count = []  # создаем пустой список(в этот список будем добавлять счетчики попыток)
    random_array = numpy.random.randint(1, 101, size=1000)  # загаданное число(повтор 1000 раз)

    for number in random_array:  # итерация по каждому загаданному числу
        iteration_count.append(
            guess_number(number))  # функция guess_number возвращает нам счетчик и мы помещаем его в наш список
    score = int(numpy.mean(iteration_count))  # среднее значение из списка с счетчиками

    return (score)  # возвращаем среднее


ans = iteration_count(guess_number)
print(f"Ваш алгоритм угадывает число в среднем за {ans} попыток")