import numpy
import scipy.ndimage

_shape = (300, 300)

def half_plane(point, direction):
    shape = _shape
    x, y = numpy.meshgrid(numpy.arange(shape[0]), numpy.arange(shape[1]), indexing="ij")
    direction = direction / numpy.linalg.norm(direction)
    a = (x - point[0])*direction[0] + (y-point[1])*direction[1] > 0
    return a


def square(side):
    return numpy.float64(half_plane((_shape[0]/2-side/2, _shape[1]/2), (1, 0)) *
                         half_plane((_shape[0]/2, _shape[1]/2+side/2), (0, -1)) *
                         half_plane((_shape[0]/2+side/2, _shape[1]/2), (-1, 0)) *
                         half_plane((_shape[0]/2, _shape[1]/2-side/2), (0, 1)))

def rectangle(side1, side2):
    return numpy.float64(half_plane((_shape[0]/2-side2/2, _shape[1]/2), (1, 0)) *
                         half_plane((_shape[0]/2, _shape[1]/2+side1/2), (0, -1)) *
                         half_plane((_shape[0]/2+side2/2, _shape[1]/2), (-1, 0)) *
                         half_plane((_shape[0]/2, _shape[1]/2-side1/2), (0, 1)))

def triangle(side):
    return numpy.float64(half_plane((_shape[0]/2-side/2, _shape[1]/2-side/2), (numpy.cos(numpy.pi*2/3), numpy.sin(numpy.pi*2/3))) *
                         half_plane((_shape[0]/2-side/2, _shape[1]/2+side/2), (numpy.cos(numpy.pi*2/3), -numpy.sin(numpy.pi*2/3))) *
                         half_plane((_shape[0]/2-side/2, _shape[1]/2-side/2), (1, 0)))

def oval(axis1, axis2):
    shape = _shape
    x, y = numpy.meshgrid(numpy.arange(shape[0]), numpy.arange(shape[1]), indexing="ij")
    return numpy.float64((2*(x-shape[0]/2)/axis2)**2 + (2*(y-shape[1]/2)/axis1)**2 < 1.)

def circle(side):
    return oval(side, side)


def gaussian(sigma, shape=_shape):
    x, y = numpy.meshgrid(numpy.arange(shape[0]), numpy.arange(shape[1]), indexing="ij")
    return numpy.exp(-((x-shape[0]/2)**2 + (y-shape[1]/2)**2) / (2*sigma**2))

def rotate(array, angle):
    padded = numpy.zeros((array.shape[0]+1, array.shape[1]+1), dtype=array.dtype)
    padded[:array.shape[0], :array.shape[1]] = array
    rotated_padded = scipy.ndimage.rotate(padded, angle*180/numpy.pi, reshape=False)
    rotated = rotated_padded[:array.shape[0], :array.shape[1]]
    return rotated
