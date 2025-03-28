def exponential_function(sigma, n_1, n_2, omega):

    import numpy as np
    
    time_vector = np.linspace(n_1, n_2, 1000)
    complex_vector = np.exp((sigma + 1j * omega)* time_vector)

    return[time_vector,complex_vector]