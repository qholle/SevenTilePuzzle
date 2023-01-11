import heapq

# This function gets the manhattan distance between two states.
def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    distance = 0
    coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    for i in range (7):
        distance += abs(coordinates[i][0] - coordinates[from_state.index(to_state[i])][0]) + abs(coordinates[i][1] - coordinates[from_state.index(to_state[i])][1])

    return distance

# This function prints the successors of a given state.
def print_succ(state):
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))

# This function finds all of the potential successor states of a given state.
def get_succ(state):
    coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

    zero_coords = []
    adjacent_coords = []
    state_coords = []
    succ_states = []
    
    # getting coordinates of starting values
    for i in range (7):
        state_coords.append(coordinates[state.index(i+1)])

    # finding coordinates where zero is and determining adjacent coordinates
    for i in range (9):
        if state[i] == 0:
            zero_coords.append(coordinates[i])
            if coordinates[i][0] != 0:
                adjacent_coords.append([coordinates[i][0] - 1, coordinates[i][1]])
            if coordinates[i][0] != 2:
                adjacent_coords.append([coordinates[i][0] + 1, coordinates[i][1]])
            if coordinates[i][1] != 0:
                adjacent_coords.append([coordinates[i][0], coordinates[i][1] - 1])
            if coordinates[i][1] != 2:
                adjacent_coords.append([coordinates[i][0], coordinates[i][1] + 1])
            
            # finding successor states
            for each in adjacent_coords:
                    successor = state.copy()
                    if state_coords.count(each) != 0:
                        successor[successor.index(state_coords.index(each)+1)] = 0
                        successor[i] = state_coords.index(each)+1
                        succ_states.append(successor)
            adjacent_coords.clear()

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):

    pq = []
    visited = []
    visited_states = []
    max_length = 1
    g = 0
    h = get_manhattan_distance(state)
    cost = g + h
    parent_index = -1

    heapq.heappush(pq, (cost, state, (g, h, parent_index)))
    visited_element = heapq.heappop(pq)
    visited.append(visited_element)
    visited_states.append(visited_element[1])

    while state != goal_state:
        for each in get_succ(state):
            if each not in visited_states :
                g = visited_element[2][0] + 1
                h = get_manhattan_distance(each)
                cost = g + h
                parent_index = visited.index(visited_element)
                heapq.heappush(pq, (cost, each, (g, h, parent_index)))
        if len(pq) > max_length:
            max_length = len(pq)
        visited_element = heapq.heappop(pq)
        visited.append(visited_element)
        visited_states.append(visited_element[1])
        state = visited_element[1]

    # printing path
    path = []
    while visited_element[2][2] != -1:
        path.append(visited_element[1])
        visited_element = visited[visited_element[2][2]]
    
    path.append(visited_element[1])
    visited_element = visited[visited_element[2][2]]
    
    path.reverse()

    for each in path:
        print(each, "h={}".format(get_manhattan_distance(each)), "moves: {}".format(path.index(each)))
    print("Max queue length: {}".format(max_length))


# Project Demo
if __name__ == "__main__":

    print("Finding manhattan distance of various states:")
    print(get_manhattan_distance([2,5,1,4,3,6,7,0,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    print(get_manhattan_distance([2,0,1,4,5,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()
    
    print(get_manhattan_distance([2,5,1,0,4,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    print(get_manhattan_distance([2, 5, 1, 4, 0, 6, 0, 7, 3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    print(get_manhattan_distance([2, 5, 1, 4, 0, 6, 7, 3, 0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    print("Finding successors of various states:")
    print_succ([2, 5, 1, 4, 0, 6, 7, 0, 3])
    print()

    print_succ([3, 4, 6, 0, 0, 1, 7, 2, 5])
    print()

    print("Solving various boards:")
    solve([3, 4, 6, 0, 0, 1, 7, 2, 5])
    print()

    solve([6, 0, 0, 3, 5, 1, 7, 2, 4])
    print()
    
    solve([0, 4, 7, 1, 3, 0, 6, 2, 5])
    print()

    solve([5, 2, 3, 0, 6, 4, 7, 1, 0])
    print()

    solve([1, 7, 0, 6, 3, 2, 0, 4, 5])
    print()
    
    solve([1, 2, 3, 4, 5, 6, 7, 0, 0])
    print()