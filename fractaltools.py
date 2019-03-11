import numpy as np
import collections
import numpy.linalg

from decimal import Decimal


# - add docstrings to each function and usage examples
# - specify variable types
# - argument verification
#
# Add the inverse function for cart2pol

# TODO:
# - remove reference or make it optional with default (0, 0)
# - accept 2 dimensional arrays as input

def cart2pol(points, reference):
    """
        Transforms from cartesian to polar coordinates.
        [[x, y] - ref] -> [[rho, theta]]
    """
    # Numpy array used for builtin array arithmetic
    r  = np.array(reference)
    conversion = lambda p: [np.sqrt(sum((r - p) ** 2)), np.arctan2(*(r - p))]

    return list(map(conversion, points))


# TODO: add changes for spectrum
def spectrum(points, powers, scales):

    # order and remove offset
    points.sort()
    points = points - points[0]

    result = []
    for scale in scales:
        counts = collections.Counter(np.floor(points / scale)).values()
        # Convert to decimal
        counts = np.array(list(map(Decimal, counts)), dtype=np.dtype(Decimal))
        result.append(counts / counts.sum())

    slopes = []
    x = np.log(scales)

    for q in powers:
        y = [(r ** q).sum().ln() for r in result]

        # fit a line
        A = np.vstack([x, np.ones(x.shape)]).T
        # TODO: add more info about the fit
        fit = np.linalg.lstsq(A, np.array(y, dtype=np.float), rcond=-1)
        slopes.append(fit[0][0])

    # Compute the spectrum
    a = np.gradient(slopes, edge_order=2)
    f = a * powers - slopes

    return a, f
