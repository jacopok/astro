import numpy as np

default_func = lambda x : 10**x

def recalculate_errors(x0, sigma, func=default_func):

    xs = np.ones(2) * x0
    err_xs = xs + np.array([-sigma, sigma])
    y = func(xs[0])
    err_ys = func(err_xs)

    return(y, err_ys-y)