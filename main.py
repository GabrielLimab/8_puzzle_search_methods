import time
import unittest

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class Node:
    def __init__(self, state, parent, move, cost=1, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        self.cost = cost
        self.heuristic = heuristic

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))
    
class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

class Heap:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def heappush(self, item):
        self.items.append(item)
        if self.algorithm == 'U':
            self.items.sort(key=lambda x: x.cost)
        elif self.algorithm == 'A':
            self.items.sort(key=lambda x: x.cost + x.heuristic)
        elif self.algorithm == 'G':
            self.items.sort(key=lambda x: x.heuristic)
        else:
            self.items.sort(key=lambda x: x.depth)
    def heappop(self):
        return self.items.pop(0)

def bfs(start_state):
    iteracoes = 0
    q = Queue()
    visited = set()

    start_node = Node(start_state, None, None)
    q.put(start_node)
    visited.add(start_node)

    while not q.empty():
        node = q.get()

        if node.state == goal_state:
            moves = []
            while node.parent is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves

        zero_index = node.state.index(0)
        row = zero_index // 3
        col = zero_index % 3

        if row > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Up')
            if new_node not in visited:
                q.put(new_node)
                visited.add(new_node)

        if row < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Down')
            if new_node not in visited:
                q.put(new_node)
                visited.add(new_node)

        if col > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Left')
            if new_node not in visited:
                q.put(new_node)
                visited.add(new_node)

        if col < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Right')
            if new_node not in visited:
                q.put(new_node)
                visited.add(new_node)

    return None

def iterative_deepening_search(start_state):
    depth = 0
    while True:
        result = depth_limited_search(start_state, depth)
        if result != 'cutoff':
            return result
        depth += 1

def depth_limited_search(start_state, depth_limit):
    iteracoes = 0
    q = Queue()
    visited = set()

    start_node = Node(start_state, None, None)
    q.put(start_node)
    visited.add(start_node)

    while not q.empty():
        node = q.get()

        if node.state == goal_state:
            moves = []
            while node.parent is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves

        if node.depth < depth_limit:
            zero_index = node.state.index(0)
            row = zero_index // 3
            col = zero_index % 3

            if row > 0:
                new_state = node.state[:]
                new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
                new_node = Node(new_state, node, 'Up')
                if new_node not in visited:
                    q.put(new_node)
                    visited.add(new_node)

            if row < 2:
                new_state = node.state[:]
                new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
                new_node = Node(new_state, node, 'Down')
                if new_node not in visited:
                    q.put(new_node)
                    visited.add(new_node)

            if col > 0:
                new_state = node.state[:]
                new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
                new_node = Node(new_state, node, 'Left')
                if new_node not in visited:
                    q.put(new_node)
                    visited.add(new_node)

            if col < 2:
                new_state = node.state[:]
                new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
                new_node = Node(new_state, node, 'Right')
                if new_node not in visited:
                    q.put(new_node)
                    visited.add(new_node)

    return 'cutoff'

def uniform_cost_search(start_state):
    iteracoes = 0
    start_node = Node(start_state, None, None, 0)
    q = Heap('U')
    q.heappush(start_node)
    visited = set()
    visited.add(start_node)

    while not q.empty():
        node = q.heappop()

        if node.state == goal_state:
            moves = []
            while node.parent is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves
        
        zero_index = node.state.index(0)
        row = zero_index // 3
        col = zero_index % 3

        if row > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Up', node.cost + 1)
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if row < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Down', node.cost + 1)
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if col > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Left', node.cost + 1)
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if col < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Right', node.cost + 1)
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

    return None

