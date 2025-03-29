import numpy as np
import matplotlib.pyplot as plto
import pandas as pd

""" Ejemplo: Impulso Unitario"""

# Se importa la función Impulse_function creada anteriormente oara crear la función impulso.
from impulse_function import impulse_function

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(impulse_function(0,-2,2,1)[0], impulse_function(0,-2,2,1)[1])
plto.title('Función Impulso Unitario')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.show()

""" 1) Implemente una función en Python que permita generar una función escalón unitario, definida en
un intervalo n1≤n0≤n2"""

from step_function import step_function

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(step_function(-5,5,0,1)[0],step_function(-5,5,0,1)[1])
plto.title('Función Escalón Unitario')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.show()


""" 2) Implemente una función en Python que permita generar una función rampa, definida en un intervalo
𝑛1≤𝑛0≤𝑛2 con una pendiente m."""

from ramp_function import ramp_function

time_vector = ramp_function(0,-5,5,1)[0]
ramp_vector = ramp_function(0,-5,5,1)[1]

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(time_vector, ramp_vector)
plto.title('Función Rampa')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.show()

""" 3) Implemente una función en Python que permita generar una función exponencial compleja, definida en
un intervalo 𝑛1≤𝑛0≤𝑛2. """

from exponential_function import exponential_function

exponential_function(0.05,-10,60,0.3)

time_vector = exponential_function(0.05,-10,60,0.3)[0]
complex_function = exponential_function(0.05,-10,60,0.3)[1]

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.plot(time_vector, np.real(complex_function), color = 'red', label = 'Parte Real')
plto.plot(time_vector, np.imag(complex_function), color = 'blue', label = 'Parte Imaginaria')
plto.title('Función Exponencial Compleja')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True) 
plto.legend()
plto.show()

""" 4) Implemente una función en Python que permita generar una función sinusoidal, definida en un intervalo
𝑛1≤𝑛0≤𝑛2. """

from sin_function import sin_function

[time_vector, signal] = sin_function(-10,10,3.14,0)

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.plot(time_vector, signal, color = 'pink')
plto.title('Función Seno')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True) 
plto.show()

""" 5) Genere las siguientes secuencias usando las funciones básicas de Python que se han presentado. Grafique 
los resultados."""

""" a)"""

# Se crea la variable n, a la cual se le asigna el array que corresponde al vector de tiempo para dicha función
# el cual también se utiliza para crear el eje horizontal "x" del plano cartesiano, la función en este caso se
# compone de 4 argumentos los cuales son desfase de la señal, inicio de vector de tiempo, final del vector de tiempo,
# y la pendiente de la rampa recpectivamente: n_0, n_1,n_2, slope.
n = impulse_function(-1,-10,10,3)[0]

# Para este caso se crean las variables x_1, x_2, x_3, x_4, x_5 en el que se invoca la función rampa construida
# esta función en este caso se compone de 4 argumentos los cuales son desfase de la señal, inicio de vector de tiempo, final del vector de tiempo,
# y la pendiente de la rampa recpectivamente: n_0, n_1,n_2, slope. Los valores de los argumentos se ingresan de tal manera que cincidan con
# la función requerida, en este caso algunos argumentos tienen un valor contrario al mencionado anteriormente pero es solo por la definición de la función ramp_function, dentro de la función se agrego
# el valor de la pendiente la cuál hace que la diagonal de la pendiente cresca para valores positivos o disminuya para valores negativos
x_1 = impulse_function(-1,-10,10,3)
x_2 = impulse_function(-3,-10,10,5)
x_3 = impulse_function(-2,-10,10,3)
x_4 = impulse_function(0,-10,10,3)
x_5 = impulse_function(0,-10,10,1)

# Se usa la sintaxis [1] para retornar la segunda posición del array que corresponde al ramp_vector la función ramp_function. 
# Se suman cada uno de los vectores para obtener así la función final requerida.
x_n = x_1[1] + x_2[1] + x_3[1] + x_4[1] + x_5[1]

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(n, x_n)
plto.title('Suma Entre Funciones Impulso')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.xticks(np.arange(-10,10+1, step=1))
plto.show()

