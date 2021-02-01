#CANUL CHAVEZ JUDITH ELUZAI
#No.CONTROL: 18390034
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, sqrt

plt.axis([0,160,120,0])
plt.axis('on')
plt.grid(True)

#ubicacion del plano
x=[40,30,80,45,85] 
y=[60,10,60,45,40]
z=[0,0,0,0]

plt.plot([x[0],x[1]],[y[0],y[1]],color='blue') 
plt.plot([x[1],x[2]],[y[1],y[2]],color='blue')
plt.plot([x[2],x[0]],[y[2],y[0]],color='blue')

#pedimos las coordenadas del hitpoint
puntox=int(input('teclea la coordena "X" del hitpoint:'))
puntoy=int(input('teclea la coordena "Y" del hitpoint:'))

#se guardan las coordenadas en x and y 
xg=[puntox]
yg=[puntoy]

plt.scatter(xg[0],yg[0],s=15,color='r')

#___trazado
plt.plot([x[0],xg[0]],[y[0],yg[0]],linestyle=':',color='r') 
plt.plot([x[1],xg[0]],[y[1],yg[0]],linestyle=':',color='r')
plt.plot([x[2],xg[0]],[y[2],yg[0]],linestyle=':',color='r')

plt.text(100,29, 'Hitpoint'+str(xg) + str(yg), color='k')
plt.text(100,34, 'Area: ', color='k')
plt.title('3D')

plt.show()
