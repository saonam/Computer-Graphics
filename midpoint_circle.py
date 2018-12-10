from matplotlib import pyplot as plt
a=[]
b=[]
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
        

midPoint(0,0,500)
plt.plot([-500,500],[0,0], color='red')
plt.plot([0,0],[-500,500], color='red')
plt.scatter(a,b)
plt.show()
