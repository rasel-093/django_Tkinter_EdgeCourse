import matplotlib.pyplot as plt
import numpy as np

# Bar plot
# month = ['January', 'March', 'May']
# sales = [200,3000,1500]
# plt.bar(month, sales, color='r')
# plt.title('Month VS Sales')
# plt.suptitle("Shop Summary")
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.show()

# Scatter plot
x = np.array([2, 4, 9, 6, 23])
y = np.power(x, 3)
# plt.scatter(x, y)
plt.stem(x,y)
plt.show()
