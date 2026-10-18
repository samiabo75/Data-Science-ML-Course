# -*- coding: utf-8 -*-
# פתרון מלא — תרגיל 1.1.1: פעולות בווקטורים (על פי מקור ההשתלמות).
import numpy as np
np.set_printoptions(floatmode="fixed", precision=2)

# Add and subtract vectors
x = np.array([3.0, -5.0, -4.0])
y = np.array([-1.0, -3.0, 2.0])
print("x+y vectorized:", x + y)
print("x+y loop:", np.array([a+b for a,b in zip(x,y)]))
print("x-y vectorized:", x - y)
print("x-y loop:", np.array([a-b for a,b in zip(x,y)]))

# Multiply array with scalar
alpha = 2
print("alpha*x vectorized:", alpha*x)
print("alpha*x loop:", np.array([alpha*a for a in x]))

# Element-wise multiplication
print("elementwise vectorized:", x*y)
print("elementwise loop:", np.array([a*b for a,b in zip(x,y)]))

# Dot product: loop equivalent must be summed
print("dot vectorized:", x @ y)
print("dot loop:", np.sum([a*b for a,b in zip(x,y)]))

# L1 norm
x = np.array([-5.0, -3.0, 2.0])
print("L1 norm vectorized:", np.linalg.norm(x, ord=1))
print("L1 norm loop:", np.sum([np.abs(a) for a in x]))

# L2 norm
print("L2 norm library:", np.linalg.norm(x, ord=2))
print("L2 norm dot:", np.sqrt(x @ x))
print("L2 norm loop:", np.sqrt(np.sum([a**2 for a in x])))

# Cartesian to Polar
v = np.array([2.0, 3.0])
r = np.linalg.norm(v, ord=2)
theta_rad = np.arctan2(3.0, 2.0)
theta_deg = np.degrees(theta_rad)
print("radius:", r, "angle(degrees):", theta_deg)
print("polar (r,theta):", np.array([r,theta_rad]))

# Polar to Cartesian (using the same r and theta_rad)
cart_x = r*np.cos(theta_rad)
cart_y = r*np.sin(theta_rad)
v = np.array([cart_x,cart_y])
print("back to Cartesian:", v)

# Normalizing vectors L1
x = np.array([-5.0, -3.0, 2.0])
x_norm = np.linalg.norm(x, ord=1)
l1_norm = x/np.linalg.norm(x, ord=1)
print("L1 normalized vector:", l1_norm)
print("L1 normalized loop:", np.array([a/x_norm for a in x]))
print("L1 norm after:", np.linalg.norm(l1_norm, ord=1))

# Normalizing vectors L2
x_norm = np.linalg.norm(x, ord=2)
l2_norm = x/x_norm
print("L2 normalized vector:", l2_norm)
print("L2 normalized loop:", np.array([a/x_norm for a in x]))
print("L2 norm after:", np.linalg.norm(l2_norm, ord=2))

# Note: For a zero vector, guard against division by zero before normalization.
