from math import sin, cos, sqrt

EARTH_RADIUS = 6371.0

class Point:
    def __init__(self, data):
        self.name = data["name"]
        self.neighbours = []

        self.position = data["position"]
        self.coordinates = self.cartesian_coordinates()

    def build_neighbours(self, other_points):
        for point in other_points:
            if self.sees_other(point):
                self.neighbours.append((self.distance_to(point), point.name, point))

    def distance_to(self, other):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 -z1, 2))


    def sees_other(self, other):
        #http://paulbourke.net/geometry/circlesphere/index.html#linesphere
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        a = pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2)
        b = 2 * ((x2 - x1) * x1 + (y2 - y1) * y1 + (z2 - z1) * z1)
        c = pow(x1, 2) + pow(y1, 2) + pow(z1, 2) - pow(EARTH_RADIUS, 2)
        discriminant = pow(b, 2) - 4 * a * c
        return discriminant <= 0

    def cartesian_coordinates(self):
        lat, lon, height = self.position
        x = height * cos(lat) * cos(lon)
        y = height * cos(lat) * sin(lon)
        z = height * sin(lat)
        return (x, y, z)
