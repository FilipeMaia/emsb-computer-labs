import numpy
import matplotlib.pyplot
from PIL import Image
#image_original = matplotlib.pyplot.imread("/Users/ekeberg/Work/Courses/Experimental Methods in Structural Biology/2020/Notebooks/tomas.jpeg")
image_original = matplotlib.pyplot.imread("/Users/ekeberg/Work/Courses/Experimental Methods in Structural Biology/2020/Notebooks/filipe.png")
image = image_original[450:150:-1, 50:350].sum(axis=2)
image = (image-image.min())/(image.max()-image.min())
image = image / image.max()
image *= 255
image = numpy.uint8(image)
#print(image.max())
image_pil = Image.fromarray(image)
#image_pil.save("tomas.png")
image_pil.save("filipe.png")
#matplotlib.pyplot.imsave("tomas.png", image)
