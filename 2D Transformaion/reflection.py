from matplotlib import pyplot as plt
import sys
from math import cos, sin, radians
import numpy as np

t_vertices = [
        (2,4),
        (10,4),
        (6,10),
        (2,4)
]
reflection_about = sys.argv[1]
rx = 1
ry = 1

if reflection_about == 'x-axis':
    ry = -1

if reflection_about == 'y-axis':
    rx = -1

if reflection_about == 'x=y':
    rt_vertices = [(v[1],v[0]) for v in t_vertices]
    plt.plot([v[0] for v in rt_vertices],[v[1] for v in rt_vertices])

if reflection_about == 'x=-y':
    rt_vertices = [(-1*v[1],-1*v[0]) for v in t_vertices]
    plt.plot([v[0] for v in rt_vertices],[v[1] for v in rt_vertices])

if reflection_about == 'y=mx+c':
    m = int(sys.argv[2])
    c = int(sys.argv[3])
    reflection_matrix = [
            [(1-m*m)/(1+m*m),2*m/(1+m*m),-2*c*m/(1+m*m)],
            [2*m/(1+m*m),(m*m-1)/(m*m+1),2*c/(1+m*m)],
            [0,0,1]
    ]
    rt_vertices = []
    for v in t_vertices:
        mat = np.matrix(reflection_matrix)*np.matrix([[v[0]],[v[1]],[1]])
        mat = mat.tolist()
        rt_vertices.append((mat[0][0],mat[1][0]))
        plt.plot([v[0] for v in rt_vertices],[v[1] for v in rt_vertices])

# axes
plt.plot([-20,20],[0,0])
plt.plot([0,0],[-20,20])
# original traingle 
plt.plot([v[0] for v in t_vertices],[v[1] for v in t_vertices])
# changed traingle
plt.plot([v[0]*rx for v in t_vertices],[v[1]*ry for v in t_vertices])
plt.show()


