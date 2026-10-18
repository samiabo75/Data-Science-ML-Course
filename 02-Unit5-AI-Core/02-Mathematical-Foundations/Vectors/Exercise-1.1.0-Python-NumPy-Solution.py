# -*- coding: utf-8 -*-
# פתרון מלא — תרגיל 1.1.0: Python ו-NumPy בסיסי
# לפי סדר התרגיל המקורי של ההשתלמות, כולל list comprehensions, for ו-zip.
import numpy as np

# List1, List2, list3
list1 = [i for i in range(1, 11, 2)]
print("list1:", list1)
list2 = [i for i in range(2, 11, 2)]
print("list2:", list2)
for item1, item2 in zip(list1, list2):
    print(item1 + item2, end=" ")
print()
list3 = [item1 + item2 for item1, item2 in zip(list1, list2)]
print("list3:", list3)
print(sum(list1), sum(list2), sum(list3))

# np1, np2, np3
np1 = np.array([i for i in range(11, 21, 2)])
print("np1:", np1)
np2 = np.array([i + 1 for i in range(11, 21, 2)])
print("np2:", np2)
for item1, item2 in zip(np1, np2):
    print(item1 + item2, end=" ")
print()
np3 = np.array([item1 + item2 for item1, item2 in zip(np1, np2)])
print("np3:", np3)
print(np.sum(np1), np.sum(np2), np.sum(np3))

# np4, np5, np6, np7
np4 = np.array([x**2 for x in np1])
print("np4:", np4)
np5 = np.array([np.sqrt(x) for x in np2])
print("np5:", np5)
np6 = np.array([-3, 5, -7, -8, 11])
print("np6:", np6)
np7 = np.array([np.abs(x) for x in np6])
print("np7:", np7)
print("Sum of absolute values:", np.sum(np.array([np.abs(x) for x in np6])))
