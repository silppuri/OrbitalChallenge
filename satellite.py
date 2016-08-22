from math import sin, cos, sqrt

class Satellite:
    def __init__(self, data):
        self.name = data["name"]
        self.neighbours = []

        self.position = data["position"]
        self.coordinates = self.cartesian_coordinates()
        print self.position
        print self.coordinates

    def build_neighbours(self, other_satellites):
        for satellite in other_satellites:
            if self.sees_other(satellite):
                self.neighbours.append((self.distance_to(satellite), satellite))

    def distance_to(self, satellite):
        return sqrt(0)

    def sees_other(self, satellite):
        return True

    def cartesian_coordinates(self):
        lat, lon, height = self.position
        x = height * cos(lat) * cos(lon)
        y = height * cos(lat) * sin(lon)
        z = height * sin(lat)
        return (x, y, z)