""" b) """

# Se crea la variable n, a la cual se le asigna el array que corresponde al vector de tiempo para dicha función
# el cual también se utiliza para crear el eje horizontal "x" del plano cartesiano, la función en este caso se
# compone de 4 argumentos los cuales son desfase de la señal, inicio de vector de tiempo, final del vector de tiempo,
# y la pendiente de la rampa recpectivamente: n_0, n_1,n_2, slope. Se usa la sintaxis [0] para retornar la primera
# posición del array que corresponde al vector tiempode la función ramp_function. 
n = ramp_function(-3,-10,10,2)[0]

# Se crea la variable x_n, a dicha variable se le asigna la suma de las funciones rampas como dicta la función x_4(n)
# la cual solo existe dentro del intervalo de -10 a 10, esta función esta compuesta por varios desplazamientos un desplazamiento
# hacia la izquierda de tres unidades, otro hacia la derecha de dos unidades y un ultimo hacia la derecha con tres unidades
# los cuales corresponden al primer argumento de la función, en este caso algunos argumentos tienen un valor contrario
# al mencionado anteriormente pero es solo por la definición de la función ramp_function, dentro de la función se agrego
# el valor de la pendiente la cuál hace que la diagonal de la pendiente cresca para valores positivos o disminuya para valores negativos
# Se usa la sintaxis [1] para retornar la segunda posición del array que corresponde al ramp_vector la función ramp_function. 
x_n = ramp_function(-3,-10,10,2)[1] + ramp_function(2,-10,10,-1)[1] + step_function(-10,10,3,-5)[1]

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.plot(n, x_n)
plto.title('Operaciones Entre Funciones')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.xticks(np.arange(-10,10+1, step=1))
plto.show()

# Para ambos casos el vector de muestras es discreto debido a que son impulsos que toman un valor especificos en 
# determinados momentos de tiempo, no es posible que sea un vector continuo debido a que para este caso no se conoce
# una frecuencia establecida para la aparición de nuevos impulsos por lo que no sería posible estimar vectores
# anteriores o posteriores a los que dicen las funciones, además cabe resaltar que los vectores siempren deben tener la 
# misma dimensión.

""" 6) Genere la siguiente secuencia

𝑥[𝑛]=   {𝑟[𝑛] 
        0≤𝑛≤5𝑟[𝑛−5] 
        6≤𝑛≤11𝑟[𝑛−10] 12≤𝑛≤17

"""

# Se generan segmentos de la señal usando la función ramp_function.
# Cada llamada devuelve dos valores: la secuencia x y su respectivo eje de tiempo n.
x_1 = ramp_function(0,0,5,1)[1] # Primer segmento de la señal
n_1 = ramp_function(0,0,5,1)[0]
x_2 = ramp_function(5,6,11,1)[1] # Segundo segmento de la señal
n_2 = ramp_function(5,6,11,1)[0]
x_3 = ramp_function(10,12,17,1)[1] # Tercer segmento de la señal
n_3 = ramp_function(10,12,17,1)[0]

"""se concatena, porque están definidas en un rango diferente de n"""
n = np.concatenate((n_1, n_2, n_3)) # Une los vectores de tiempo en uno solo
x = np.concatenate((x_1, x_2, x_3)) # Une las señales en una sola función

"""se deriva la función de interés """
x2 = np.diff(x) 
rango_derivada=np.arange(1,len(x2)+1)  # Vector de tiempo para la derivada, desde 1 hasta la cantidad de elementos de x2 + 1

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.subplot(2,1,1)
plto.plot(n,x)
plto.title('Función Normal')
plto.ylabel('Amplitud')
plto.grid(True)
plto.subplot(2,1,2)
plto.stem(rango_derivada,x2)
plto.title('Función Derivada')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.yticks(np.arange(-5,5+1, step=1))
plto.grid(True)
plto.show()

