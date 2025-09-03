import numpy

def detector_coordinates(distance, pixel_size, shape=(128, 128)):
    x = pixel_size*(numpy.arange(shape[0]) - shape[0]/2 + 0.5)
    y = pixel_size*(numpy.arange(shape[1]) - shape[1]/2 + 0.5)
    X, Y = numpy.meshgrid(x, y, indexing="ij")
    Z = distance*numpy.ones(X.shape)
    return X, Y, Z
