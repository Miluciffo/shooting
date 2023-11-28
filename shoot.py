import random


n_list=[]
r0=20
def xyr(x,y,r):
    x_r=x + r * (random.random() + random.random() - 1)
    y_r = y + r * (random.random() + random.random() - 1)


    return [int(x_r), int(y_r)]

def mass_shooting(x,y,n):
    for i in range(n):
        cord=xyr(6,8,4)
        n_list.append(cord)
    return n_list
