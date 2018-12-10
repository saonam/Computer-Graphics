from matplotlib import pyplot as plt
from random import randint
	
				
def bresenham(xa, ya, xb, yb):
    dx = abs(xb-xa)
    dy = abs(yb-ya)
    
    if xb > xa: 
        lx = 1
    else:
        lx = -1
    if yb > ya:
        ly = 1
    else: 
        ly = -1
    
    if dx > dy:
        p0 = 2 * dy - dx
        for i in range(dx+1):

            a.append(xa)
            b.append(ya)

            if p0 < 0:
                x = xa + lx
                y = ya
                p = p0 + 2 * dy
            else: 
                x = xa + lx
                y = ya + ly
                p = p0 + 2 * dy - 2* dx
            xa = x
            ya = y
            p0 = p
        
    else:
        p0 = 2 * dx - dy
        for i in range(dy+1):
            a.append(xa)
            b.append(ya)

            if p0 < 0:
                x = xa
                y = ya + ly
                p = p0 + 2 * dx
            else:
                x = xa + lx
                y = ya + ly
                p = p0 + 2 * dx - 2 * dy
            xa = x
            ya = y
            p0 = p
 
for i in range(5):   
    a = []
    b = []
    c, d, e, f = randint(-10000,10000), randint(-10000,10000),randint(-10000,10000),randint(-10000,10000)
    bresenham(c,d,e,f)
    print("( {0} , {1} ), ( {2} , {3} )".format(c,d,e,f))
	plt.plot([-10000,10000],[0,0], linewidth=4, color='red' )
	plt.plot([0,0],[-10000,10000], linewidth=4, color='red' )
	plt.plot(a,b, color='red')
	plt.plot([c,e],[d,f], color='grey')
	plt.show()
