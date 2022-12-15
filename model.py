import numpy as np


def calculating(objects):
    """
    Получает на вход список объектов, на выход выдаёт массив с уровнем потенциала в каждой точке
    :param obj:
    :return:
    """
    arr_potential_0 = [100] * 120
    for i in range (120):
        arr_potential_0[i] = [100]*240
    for i in range (240):
        arr_potential_0[50][i] = 450
    for obj in objects:
        arr_potential_0[obj*10][obj*10] = 1000
    return np.array(arr_potential_0, dtype='int')