"""  7) Sea x(n) = {0,1,2,3,4, 5̂, 4,3,2,1,0,1,2,3,4,5,5,5,5,10,10,10,10}. Genere la secuencia anterior y
grafique los resultados. Use las funciones que generó antes para generar la secuencia
concatenando secuencias más simples. Además, encuentre las siguientes secuencias:

"""
# Se construye la secuencia x(n) utilizando ramp_function y step_function.
x_1 = ramp_function(0,0,4,1)[1] # Parte creciente de la señal
x_2 = ramp_function(5,5,9,-1)[1] + step_function(5,9,5,5)[1] # Parte decreciente
x_3 = ramp_function(10,10,15,1)[1]  # Segunda parte creciente
x_4 = step_function(16,18,16,5)[1] # Parte constante en 5
x_5 = step_function(19,22,19,10)[1] # Parte constante en 10
x_n = np.concatenate((x_1,x_2,x_3,x_4,x_5)) # Se concatenan las partes para formar la señal completa.

# Se genera un vector de tiempo
# 0 = El primer valor del vector será 0 (inicio del tiempo).
# np.shape(x_n) - 1 = El último valor será np.shape(x_n) - 1, para que el eje de tiempo cubra toda la señal.
# np.shape(x_n) = Se generan exactamente np.shape(x_n) valores para asegurar que haya un punto de tiempo para cada valor en x_n.
time_vector = np.linspace(0,np.shape(x_n)[0]-1, np.shape(x_n)[0])

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(time_vector, x_n)
plto.grid(True)
plto.title('Función Derivada')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.show()

""" a) x5(n) = 2x(n − 4) + x(n) """

x_0 = np.zeros(4) # Se crea un vector de ceros de longitud 4 

# Se construye la señal x5(n) = 2x(n − 4) + x(n)
# 1. np.hstack((x_0, x_n)): Desplaza x_n 4 posiciones a la derecha agregando ceros al inicio.
# 2. np.hstack((x_n, x_0)): Desplaza x_n 4 posiciones a la izquierda agregando ceros al final.
# 3. Se multiplica la primera por 2 y se suma la segunda para formar la ecuación dada.
x5 = 2*np.hstack((x_0,x_n))+np.hstack((x_n,x_0)) 

# Se genera el vector de tiempo con la misma cantidad de elementos que x5.
# 0 = El primer valor del vector será 0 (inicio del tiempo).
# np.shape(x5)[0] - 1 = El último valor será np.shape(x5)[0] - 1, para cubrir toda la señal.
# np.shape(x5)[0] = Se generan exactamente np.shape(x5)[0] valores, asegurando que haya un punto de tiempo para cada valor en x5.
n = np.linspace(0, np.shape(x5)[0] - 1, np.shape(x5)[0])  
n = np.linspace(0,np.shape(x5)[0]-1,np.shape(x5)[0])

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(n,x5)
plto.title('Primera Concatenación')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.show()

""" b) x6(n) = 0.001e0.5nx(n) + 10sin(0.05πn) x(n + 2), −20 ≤ n ≤ 20. """

# Se genera un vector de tiempo 'n' desde -20 hasta 20 con 41 puntos
# Esto asegura que cada punto en 'x6' tenga un valor de tiempo correspondiente
n = np.linspace(-20,20,41)

# np.ones(20) crea un vector de unos para completar los primeros 20 valores
# x_n[:-2] toma la señal x_n sin los últimos 2 valores, simulando x(n) en este rango de tiempo
xn_1 = np.hstack((np.ones(20),x_n[:-2]))
# np.ones(18) crea un vector de unos para rellenar los primeros 18 valores.
# x_n se concatena directamente, simulando el desplazamiento x(n+2).
xn_2 = np.hstack((np.ones(18),x_n))
# Se remplazan las anteriores variables en la ecuación
x6 = 0.001*np.exp(0.5*n)*xn_1+10*np.sin(0.05*np.pi*n)*xn_2

# Se hace uso de la libreria matplotlib mediante plto para usar sus funnciones como stem, title, etc y 
# generar la gráfica con titulo y ejes.
plto.stem(n,x6)
plto.title('Segunda Concatenación')
plto.xlabel('Tiempo (s)')
plto.ylabel('Amplitud')
plto.grid(True)
plto.show()
