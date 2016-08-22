import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

EARTH_RADIUS = 6371.0

class Plotter:
    def __init__(self, satellites):
        self.satellites = satellites

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        self.ax = ax

    def plot(self):
        self.plot_earth()
        self.plot_satellites()
        plt.show()

    def plot_earth(self):
        # Create a sphere
        r = EARTH_RADIUS
        pi = np.pi
        cos = np.cos
        sin = np.sin
        phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
        x = r*sin(phi)*cos(theta)
        y = r*sin(phi)*sin(theta)
        z = r*cos(phi)

        self.ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='c', alpha=0.3, linewidth=0)

    def plot_satellites(self):
        for satellite in self.satellites:
            x, y, z = satellite.coordinates
            self.ax.scatter(x, y, z, c='r', marker='o')
