from Maze import Maze
from SensorlessProblem import SensorlessProblem

from astar_search import astar_search


def null_heuristic(state):
    return 0


# Test problems
# test_maze = Maze("maze1.maz")
# test_mp = SensorlessProblem(test_maze)
# print(test_mp.start_state)
# print(test_mp.get_successors(test_mp.start_state))
# #
# result = astar_search(test_mp, null_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# test_maze2 = Maze("maze2.maz")
# test_mp = SensorlessProblem(test_maze2)
# print(test_mp.start_state)
# print(test_mp.get_successors(test_mp.start_state))
# #
# result = astar_search(test_mp, null_heuristic)
# print(result)
# test_mp.animate_path(result.path)

test_maze3 = Maze("maze3.maz")
test_mp = SensorlessProblem(test_maze3)
print(test_mp.start_state)
print(test_mp.get_successors(test_mp.start_state))
#
result = astar_search(test_mp, null_heuristic)
print(result)
test_mp.animate_path(result.path)

# test_maze4 = Maze("maze4.maz")
# test_mp = SensorlessProblem(test_maze4)
# print(test_mp.start_state)
# print(test_mp.get_successors(test_mp.start_state))
# #
# result = astar_search(test_mp, null_heuristic)
# print(result)
# test_mp.animate_path(result.path)


# test_maze5 = Maze("maze5.maz")
# test_mp = SensorlessProblem(test_maze5)
# print(test_mp.start_state)
# print(test_mp.get_successors(test_mp.start_state))
# #
# result = astar_search(test_mp, null_heuristic)
# print(result)
# test_mp.animate_path(result.path)
