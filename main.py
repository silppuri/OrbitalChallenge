from geopy.distance import great_circle

from point import Point
from plotter import Plotter
from priority_queue import PriorityQueue

EARTH_RADIUS = 6371.0

data = open('positions.dat')
rows = data.read().split('\n')
route_data = rows[-2].split(',')
seed = float(rows[0].split(' ')[-1])

start = Point({
    "name": "START",
    "position": (float(route_data[1]), float(route_data[2]), EARTH_RADIUS)
})
end = Point({
    "name": "END",
    "position": (float(route_data[3]), float(route_data[4]), EARTH_RADIUS)
})

start_satellite = None
goal_satellite = None
start_distance = float('inf')
end_distance = float('inf')
satellites = []
for line in rows[1:-2]:
    satellite_data = line.strip().split(',')
    satellite = {
        "name": satellite_data[0],
        "position": (float(satellite_data[1]), float(satellite_data[2]), EARTH_RADIUS + float(satellite_data[3]))
    }
    satellites.append(Point(satellite))

for satellite in satellites:
    other_satellites = satellites[:]
    other_satellites.remove(satellite)
    satellite.build_neighbours(other_satellites)

    # Find the start and end satellites
    if len(satellite.neighbours) == 0: continue
    new_start_distance = start.distance_to(satellite)
    new_end_distance = end.distance_to(satellite)
    if new_start_distance < start_distance:
        start_satellite = satellite
        start_distance = new_start_distance
    if new_end_distance < end_distance:
        end_satellite = satellite
        end_distance = new_end_distance

# Find route

def heuristic(point):
    return point.distance_to(end_satellite)

def astar():
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def apply_heuristic(item):
        (cost, _, point) = item
        return heuristic(point) + cost

    queue = PriorityQueue(apply_heuristic)
    return astar_traverse(start_satellite, queue, end_satellite)

def astar_traverse(start, nodes, goal):
    visited = set()
    start = (0, [start.name], start)
    nodes.push(start)

    while not nodes.is_empty():
        (cost, actions, node) = nodes.pop()
        if node in visited: continue
        visited.add(node)

        if node == end_satellite:
            return actions

        for next in node.neighbours:
            (successor_cost, name, point) = next
            if not next in visited:
                next_cost = cost + successor_cost
                nodes.push((next_cost, actions + [name], point))

print "seed ", seed
print "satellites count ", len(satellites)
print "Start satellite: ", start_satellite.name
print "End satellite: ", end_satellite.name
steps = astar()
print "Route ", steps

Plotter(start, satellites, end).plot()

