# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimSun']
# plt.rcParams['axes.unicode_minus'] = False
# # 投影仪放大倍率，单位都是cm
# l1 = 18.2  # 物体的位置
# a1 = 0.5  # 物体的大小
# a2 = np.array([1.3, 1.5, 1.6, 1.7, 1.9])  # 像的大小
# l2 = 37.2  # L2的位置
# l3 = np.array([87.5, 92.5, 97.5, 102.2, 107.6])  # 屏的位置
# l32 = l3-l2  # 像距
# a3 = a2/a1  # 实际放大率
# l32.sort()
# a3.sort()
# a4 = l32/19  # 理论放大率
# print(l32, a4)
# fig1 = plt.figure(dpi=250)
# plt.plot(l32, a3, ".", label=r"测量值")
# plt.legend(loc="upper left", fontsize="small")
# plt.plot(l32, a4, label=r"理论值")
# plt.legend(loc="upper left", fontsize="small")
# plt.xlabel("像距/cm")
# plt.ylabel("放大率")
# plt.tight_layout()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimSun']
# plt.rcParams['axes.unicode_minus'] = False
# d = np.array([4.2, 4.7, 5.2, 5.7, 6.2, 6.7, 7.2, 7.5])
# Lx = np.array([0.026, 0.096, 0.181, 0.272, 0.326, 0.174, 0.024, 0.001])
# fig1 = plt.figure(dpi=250)
# plt.xlabel("距离/cm")
# plt.ylabel("照度/mW")
# plt.plot(d, Lx)
# plt.plot(d, Lx, ".")
# plt.tight_layout()
# plt.show()
import numpy as np
d1 = np.array([2.0, 3.0, 2.5, 4.0, 3.5, 1.0])
d2 = np.array([7.8, 11.7, 11.2, 16.4, 17.6, 4.4])
fd = d2 / d1
print(fd.mean(), fd.var())
