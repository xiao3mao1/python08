import numpy as np
def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число.
       Находим серидину интервала и выясняем больше она или меньше загаданного числа.
       Если больше, то правая граница равна середине. 
       Если меньше, то левая граница равна середине.
       Новый интервал снова делим пополам. И так пока не найдем заданное число.
       Функция принимает загаданное число и возвращает число попыток
     
     Args:
        number (int, optional): Загаданное число. Defaults to 1.

     Returns:
            int: Число попыток
      """

    count = 0
    predict = np.random.randint(1, 101)

    left=1
    right=101
    middle=(right-left)//2 # вычисляем середину интервала между 1 и 100

    while middle!=predict:
         count += 1
         if middle > predict:
             right=middle  # переопределяем правую границу
         elif middle < predict:
            left=middle    # переопределяем левую границу
         middle=left+(right-left)//2  # вычисляем середину нового интервала
         
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
