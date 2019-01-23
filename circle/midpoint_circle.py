from matplotlib import pyplot as plt
from random import randint

def midPoint(xc,yc,r):
    x=0
    y=r
    p=5/4-r
    a.append(xc)
    b.append(yc)
    while(x<=y):
        # octant points
        a.append(x+xc)
        b.append(y+yc)

        a.append(x+xc)
        b.append(-y+yc)

        a.append(-x+xc)
        b.append(y+yc)

        a.append(-x+xc)
        b.append(-y+yc)

        a.append(y+xc)
        b.append(x+yc)

        a.append(y+xc)
        b.append(-x+yc)
        
        a.append(-y+xc)
        b.append(x+yc)
        
        a.append(-y+xc)
        b.append(-x+yc)
        
        x+=1
        if(p<=0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x+1-2*(y-2)
        

for i in range(5):   
		a = []
		b = []
		c, d, e = randint(-10000,10000), 					randint(-10000,10000),randint(0,10000)
		midPoint(c,d,e)
		print("( {0} , {1} ), {2} )".format(c,d,e))
		plt.plot([-10000,10000],[0,0],color='red' )
		plt.plot([0,0],[-10000,10000], color='red' )
		plt.scatter(a,b, color='grey')
		plt.show()
