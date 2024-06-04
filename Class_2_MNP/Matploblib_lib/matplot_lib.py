import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 10)
y = np.power(x, 3)

plt.plot(x,y, color='r', linewidth='2.0', marker='*')
plt.suptitle('X^3 Curve')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()