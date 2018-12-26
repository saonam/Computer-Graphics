from matplotlib import pyplot as plt
import sys
from math import cos, sin, radians
t_vertices = [
        (2,4),
        (10,4),
        (6,10),
        (2,4)
]
rt_vertices = []
angle = int(sys.argv[1])

x_pivot, y_pivot = 0,0

for v in t_vertices:
    x_shifted = v[0] - x_pivot
    y_shifted = v[1] - y_pivot
    x = x_pivot + (x_shifted*round(cos(radians(angle)),3)) - (y_shifted*round(sin(radians(angle)),3))
    y = y_pivot + (x_shifted*round(sin(radians(angle)),3)) + (y_shifted*round(cos(radians(angle)),3))
    rt_vertices.append((x,y))
# axes
plt.plot([-20,20],[0,0])
plt.plot([0,0],[-20,20])
# original traingle 
plt.plot([v[0] for v in t_vertices],[v[1] for v in t_vertices])
# translated traingle
plt.plot([v[0] for v in rt_vertices],[v[1] for v in rt_vertices])
plt.show()


