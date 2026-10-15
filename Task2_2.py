def input_vector():
    
    while True:
        
        user_input = input("Введите числа для вектора через пробел: ")
        String_coordinates = user_input.split()
        
        if len(String_coordinates) == 0:
            print("Ошибка: вы ничего не ввели. Попробуйте снова.")
            continue
        
        vector = []
        is_valid = True
        
        for Coordinate in String_coordinates:

            try:
                vector.append(float(Coordinate))
                
            except ValueError:
                print("Ошибка: вы ввели не цифры. Вектор должен состоять только из чисел. Попробуйте снова.")
                is_valid = False
                break
        
        if is_valid:
            return vector


def calculate_cosine_distance(vec1, vec2):
    
    if len(vec1) != len(vec2):
        print("Ошибка: вектора имеют разную длину. Расчет невозможен.")
        return
    
    if len(vec1) == 0:
        print("Ошибка: вектора пустые. Расчет невозможен.")
        return

    scalar_multiplication = 0
    sum_squares_1 = 0
    sum_squares_2 = 0

    for i in range(len(vec1)):
        scalar_multiplication += vec1[i] * vec2[i]
        sum_squares_1 += vec1[i] ** 2
        sum_squares_2 += vec2[i] ** 2

    Vector_modul_1 = sum_squares_1 ** 0.5
    Vector_modul_2 = sum_squares_2 ** 0.5

    if Vector_modul_1 == 0 or Vector_modul_2 == 0:
        print("Ошибка: один из векторов нулевой. Делить на ноль нельзя.")
        return

    cosine_similarity = scalar_multiplication / (Vector_modul_1 * Vector_modul_2)
    cosine_distance = 1 - cosine_similarity
    print("Косинусное расстояние рассчитано:", cosine_distance)

print("Задайте первый вектор:")
vector1 = input_vector()
print("Задайте второй вектор:")
vector2 = input_vector()
calculate_cosine_distance(vector1, vector2)