def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            distance += abs(i // 3 - (state[i] - 1) // 3) + abs(i % 3 - (state[i] - 1) % 3)
    return distance

def a_star(start_state):
    iteracoes = 0
    start_node = Node(start_state, None, None, 0, manhattan_distance(start_state))
    q = Heap('A')
    q.heappush(start_node)
    visited = set()
    visited.add(start_node)

    while not q.empty():
        node = q.heappop()

        if node.state == goal_state:
            moves = []
            while node.parent is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves
        
        zero_index = node.state.index(0)
        row = zero_index // 3
        col = zero_index % 3

        if row > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Up', node.cost + 1, manhattan_distance(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if row < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Down', node.cost + 1, manhattan_distance(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if col > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Left', node.cost + 1, manhattan_distance(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if col < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Right', node.cost + 1, manhattan_distance(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

    return None

def misplaced_tiles(state):
    misplaced = 0
    for i in range(9):
        if state[i] != goal_state[i]:
            misplaced += 1
    return misplaced

def greedy_best_first_search(start_state):
    start_node = Node(start_state, None, None, 0, misplaced_tiles(start_state))
    q = Heap('G')
    q.heappush(start_node)
    visited = set()
    visited.add(start_node)

    while not q.empty():
        node = q.heappop()

        if node.state == goal_state:
            moves = []
            while node.parent is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves
        
        zero_index = node.state.index(0)
        row = zero_index // 3
        col = zero_index % 3

        if row > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Up', node.cost + 1, misplaced_tiles(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if row < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            new_node = Node(new_state, node, 'Down', node.cost + 1, misplaced_tiles(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if col > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Left', node.cost + 1, misplaced_tiles(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

        if col < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            new_node = Node(new_state, node, 'Right', node.cost + 1, misplaced_tiles(new_state))
            if new_node not in visited:
                q.heappush(new_node)
                visited.add(new_node)

    return None

def hill_climbing(start_state):
    iteracoes = 0
    k = 5
    start_node = Node(start_state, None, None, 0, manhattan_distance(start_state))
    q = Heap('G')
    q.heappush(start_node)
    visited = set()
    visited.add(start_node)

    while not q.empty():
        node = q.heappop()

        if node.state == goal_state:
            moves = []
            while node.parent is not None:
                moves.append(node.move)
                node = node.parent
            moves.reverse()
            return moves
        
        zero_index = node.state.index(0)
        row = zero_index // 3
        col = zero_index % 3

        if row > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            if manhattan_distance(new_state) < manhattan_distance(node.state):
                new_node = Node(new_state, node, 'Up', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            elif manhattan_distance(new_state) == manhattan_distance(node.state) and k > 0:
                k -= 1
                new_node = Node(new_state, node, 'Up', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            else:
                k = 5
                new_node = Node(new_state, node, 'Up', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)

        if row < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            if manhattan_distance(new_state) < manhattan_distance(node.state):
                new_node = Node(new_state, node, 'Down', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            elif manhattan_distance(new_state) == manhattan_distance(node.state) and k > 0:
                k -= 1
                new_node = Node(new_state, node, 'Down', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            else:
                k = 5
                new_node = Node(new_state, node, 'Down', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            

        if col > 0:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            if manhattan_distance(new_state) < manhattan_distance(node.state):
                new_node = Node(new_state, node, 'Left', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            elif manhattan_distance(new_state) == manhattan_distance(node.state) and k > 0:
                k -= 1
                new_node = Node(new_state, node, 'Left', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            else:
                k = 5
                new_node = Node(new_state, node, 'Left', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)

        if col < 2:
            new_state = node.state[:]
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            if manhattan_distance(new_state) < manhattan_distance(node.state):
                new_node = Node(new_state, node, 'Right', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            elif manhattan_distance(new_state) == manhattan_distance(node.state) and k > 0:
                k -= 1
                new_node = Node(new_state, node, 'Right', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)
            else:
                k = 5
                new_node = Node(new_state, node, 'Right', node.cost + 1, manhattan_distance(new_state))
                if new_node not in visited:
                    q.heappush(new_node)
                    visited.add(new_node)

    return None

def print_state(state):
    for i in range(0, 9, 3):
        if state[i] == 0:
            print(' ', end=' ')
            print(state[i + 1], end=' ')
            print(state[i + 2])
        elif state[i + 1] == 0:
            print(state[i], end=' ')
            print(' ', end=' ')
            print(state[i + 2])
        elif state[i + 2] == 0:
            print(state[i], end=' ')
            print(state[i + 1], end=' ')
            print(' ')
        else:
            print(state[i], end=' ')
            print(state[i + 1], end=' ')
            print(state[i + 2])
    print()

# get the algorithm from command line argument, the start state and if PRINT is set to true, print the solution
def main():
    import sys
    algorithm = sys.argv[1]
    start_state = [0] * 9
    for i in range(2,11):
        start_state[i-2] = int(sys.argv[i])
    # maybe there wont be a print argument
    PRINT = False
    if len(sys.argv) > 11:
        PRINT = sys.argv[11] == 'PRINT'
    if algorithm == 'B':
        moves = bfs(start_state)
    elif algorithm == 'U':
        moves = uniform_cost_search(start_state)
    elif algorithm == 'I':
        moves = iterative_deepening_search(start_state)
    elif algorithm == 'A':
        moves = a_star(start_state)
    elif algorithm == 'G':
        moves = greedy_best_first_search(start_state)
    elif algorithm == 'H':
        moves = hill_climbing(start_state)
    else:
        print("Unknown algorithm:", algorithm)
        return

    if moves is None:
        print("No solution found.")
        return

    if PRINT:
        # print all moves until solution
        state = start_state[:]
        print(len(moves))
        print()
        print_state(state)

        for move in moves:
            if move == 'Up':
                zero_index = state.index(0)
                state[zero_index], state[zero_index - 3] = state[zero_index - 3], state[zero_index]
            elif move == 'Down':
                zero_index = state.index(0)
                state[zero_index], state[zero_index + 3] = state[zero_index + 3], state[zero_index]
            elif move == 'Left':
                zero_index = state.index(0)
                state[zero_index], state[zero_index - 1] = state[zero_index - 1], state[zero_index]
            elif move == 'Right':
                zero_index = state.index(0)
                state[zero_index], state[zero_index + 1] = state[zero_index + 1], state[zero_index]
            print_state(state)
    else:
        print(len(moves))

    return

if __name__ == '__main__':
    main()