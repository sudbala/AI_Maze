from SearchSolution import SearchSolution
from SearchPq import SearchPq


class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # Set up all the Node internal variables
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        return self.heuristic + self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # Get started with our starting node and our frontier, which in this case is a priority queue
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pq = SearchPq()

    # add start node to the pq
    pq.add(start_node)
    visited = set()

    # start our solution, the path of which is our explored set
    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    # keep track of visited costs.
    visited_cost = {start_node.state: 0}

    while pq.length() != 0:
        node = pq.pop()
        solution.nodes_visited += 1

        # Check if a goal state
        if search_problem.is_goal(node.state):
            solution.path = backchain(node)
            solution.cost = node.transition_cost
            return solution
        # add to the path if not goal
        visited.add(node.state)

        # Now for each successor, calc the cost, add it to the queue
        for successor in search_problem.get_successors(node.state):
            if successor[1:] == node.state[1:]:
                visited_cost[successor] = visited_cost[node.state]
            else:
                visited_cost[successor] = visited_cost[node.state] + 1
            successor_node = AstarNode(successor, heuristic_fn(successor), node, visited_cost[successor])

            # Check if in the path or in our queue
            if successor not in visited and not pq.contains(successor_node):
                pq.add(successor_node)
            elif pq.contains(successor_node):
                pq.add(successor_node)
    return solution

