from Maze import Maze
from time import sleep


class MazeworldProblem:

    # Constructor for hte MazeworldProblem Class
    def __init__(self, maze, goal_locations):
        # Set the constructor maze and goal locations\
        initial_state = list(maze.robotloc)
        initial_state.insert(0, 0)
        self.start_state = tuple(initial_state)
        self.maze = maze
        self.goal_locations = goal_locations

    # Returns the successors for the robot with current turn
    def get_successors(self, state):
        # Update the maze
        self.maze.robotloc = list(state[1:])

        # Grabs the current turn and uses number of robots to compute the next turn
        current_turn = state[0]
        num_robots = self.maze.get_num_robots()
        next_turn = int((current_turn + 1) % num_robots)

        # Readies up a list for successors
        successor_list = []

        # Now we make a state for the four cardinal directions. North, East, South, West. We first make it a list so we
        # can modify it, set the next turn, edit the x or y location, and then check if it is a safe tile to go to.
        state_left = list(state)
        state_left[0] = next_turn
        state_left[current_turn*2 + 1] -= 1
        if self.is_safe_tile(state_left[current_turn * 2 + 1], state_left[current_turn * 2 + 2]):
            successor_list.append(tuple(state_left))

        # Right successor
        state_right = list(state)
        state_right[0] = next_turn
        state_right[current_turn * 2 + 1] += 1
        if self.is_safe_tile(state_right[current_turn * 2 + 1], state_right[current_turn * 2 + 2]):
            successor_list.append(tuple(state_right))

        # North Successor
        state_up = list(state)
        state_up[0] = next_turn
        state_up[current_turn * 2 + 2] += 1
        if self.is_safe_tile(state_up[current_turn * 2 + 1], state_up[current_turn * 2 + 2]):
            successor_list.append(tuple(state_up))

        # South Successor
        state_down = list(state)
        state_down[0] = next_turn
        state_down[current_turn * 2 + 2] -= 1
        if self.is_safe_tile(state_down[current_turn * 2 + 1], state_down[current_turn * 2 + 2]):
            successor_list.append(tuple(state_down))

        # Pass Successor
        state_pass = list(state)
        state_pass[0] = next_turn
        if self.maze.get_num_robots() > 1:
            successor_list.append(tuple(state_pass))

        return successor_list

    # Checks if the tile we are moving to is a safe tile.
    def is_safe_tile(self, x, y):

        # Check if wall/edge
        if self.maze.is_floor(x, y):
            # Now check if robot is not colliding with another robot
            if not self.maze.has_robot(x, y):
                return True
        return False

    # Checks if the current state is the goal state
    def is_goal(self, state):
        # Grab the rest of the state besides the current turn indicator, which are current locations and compare with
        # goal state locations.
        goal_state_check = state[1:]
        return goal_state_check == self.goal_locations

    # Sets up the manhattan heuristic, which is just horizontal and vertical distance
    def manhattan_heuristic(self, state):
        # Start the heuristic at 0
        heuristic = 0
        # For each robot, add the x and y distances to the heuristic
        for robot in range(int(self.maze.get_num_robots())):
            # Add x and y
            heuristic += abs(self.goal_locations[robot*2] - state[robot * 2 + 1])
            heuristic += abs(self.goal_locations[robot*2 + 1] - state[robot * 2 + 2])
        # return the heuristic
        return heuristic

    def __str__(self):
        string = "Mazeworld problem: "
        return string

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
    print(test_mp.get_successors((1, 1, 0, 1, 2, 2, 1)))
    print(test_mp.get_successors((2, 1, 0, 1, 2, 2, 1)))
