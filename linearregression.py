import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

# xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

def create_dataset(hm, varience, step=2, corellation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-varience, varience)
        ys.append(y)
        if corellation and corellation == 'pos':
            val+=step
        elif corellation and corellation == 'neg':
            val-=step
    xs = [i for i in range(len(ys))]
    
    
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def mean(arr):
    total = 0
    length = len(arr)
    for ele in range(0, length):
        total = total + arr[ele]
    return total/length
    
def best_fit_slope_and_intersept(xs, ys):
    m =  ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
            ((mean(xs)*mean(xs)) - mean(xs*xs)) )
    b = mean(ys) - m*mean(xs)
    return m, b


def squared_error(ys_o, ys_l):
    return sum((ys_l-ys_o)**2)

def coefficent_of_determination(ys_o, ys_l):
    y_mean_l = [mean(ys_o) for y in ys_o]
    ser = squared_error(ys_o, ys_l)
    seym = squared_error(ys_o, y_mean_l)
    return 1 - (ser / seym)

def main(predict, hm, varience, step=2, corellation=False):
    xs, ys = create_dataset(hm, varience, step, corellation=corellation)


    m, b = best_fit_slope_and_intersept(xs, ys)


    reg_line = [(m*x) + b for x in xs]

    predict_x = float(predict)
    predict_y = (m*predict_x)+b


    r_squared = coefficent_of_determination(ys, reg_line)
    print(r_squared)

    plt.scatter(xs, ys)
    plt.scatter(predict_x, predict_y, s=100, color='g')
    plt.plot(xs, reg_line)
    plt.show()
    
main(10, 40, 50, 2, corellation='pos')