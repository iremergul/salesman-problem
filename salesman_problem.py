# salesman problem
from itertools import permutations


def calculate_total_distance(route, distance_matrix):
    """
    Calculate the total distance of the given route based on the distance matrix.
    """
    total_distance = 0
    number_of_cities = len(route)

    for i in range(number_of_cities - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]

    total_distance += distance_matrix[route[-1]][route[0]]

    return total_distance


def traveling_salesman_problem(distance_matrix):
    """
    Solve the Traveling Salesman Problem using a brute-force approach.
    """
    number_of_cities = len(distance_matrix)
    cities = list(range(number_of_cities))

    all_possible_routes = permutations(cities)

    minimum_distance = float("inf")
    best_route = None

    for route in all_possible_routes:
        current_distance = calculate_total_distance(route, distance_matrix)

        if current_distance < minimum_distance:
            minimum_distance = current_distance
            best_route = route

    return best_route, minimum_distance


distance_matrix = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 19, 22, 33, 28],
    [15, 19, 0, 12, 35, 26],
    [20, 22, 12, 0, 5, 17],
    [25, 33, 35, 5, 0, 12],
    [30, 28, 26, 17, 12, 0],
]


best_route, minimum_distance = traveling_salesman_problem(distance_matrix)


city_names = ["A", "B", "C", "D", "E", "F"]
route_names = [city_names[i] for i in best_route] + [city_names[best_route[0]]]
print(f"The shortest route is: {' -> '.join(route_names)}")
print(f"The total distance is: {minimum_distance}")
