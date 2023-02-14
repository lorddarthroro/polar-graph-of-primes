import matplotlib.pyplot as plt
import sympy

plt.axes(projection = 'polar')

p = 1

while True:
    p = sympy.nextprime(p)
    plt.plot(p, p, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
    plt.pause(.001)
