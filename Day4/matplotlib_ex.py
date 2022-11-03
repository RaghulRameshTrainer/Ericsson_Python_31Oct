import matplotlib.pyplot as plt

plt.plot([1,3,5,7,9],[2,4,8,3,6],'r',label='2021 business',linewidth=3)
plt.plot([2,4,6,8,10],[8,5,3,7,3],'g',label='2022 business',linewidth=3)
plt.legend()
plt.show()