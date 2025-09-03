import matplotlib.pyplot
import numpy

def phasor(amplitude, phase):
    return amplitude*numpy.exp(1.j*phase)

class PhasorPlotter:
    def __init__(self):
        self.setup_window()
        
    def clear(self):
        self.setup_window()
    
    def setup_window(self):
        self.fig = matplotlib.pyplot.figure("PhasePlotter", figsize=(14, 7))
        self.fig.clear()
        self.ax1 = self.fig.add_subplot(121)
        self.ax1.spines["left"].set_position(("data", 0))
        self.ax1.spines["bottom"].set_position(("data", 0))
        self.ax1.spines["right"].set_color("none")
        self.ax1.spines["top"].set_color("none")
        self.ax1.set_xlim((-1, 1))
        self.ax1.set_ylim((-1, 1))
        self._ax1_lim = 1
        self.ax1.set_aspect("equal")
        
        self.ax2 = self.fig.add_subplot(122)
        self.ax2.spines["bottom"].set_position(("data", 0))
        self.ax2.spines["top"].set_color("none")
        self.ax2.set_xticks((-3*numpy.pi, -2*numpy.pi, -1*numpy.pi, 0, 1*numpy.pi, 2*numpy.pi, 3*numpy.pi))
        self.ax2.set_xticklabels((r"$-3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$"))
        self.fig.canvas.draw()
               
    def add_wave(self, wave, color="black"):
        self.ax1.plot([0, numpy.real(wave)], [0, numpy.imag(wave)], ':', color=color)
        self.ax1.plot([numpy.real(wave)], [numpy.imag(wave)], 'o', color=color)
        if abs(wave) > self._ax1_lim:
            self._ax1_lim = abs(wave)*1.05
            self.ax1.set_xlim((-self._ax1_lim, self._ax1_lim))
            self.ax1.set_ylim((-self._ax1_lim, self._ax1_lim))
        
        x = numpy.arange(-10, 10, 0.1)
        if (abs(wave) > 1e-15).sum() == 0:
            self.ax2.plot(x, numpy.zeros(x.shape), color=color)
        else:
            self.ax2.plot(x, abs(wave)*numpy.sin(x-numpy.angle(wave)), color=color)
        
        self.fig.canvas.draw()
