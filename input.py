import numpy as np

def read_parametr_from_file(input_filename):
    """Cчитывает данные параметра из файла
    возвращает массив кадров и параметры файла

    **input_filename** — имя входного файла
    """
    with open(input_filename) as input_file:
        lines = input_file.readlines()
        m, n = [int(i) for i in lines.pop(0).split()]
        k = int((len(lines))/(n)) #кол-во итераций
        parameter_array = [[0 for i in range(m)] for j in range(n)]
        parameter_arrays = []
        for q in range (k):
            parameter_array = [[0 for i in range(m)] for j in range(n)]
            counter = 0  # счётчик строки
            for i in range (q*n, q*n+n):
                if len(lines[i].strip()) == 0 or lines[i][0] == '#':
                    continue  # пустые строки и строки-комментарии пропускаем
                for j in range(m):
                    parameter_array[counter][j] = int(lines[i].split()[j])
                counter += 1
            parameter_arrays.append(parameter_array)
    return np.array(parameter_arrays), k, m, n