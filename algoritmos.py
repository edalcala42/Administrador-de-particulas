import math

def distancia_euclidiana(x_1:int, y_1:int, x_2:int, y_2:int)->float:
    x = x_2 - x_1
    y = y_2 - y_1
    return (math.sqrt((x*x)+(y*y)))
    