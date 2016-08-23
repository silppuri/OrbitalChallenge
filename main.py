from point import Point
from priority_queue import PriorityQueue

data = open('positions.dat')
rows = data.read().split('\n')
route_data = rows[-2].split(',')
seed = float(rows[0].split(' ')[-1])

start_point = Point(("START", float(route_data[1]), float(route_data[2]), 0))
end_point = Point(("END", float(route_data[3]), float(route_data[4]), 0))
satellites = []
for line in rows[1:-2]:
    satellite_data = line.strip().split(',')
    satellites.append(Point(satellite_data))

def closest(point):
    closest_d = float('inf')
    for satellite in satellites:
        distance = point.distance_to(satellite)
        if distance < closest_d:
            closest = satellite
            closest_d = distance
    return closest

def uniform_cost_search():
    queue = PriorityQueue()
    start = closest(start_point)
    end = closest(end_point)
    return ucs_traverse(start, queue, end)

def ucs_traverse(start, nodes, goal):
    visited = set()
    start = (0, [start.name], start)
    nodes.push(start)

    while not nodes.is_empty():
        (cost, actions, node) = nodes.pop()
        if node in visited: continue
        visited.add(node)

        if node == goal:
            return actions

        for next in node.neighbours(satellites):
            (neighbour_cost, name, point) = next
            if not next in visited:
                next_cost = cost + neighbour_cost
                nodes.push((next_cost, actions + [name], point))

print uniform_cost_search()
