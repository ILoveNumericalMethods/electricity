from model import *
from color import *
objects = []
arr_potential = []
k=0
def converting(string_formula):
    """
    Получает на вход формулу объекта, создаёт объект и добавляет его в список объектов
    :param string_formula:
    :return:
    """
    global objects
    global arr_potential
    global k
    k = k+1
    objects.append(k) #добавление объекта в список
    arr_potential = coloring(calculating(objects))
