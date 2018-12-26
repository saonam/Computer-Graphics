from matplotlib import pyplot as plt
import sys
t_vertices = [
        (2,4),
        (10,4),
        (6,10),
        (2,4)
]
tx, ty = int(sys.argv[1]),int(sys.argv[2])

# axes
plt.plot([-20,20],[0,0])
plt.plot([0,0],[-20,20])
# original traingle 
plt.plot([v[0] for v in t_vertices],[v[1] for v in t_vertices])
# translated traingle
plt.plot([(v[0]+tx) for v in t_vertices],[(v[1]+ty) for v in t_vertices])
plt.show()


