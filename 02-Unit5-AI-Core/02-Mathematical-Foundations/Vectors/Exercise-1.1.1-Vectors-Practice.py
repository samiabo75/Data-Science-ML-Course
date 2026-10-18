# -*- coding: utf-8 -*-
# תרגול השלמת החסר — תרגיל 1.1.1 (ללא פתרונות)
# השלימו כל TODO באמצעות הוראת Python תקינה; הסירו # מהשורה שכתבתם.
import numpy as np
np.set_printoptions(floatmode="fixed", precision=2)
x = np.array([3.0,-5.0,-4.0])
y = np.array([-1.0,-3.0,2.0])

# חיבור וחיסור
# TODO 1: ? + ?
# TODO 2: np.array([?+? for ?,? in zip(x,y)])
# TODO 3: ? - ?
# TODO 4: np.?([?-? for ?,? in ?(?,?)])

# סקלר, מכפלה רכיבית ומכפלה פנימית
alpha = 2
# TODO 5: ? * ?
# TODO 6: np.?([? * ? for ? in ?])
# TODO 7: ? * ?
# TODO 8: np.?([?*? for ?,? in zip(x,y)])
# TODO 9: ? @ ?
# TODO 10: np.?([?*? for ?,? in zip(x,y)])

# נורמות
x = np.array([-5.0,-3.0,2.0])
# TODO 11: np.linalg.?(?,ord=?)
# TODO 12: np.?([np.?(?) for ? in ?])
# TODO 13: np.linalg.?(?,ord=?)
# TODO 14: np.?(x@x)
# TODO 15: np.?(np.?([?**? for ? in ?]))

# קרטזי ↔ פולרי
v = np.array([2.0,3.0])
# TODO 16: r = np.linalg.?(?,ord=?)
# TODO 17: theta_rad = np.?(3.0,2.0)
# TODO 18: theta_deg = np.?(theta_rad)
# TODO 19: polar = np.?([?,?])
# TODO 20: cart_x = ?*np.?(?)
# TODO 21: cart_y = ?*np.?(?)
# TODO 22: v = np.?([?,?])

# נרמול L1 ו-L2
x = np.array([-5.0,-3.0,2.0])
# TODO 23: x_norm = np.linalg.?(?,ord=?)
# TODO 24: l1_norm = ?/np.linalg.?(?,ord=?)
# TODO 25: np.?([?/? for ? in ?])
# TODO 26: np.linalg.?(l1_norm,ord=?)
# TODO 27: x_norm = np.linalg.?(?,ord=?)
# TODO 28: l2_norm = ?/?
# TODO 29: np.?([?/? for ? in ?])
# TODO 30: np.linalg.?(l2_norm,ord=?)

# שאלת חשיבה: למה dot product מחזיר סקלר ולא וקטור?
