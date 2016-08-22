import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from satellite import Satellite
from geopy.distance import great_circle

EARTH_RADIUS = 6371.0

data = open('positions.dat')
rows = data.read().split('\n')
route_data = rows[-2].split(',')
seed = float(rows[0].split(' ')[-1])

start = (route_data[1], route_data[2])
end =  (route_data[3], route_data[4])
distance = great_circle(start, end)

satellites = []
for line in rows[1:-2]:
    satellite_data = line.strip().split(',')
    satellite = {
        "name": satellite_data[0],
        "position": (float(satellite_data[1]), float(satellite_data[2]), EARTH_RADIUS + float(satellite_data[3]))
    }
    satellites.append(Satellite(satellite))

print "seed ", seed
print "distance ", distance
print "satellites count ", len(satellites)

for satellite in satellites:
    other_satellites = satellites[:]
    other_satellites.remove(satellite)
    satellite.build_neighbours(other_satellites)

# Create a sphere
r = EARTH_RADIUS
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(
    x, y, z,  rstride=1, cstride=1, color='c', alpha=0.3, linewidth=0)

n = 100
for satellite in satellites:
    x, y, z = satellite.coordinates
    ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
