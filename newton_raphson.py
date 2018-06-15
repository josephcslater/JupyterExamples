"""
Demonstration of Python Scientific computing.

Uses Newton Raphson's method as a vehicle.
"""

import matplotlib.pyplot as plt
import scipy as sp


def myfunc(x):
    """
    Generic function.

    Parameters
    ----------
    x: float or array_like
        The value or array at which to calculate the function

    Examples
    --------

    Execution on a float

    >>> from newton_raphson import *
    >>> myfunc(3.0)
        11.0

    Execution on a SciPy array_like

    >>> a = np.linspace(0,10,10)
    >>> myfunc(a)
        array([  -4.        ,   -0.54320988,    5.38271605,   13.77777778,
             24.64197531,   37.97530864,   53.77777778,   72.04938272,
             92.79012346,  116.        ])
    """
    return x**2+2*x-4


def newton_raphson_plot(function, x0=0, dx=1e-10, eps=1e-10):
    """
    Solve for a root of a function using Newton Raphson's method.

    Also plots the process.

    Parameters
    ----------
    function : string
        String with name of function to be solved for *function(x) = 0*
    x0       : float
        Initial guess for *x* near *function(x) = 0*
    dx       : float
        Delta x used for finite difference calculation of slope
    eps      : float
        Absolute value of *function(x)* which is considered zero.

    Examples
    --------
    >>> from newton_raphson import *
    >>> def myfunc(x):
    ...     return x**2+2*x-4
    >>> function_name = 'myfunc'
    >>> newton_raphson_plot(function_name, x0=2)
        (1.23606797..., ...)
    """
    deltax = 2 * eps
    count = 0
    x = x0
    y = np.linspace(1, 6, 200)
    plt.plot(y, globals()[function](y))
    plt.ylabel('$f(x)$')
    plt.xlabel('$x$')
    plt.title('Newton Raphson search for solution to $f(x)=0$.')
    plt.grid(True)
    plt.plot(np.array([x0, x0]), np.array([globals()[function](x0), 0]), 'r')
    plt.plot(np.array([x0]), np.array([globals()[function](x0)]), 'r*')
    while abs(globals()[function](x)) > eps and count < 50:
        count += 1
        plt.plot(np.array([x, x]), np.array([globals()[function](x), 0]), 'r')
        plt.plot(np.array([x]), np.array([globals()[function](x)]), 'r*')
        f = globals()[function](x)
        f2 = globals()[function](x + dx)
        dfdx = (f2 - f) / dx
        deltax = -f / dfdx
        x = x + deltax
        xr = np.linspace(x, x - deltax, 200)
        y = xr * dfdx - x * dfdx
        plt.plot(xr, y, 'y')  # Current point
    return x, deltax


def newton_raphson(function, x0=0, dx=1e-10, eps=1e-10):
    """
    Solve for a root of a function using Newton Raphson's method.

    Parameters
    ----------
    function : string
        String with name of function to be solved for *function(x) = 0*
    x0       : float
        Initial guess for *x* near *function(x) = 0*
    dx       : float
        Delta x used for finite difference calculation of slope
    eps      : float
        Absolute value of *function(x)* which is considered zero.

    Examples
    --------
    >>> from newton_raphson import *
    >>> def myfunc(x):
    ...     return x**2+2*x-4
    >>> function_name = 'myfunc'
    >>> newton_raphson(function_name, x0=2)
        (1.2360679..., ...)
    """
    deltax = 2*eps
    count = 0
    x = x0
    # loop until it converges, but no more than 50 times
    while abs(deltax) > eps and count < 50:
        count += 1 # I can add 1 to the variable *count*. Neat Python shortcut.
        # This is a comment
        # The next line is "Matlab style" and *bad*
        #f = eval(function + '('+ str(x) + ')')
        f = globals()[function](x)  #We explain later.
        #f2 = eval(function + '('+ str(x+dx) + ')')
        f2 = globals()[function](x+dx)
        dfdx = (f2-f)/dx
        deltax = -f/dfdx
        x = x + deltax
    return x, deltax
