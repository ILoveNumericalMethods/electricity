import matplotlib.pyplot as plt
import numpy as np

c1='#00FFFF' #blue
c2='#EE82EE' #purple

def fadeColor(c1,c2,mix=0): #создаЄт линейную интерпол€цию от цвета с1 до цвета с2
    assert len(c1)==len(c2)
    assert mix>=0 and mix<=1, 'mix='+str(mix)
    rgb1=np.array([int(c1[ii:ii+2],16) for ii in range(1,len(c1),2)])
    rgb2=np.array([int(c2[ii:ii+2],16) for ii in range(1,len(c2),2)])
    rgb=((1-mix)*rgb1+mix*rgb2).astype(int)
    c='#'+('{:}'*3).format(*[hex(a)[2:].zfill(2) for a in rgb])
    return c

def coloring (arr):
    """
    creates an array with gradient colours from an array with parameter intensities

    accepts a two-dimensional array with the parameter intensity
    returns a three dimensional array coloured with the gradient
    """

    coloured_arr = np.zeros((arr.shape[0], arr.shape[1], 3), dtype = int)
    for x in range (arr.shape[0]):
        for y in range (arr.shape[1]):
            if arr[x][y]>-1:
                color1 = fadeColor(c1,c2, arr[x][y]/1000) 
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
