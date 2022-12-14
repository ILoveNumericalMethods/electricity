import matplotlib.pyplot as plt
import numpy as np

from input import *

c1='#00FFFF' #blue
c2='#EE82EE' #purple

def fadeColor(c1,c2,mix=0): #создаёт линейную интерполяцию от цвета с1 до цвета с2
    assert len(c1)==len(c2)
    assert mix>=0 and mix<=1, 'mix='+str(mix)
    rgb1=np.array([int(c1[ii:ii+2],16) for ii in range(1,len(c1),2)])
    rgb2=np.array([int(c2[ii:ii+2],16) for ii in range(1,len(c2),2)])
    rgb=((1-mix)*rgb1+mix*rgb2).astype(int)
    c='#'+('{:}'*3).format(*[hex(a)[2:].zfill(2) for a in rgb])
    return c

def coloring (arr):
    """
    создаёт массив с цветами градиента из массива с интенсивностью параметра

    :param arr: двумерный массив с интентсивностью параметра
    :return coloured_arr: двумерный массив, раскрашенный градиентом
    """
    coloured_arr = np.zeros((arr.shape[0], arr.shape[1], 3), dtype=int)
    for x in range (arr.shape[0]):
        for y in range (arr.shape[1]):
            if arr[x][y]>-1:
                color1 = fadeColor(c1,c2, arr[x][y]/1000) #цвет пикселя
                r = int(color1[1:3], 16)
                g = int(color1[3:5], 16)
                bl = int(color1[5::], 16)
                coloured_arr[x][y][0] = r
                coloured_arr[x][y][1] = g
                coloured_arr[x][y][2] = bl
            else:
                coloured_arr[x][y][0] = 0
                coloured_arr[x][y][1] = 0
                coloured_arr[x][y][2] = 0
    return (coloured_arr)

def colored_array_from_file(file_name):
    """
    создаёт массив из раскрашенных функцией coloring элементов массива кадров, возвращает массив раскрашенных кадров
    и параметры файла
    """
    arr, k, m, n = read_parametr_from_file(file_name)
    colored_arr = []
    for i in range(k):
        colored_arr.append(coloring(arr[i]))
    return colored_arr, k, m, n

#print(plt.imshow(colored_arr))
#plt.savefig('saved3_figure.png')
#plt.show()