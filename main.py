from geopy.distance import great_circle

from satellite import Satellite
from plotter import Plotter

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

#Plotter(satellites).plot()
