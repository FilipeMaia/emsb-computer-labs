import numpy
import matplotlib.pyplot

original = matplotlib.pyplot.imread("Unsharped_eye.jpg")[::-1, :, :]
cropped = original[390:, :175]

scaled = 0.1 + (cropped / 255)*0.6

matplotlib.pyplot.imsave("eye.jpg", scaled, origin="upper")
