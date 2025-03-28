def impulse_function(n_0, n_1,n_2, am):
    
    import numpy as np

    n = np.arange(n_1, n_2+1)
    x = (n-n_0) == n_0
    y_axis = am*(n==n_0).astype(int)

    return [n, y_axis]    