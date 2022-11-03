import matplotlib.pyplot as plt

activities=['Sleeping','Work','Play','Eating','Tv']
hours=[6,7,3,3,3]
cols=['c','m','r','b','g']

plt.pie(hours,
       labels=activities,
       colors=cols,
       autopct='%1.1f%%',
       startangle=90)
plt.title('PIE CHART')
plt.show()