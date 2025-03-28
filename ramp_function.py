def ramp_function(n_0, n_1, n_2, slope):

    import numpy as np

# Se define el vector de tiempo "Eje x del plano cartesiano".
    time_vector = np.linspace(n_1,n_2+1,1000)

# Se define la variable step_vector la cual contiene un vector de ceros con la misma dimensión de time_vector y de tipo entero.
    ramp_vector = np.zeros(time_vector.shape)

# Se define la variable contador, con un valor incial de cero.
    counter = 0

# Se utiliza el bloque for para recorrer time_vector y mediante los condicionales if y elif verificar que se cumpla la condición y cambiar
# los valores que para que así se origine la función rampa

    for i in time_vector:

        if i < n_0 :
            ramp_vector[counter] = 0

        elif i >= n_0 :
            ramp_vector[counter] = (i - n_0) * slope 

        counter = counter+1
        
# Finalmente se retorna time_vector y step_vector, los cuales son los vectores que se usan en matplotlib
    return[time_vector, ramp_vector]