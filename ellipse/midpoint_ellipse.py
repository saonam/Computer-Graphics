from matplotlib import pyplot as plt
from random import randint

def ellipse(xc, yc, ra, rb):
    x = 0 
    y = rb
    p = (rb*rb) - (ra*ra*rb) + ((ra*ra)/4)
    
    while((2*x*rb*rb)<(2*y*ra*ra)):
#            print(xc+x, yc-y)
 #           print(xc-x, yc+y)
  #          print(xc+x, yc+y)
   #         print(xc-x, yc-y)
            a.append(xc+x)
            a.append(xc-x)
            a.append(xc+x)
            a.append(xc-x)
            b.append(yc-y)
            b.append(yc+y)
            b.append(yc+y)
            b.append(yc-y)
            if(p<0):
                x = x + 1 
                p = p + (2*rb*rb*x) + (rb*rb)
            else:
                x = x + 1
                y = y - 1
                p = p + (2*rb*rb*x+rb*rb) - (2*ra*ra*y)
    
    p = rb*rb*(float(x)+0.5)*(float(x)+0.5) + ra*ra*(y-1)*(y-1) - ra*ra*rb*rb
    while(y>=0):
#        print(xc+x, yc-y)
 #       print(xc-x, yc+y)
  #      print(xc+x, yc+y)
    #    print(xc-x, yc-y)
        a.append(xc+x)
        a.append(xc-x)
        a.append(xc+x)
        a.append(xc-x)
        b.append(yc-y)
        b.append(yc+y)
        b.append(yc+y)
        b.append(yc-y)
        if(p<0):
            y = y - 1
            x = x + 1
            p = p + (2*rb*rb*x) - (2*ra*ra*y) - (ra*ra)
        else:
            y = y - 1
            p = p - (2*ra*ra*y) + (ra*ra)
'''
for i in range(5):  
    a = []
    b = []
    c = randint(-100,100)
    d = randint(-100,100)
    e = randint(1,100)
    f = randint(1,100)
    print(c,d,e,f)
    ellipse(c,d,e,f)
    plt.scatter(c,d, color='red')
    plt.plot([-100,100],[0,0], color='red')
    plt.plot([0,0],[-100,100], color='red')
    plt.scatter(a,b)
    plt.show()
'''
a=[]
b=[]
ellipse(0,0,2,3)
for x,y in zip(a,b):
    print(x,y)



    



