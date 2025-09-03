import matplotlib
import matplotlib.pyplot
import numpy

def fourier_transform(a):
    return numpy.fft.fftshift(numpy.fft.fftn(numpy.fft.ifftshift(a)))

def inverse_fourier_transform(a):
    return numpy.fft.fftshift(numpy.fft.ifftn(numpy.fft.ifftshift(a)))

# def plot_real(a):
#     x_axis = numpy.linspace(-1, 1, len(a))

#     fig = matplotlib.pyplot.figure(figsize=(12, 4))
#     fig.clear()
#     ax = fig.add_subplot(111)
#     ax.plot(x_axis, a)
#     fig.canvas.draw()
    
def plot(a, dx=1e-9):
    x_axis = dx*(numpy.arange(len(a)) - len(a)/2 + 0.5) * 1e9
    
    fig = matplotlib.pyplot.figure(figsize=(6, 4))
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(x_axis, a)
    ax.set_xlabel(r"Real space [nm]")
    fig.canvas.draw()

def plot_complex(a, type="polar", dx=1e-9):
    # x_axis = numpy.linspace(-1, 1, len(a))
    x_axis = dx*(numpy.arange(len(a)) - len(a)/2 + 0.5) * 1e9
    
    fig = matplotlib.pyplot.figure(figsize=(12, 4))
    fig.clear()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    if type == "polar":
        ax1.plot(x_axis, abs(a))
        ax1.set_title("Abs")
        ax1.set_xlabel("Real space [nm]")
        ax2.plot(x_axis, numpy.angle(a))
        ax2.set_yticks([-numpy.pi, -numpy.pi/2, 0, numpy.pi/2, numpy.pi])
        ax2.set_yticklabels([r"$-\pi$", r"$-\pi/2$", r"0", r"$\pi/2$", r"$\pi$"])
        ax2.set_title("Phase")
        ax2.set_xlabel("Real space [nm]")
    elif type == "realimag":
        ax1.plot(x_axis, numpy.real(a))
        ax1.set_title("Real")
        ax1.set_xlabel("Real space [nm]")
        ax2.plot(x_axis, numpy.imag(a))
        ax2.set_title("Imag")
        ax2.set_xlabel("Real space [nm]")
    fig.canvas.draw()

    
