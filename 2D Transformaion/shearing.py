from matplotlib import pyplot as plt
import sys
from math import cos, sin, radians
t_vertices = [
        (2,4),
        (10,4),
        (6,10),
        (2,4)
]
sx, sy = int(sys.argv[1]),int(sys.argv[2])
st_vertices = []
x_pivot,y_pivot = 2,4
for v in t_vertices:
    x = v[0]+(v[1]-y_pivot)*sx
    y = v[1]+(v[0]-x_pivot)*sy
    st_vertices.append((x,y))
# axes
plt.plot([-20,20],[0,0])
plt.plot([0,0],[-20,20])
# original traingle 
plt.plot([v[0] for v in t_vertices],[v[1] for v in t_vertices])
# changed traingle
plt.plot([v[0] for v in st_vertices],[v[1] for v in st_vertices])
plt.show()


