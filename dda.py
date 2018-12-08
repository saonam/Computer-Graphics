from matplotlib import pyplot as plt
from random import randint


def DDA(X0, Y0, X1, Y1):
    dx = X1 - X0
    dy = Y1 - Y0

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = float(dx) / float(steps)
    Yinc = float(dy) / float(steps)

    #if((dy/dx)<1):
    for i in range(steps+1):
        x.append(X0)
        y.append(Y0)
        X0+= Xinc
        Y0+= Yinc


for i in range(5):   
    x = []
    y = []
    c, d, e, f = randint(-1000,1000), randint(-1000,1000),randint(-1000,1000),randint(-1000,1000)
    DDA(c,d,e,f)
    print("( {0} , {1} ), ( {2} , {3} )".format(c,d,e,f))
    plt.plot(x,y)
    plt.show()
