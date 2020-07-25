import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

## create 2D vector

u = np.array([1, 3])
v = np.array([ 2, 4])

## Visualize the 2D vector

def plot_vector2d(vector2d, origin=[0, 0], **options):
    return plt.arrow(origin[0], origin[1], vector2d[0], vector2d[1],
              head_width=0.2, head_length=0.3, length_includes_head=True,
              **options)


## The norm of a vector  (length of vector)
norm_u = LA.norm(u)
print(norm_u)

## Vector addition
w = u + v
print(w)

## multiplication
p = u*2

## Dot product -- > |u| * |v| * cos0
v_dot = np.dot(u,v)

## multiple q
plot_vector2d(w, color="g")
plot_vector2d(u, color="r")
plot_vector2d(v, color="b")
#plot_vector2d(v_dot, color="g")
plt.axis([0, 15, 0, 15])
plt.grid()
plt.show()