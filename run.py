import matplotlib.pyplot as plt
from contadorTiempo import timeCounter
from contador import counter
from rosco import rosco

color1 = 'darkorange'
r1 = rosco(name='Rosco1')
c1 = counter(color=color1, name='Contador1')
t1 = timeCounter(color=color1, name='Tiempo1')
r1.draw()
c1.draw()
t1.draw()

color2 = 'dodgerblue'
r2 = rosco(name='Rosco2')
c2 = counter(color=color2, name='Contador2')
t2 = timeCounter(color=color2, name='Tiempo2')
r2.draw()
c2.draw()
t2.draw()

plt.show()
