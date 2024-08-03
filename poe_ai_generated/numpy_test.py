import numpy as np

x = [1.0, 1.0, 1.0, -2.0, np.pi / 2.0, 4.0, 5.0, -10.0, 10.0, 1.0, 2.0, 3.0]
a10 = 10.0
an10 = -10.0
m1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

xm_min = str(min(np.ma.core.masked_array(np.array(x), mask=m1)))

xm_max = str(max(np.ma.core.masked_array(np.array(x), mask=m1)))

m2 = []
for x in m1:
    m2.append(np.longdouble(x))
m3 = []
for x in m1:
    m3.append(np.longfloat(x))

m4 = np.array(m2).tolist()
m5 = np.array(m3).tolist()
pi_string = np.string_(np.pi)
pi_unicode = np.unicode_(pi_string)
