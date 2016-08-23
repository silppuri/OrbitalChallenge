from math import sin, cos, sqrt, pi

EARTH_RADIUS = 6371.0

class Point:
    def __init__(self, data):
        self.name = data[0]
        self.coordinates = self.cartesian_coordinates(self.lat_lon_alt(data))

    def lat_lon_alt(self, data):
        return (float(data[1]), float(data[2]), float(data[3]))

    def neighbours(self, other_points):
        neighbours = []
        for point in other_points:
            if self.sees_other(point) and not point is self:
                neighbours.append((self.distance_to(point), point.name, point))
        return neighbours

    def distance_to(self, other):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 -z1, 2))

    def sees_other(self, other):
        #http://paulbourke.net/geometry/circlesphere/index.html#linesphere
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        dx = x2 -x1
        dy = y2 - y1
        dz = z2 - z1
        a = dx**2 + dy**2 + dz**2
        b = 2 * (dx * x1 + dy * y1 + dz * z1)
        c = x1**2 + y1**2 + z1**2 - EARTH_RADIUS**2
        discriminant = b**2 - 4 * a * c
        return discriminant < 0

    def cartesian_coordinates(self, lat_lon_alt):
        latitude, longitude, altitude = lat_lon_alt
        lat = latitude * pi / 180.0
        lon = longitude * pi / 180.0
        r = EARTH_RADIUS + altitude
        x = -r * cos(lat) * cos(lon)
        y =  r * sin(lat)
        z =  r * cos(lat) * sin(lon)
        return (x, y, z)
