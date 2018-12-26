# midPoint function for line generation 
def midPoint(X1,Y1,X2,Y2): 
	# calculate dx & dy 
	dx = abs(X2 - X1) 
	dy = abs(Y2 - Y1)
	x = X1 
	y = Y1 
	a.append(x)
	b.append(y)
	# initial value of decision parameter d
	if X2 > X1: 
		lx = 1
	else:
		lx = -1
	if Y2 > Y1:
		ly = 1
	else: 
		ly = -1
        
	if(dx>dy): 
		d = dy - (dx/2)
		for i in range(dx):
			x = x+lx
			if (d<0):
				d = d+dy
			else:
				d=d+(dy-dx)
				y=y+ly
			a.append(x)
			b.append(y)
	else:
		d = dx - (dy/2)
		for i in range(dy):
			y = y+ly
			if (d<0):
				d = d+dx
			else:
				d=d+(dx-dy)
				x=x+lx

			a.append(x)
			b.append(y)

from matplotlib import pyplot as plt
from random import randint



if __name__=='__main__': 
	for i in range(5):   
		a = []
		b = []
		c, d, e, f = randint(-10000,10000), 					randint(-10000,10000),randint(-10000,10000),randint(-10000,10000)
		midPoint(c,d,e,f)
		print("( {0} , {1} ), ( {2} , {3} )".format(c,d,e,f))
		plt.plot([-10000,10000],[0,0], linewidth=4, color='red' )
		plt.plot([0,0],[-10000,10000], linewidth=4, color='red' )
		plt.plot(a,b, color='red')
		plt.plot([c,e],[d,f], color='grey')
		plt.show()


  
