def step_function (n_1, n_2, n_0, amp):

    import numpy as np
    import matplotlib as plto

# Se define el vector de tiempo "Eje x del plano cartesiano".
    time_vector = np.arange(n_1, n_2+1, step = 1) 

# Se define la variable step_vector la cual contiene un vector de ceros con la misma dimensión de time_vector y de tipo entero.
    step_vector = np.zeros(time_vector.shape, dtype=int)

# Se define la variable contador, con un valor incial de cero.
    counter = 0
    
# Se utiliza el bloque for para recorrer time_vector y mediante el condicional if verificar que se cumpla la condición y cambiar
# los valores que para que así se origine la función scalon unitario

    for i in time_vector:
        
        if i >= n_0 :
            step_vector[counter] = 1 * amp
        counter = counter+1

# Finalmente se retorna time_vector y step_vector, los cuales son los vectores que se usan en matplotlib
    return[time_vector, step_vector]