def plot_fourier_transform(a, type="polar", dx=1e-9):
    plot_size = 1000
    a_big = numpy.zeros(plot_size, dtype=a.dtype)
    a_big[plot_size//2-len(a)//2:plot_size//2-len(a)//2+len(a)] = a
    
    a_ft = fourier_transform(a_big)

    x_axis = numpy.fft.fftshift(numpy.fft.fftfreq(len(a_big), dx))*1e-9
    
    # x_step = 1/(len(a)/2)
    # x_axis = x_step*numpy.arange(-len(a)/2, len(a)/2)
    
    fig = matplotlib.pyplot.figure(figsize=(12, 4))
    fig.clear()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    if type == "polar":
        ax1.plot(x_axis, abs(a_ft))
        ax1.set_title("Abs")
        ax1.set_xlabel(r"Fourier space [nm$^{-1}$]")
        ax2.plot(x_axis, numpy.angle(a_ft))
        ax2.set_ylim((-numpy.pi, numpy.pi))
        ax2.set_yticks([-numpy.pi, -numpy.pi/2, 0, numpy.pi/2, numpy.pi])
        ax2.set_yticklabels([r"$-\pi$", r"$-\pi/2$", r"0", r"$\pi/2$", r"$\pi$"])
        ax2.set_title("Phase")
        ax2.set_xlabel(r"Fourier space [nm$^{-1}$]")
    elif type == "realimag":
        ax1.plot(x_axis, numpy.real(a_ft))
        ax1.set_title("Real")
        ax1.set_xlabel(r"Fourier space [nm$^{-1}$]")
        ax2.plot(x_axis, numpy.imag(a_ft))
        ax2.set_title("Imag")
        ax2.set_xlabel(r"Fourier space [nm$^{-1}$]")
    fig.canvas.draw()

    
def imshow(a, log=False, **kwargs):
    fig = matplotlib.pyplot.figure(figsize=(6, 5))
    fig.clear()
    ax1 = fig.add_subplot(111)
    if log:
        im = ax1.imshow(numpy.real(a), norm=matplotlib.colors.LogNorm(), origin="lower", cmap="gray", **kwargs)
    else:
        im = ax1.imshow(numpy.real(a), origin="lower", cmap="gray", **kwargs)
    fig.colorbar(im)
    fig.canvas.draw()
    
# def imshow_complex(a, type="polar", log=False, colorbar=True):
#     fig = matplotlib.pyplot.figure(figsize=(20, 8))
#     fig.clear()
#     ax1 = fig.add_subplot(121)
#     ax2 = fig.add_subplot(122)
#     if type == "polar":
#         if log:
#             im1 = ax1.imshow(abs(a), norm=matplotlib.colors.LogNorm(vmin=1e-6), origin="lower")
#         else:
#             im1 = ax1.imshow(abs(a), origin="lower")
#         im2 = ax2.imshow(numpy.angle(a), cmap="hsv", vmin=-numpy.pi, vmax=numpy.pi, origin="lower")
#         fig.colorbar(im1, ax=ax1)
#         fig.colorbar(im2, ax=ax2)
#         ax1.set_title("Abs")
#         ax2.set_title("Phase")
#     elif type == "realimag":
#         if log:
#             raise ValueError("Can't use log scale together with realimag type")
#         im1 = ax1.imshow(numpy.real(a), origin="lower")
#         im2 = ax2.imshow(numpy.imag(a), origin="lower")
#         fig.colorbar(im1, ax=ax1)
#         fig.colorbar(im2, ax=ax2)
#         ax1.set_title("Real")
#         ax2.set_title("Imag")
#     fig.canvas.draw()

def imshow_complex(a, type="polar", log=False):
    # a_ft = fourier_transform(a)

    if type in ("polar", "realimag"):
        fig = matplotlib.pyplot.figure(figsize=(12, 5))
        fig.clear()
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
    else:
        fig = matplotlib.pyplot.figure(figsize=(6, 5))
        fig.clear()
        ax1 = fig.add_subplot(111)
    if type == "polar":
        if log:
            im1 = ax1.imshow(abs(a), norm=matplotlib.colors.LogNorm(vmin=1e-6), origin="lower")
        else:
            im1 = ax1.imshow(abs(a), origin="lower")
        im2 = ax2.imshow(numpy.angle(a), cmap="hsv", vmin=-numpy.pi, vmax=numpy.pi, origin="lower")
        fig.colorbar(im1, ax=ax1)
        cb2 = fig.colorbar(im2, ax=ax2, ticks=[-numpy.pi, -numpy.pi/2, 0, numpy.pi/2, numpy.pi])
        cb2.ax.set_yticklabels([f"$-\pi$", f"$-\pi/2$", f"$0$", f"$\pi/2$", f"$\pi$"])
        ax1.set_title("Abs")
        ax2.set_title("Phase")
    elif type == "realimag":
        if log:
            raise ValueError("Can't use log scale together with realimag type")
        im1 = ax1.imshow(numpy.real(a), origin="lower")
        im2 = ax2.imshow(numpy.imag(a), origin="lower")
        fig.colorbar(im1, ax=ax1)
        fig.colorbar(im2, ax=ax2)
        ax1.set_title("Real")
        ax2.set_title("Imag")
    elif type == "abs":
        if log:
            im1 = ax1.imshow(abs(a), norm=matplotlib.colors.LogNorm(vmin=1e-6), origin="lower")
        else:
            im1 = ax1.imshow(abs(a), origin="lower")
        fig.colorbar(im1, ax=ax1)
        ax1.set_title("Abs")
    elif type == "real":
        if log:
            raise ValueError("Can't use log scale together with realimag type")
        im1 = ax1.imshow(numpy.real(a), origin="lower")
        fig.colorbar(im1, ax=ax1)
        ax1.set_title("Real")
    fig.canvas.draw()

def complex(a, b):
    return numpy.array(a) + 1.j*numpy.array(b)

random = numpy.random.random

def repeat(a, n):
    return numpy.concatenate([a]*n)

class FourierDecomposition:
    def __init__(self):
        self._data = {}

    def clear(self):
        self._data = {}
        
    def add_value(self, x, value):
        self._data[x] = value

    def plot_real(self):
        fig = matplotlib.pyplot.figure(figsize=(14, 7))
        fig.clear()
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        ax1.vlines(self._data.keys(), 0, [abs(v) for v in self._data.values()], color="black")
        #ax1.plot(self._data.keys(), [abs(v) for v in self._data.values()], 'o', color="black")
        #ax1.plot([min(-1, min(self._data.keys())), max(1, max(self._data.keys()))], [0, 0], color="black")
        ax1.set_title("Abs")

        ax2.vlines(self._data.keys(), 0, [numpy.angle(v) for v in self._data.values()], color="black")
        #ax2.plot(self._data.keys(), [numpy.angle(v) for v in self._data.values()], 'o', color="black")
        #ax2.plot([min(-1, min(self._data.keys())), max(1, max(self._data.keys()))], [0, 0], color="black")
        ax2.set_ylim((-numpy.pi*1.05, numpy.pi*1.05))
        ax2.set_title("Phase")
        
        fig.canvas.draw()
        

    def plot_fourier(self, type="polar"):
        xlim = (-10, 10)
        x_axis = numpy.linspace(xlim[0], xlim[1], 1000)

        ft = numpy.zeros(len(x_axis), dtype="complex128")
        for x, v in self._data.items():
            ft += v*numpy.exp(2.j*numpy.pi*x*x_axis)

        if type == "polar":
            fig = matplotlib.pyplot.figure(figsize=(14, 7))
            fig.clear()
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.plot(x_axis, abs(ft), color="black")
            ax1.set_title("Abs")

            ax2.plot(x_axis, numpy.angle(ft), color="black")
            ax2.set_ylim((-numpy.pi*1.05, numpy.pi*1.05))
            ax2.set_title("Phase")
        elif type == "realimag":
            fig = matplotlib.pyplot.figure(figsize=(14, 7))
            fig.clear()
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.plot(x_axis, numpy.real(ft), color="black")
            ax1.set_title("Real")

            ax2.plot(x_axis, numpy.imag(ft), color="black")
            if abs(numpy.imag(ft)).max() < 1e-2:
                ax2.set_ylim((-1e-2, 1e-2))
                
            ax2.set_title("Imag")
            
        
        fig.canvas.draw()
        
