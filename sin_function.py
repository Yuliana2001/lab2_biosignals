def sin_function (n_1, n_2, omega, theta):

    import numpy as np

# Se define el vector de tiempo "Eje x del plano cartesiano".
    vector_time = np.linspace(n_1, n_2, 1000)

# Se define la variable signal_sin utilizando una función dentro de numpy la cuál se construye con la frecuencia angulat y desfase,
# en este caso teoricamente corresponden a la frecuencia angular y desfase de dicha función.
    signal_sin = np.sin(omega*vector_time + theta)

# Finalmente se retorna time_vector y step_vector, los cuales son los vectores que se usan en matplotlib
    return [vector_time, signal_sin]