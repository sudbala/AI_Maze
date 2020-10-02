from Maze import Maze
from time import sleep


class SensorlessProblem:

    # Constructor that sets up all the possible states that the robot can be in. Obviously cannot be in the walls,
    # so just check if it is a floor.
    def __init__(self, maze):
        self.maze = maze
        initial_state = []
        # The starting state will literally be all the possible states that you can be on. Loop through the width and
        # the height of the maze, check if a floor, and add the x and y to the list.
        for robot_x in range(maze.width):
            for robot_y in range(maze.height):
                if maze.is_floor(robot_x, robot_y):
                    initial_state.append(robot_x)
                    initial_state.append(robot_y)
        # Now set the start_state for the robots, "tuplify" it
        self.start_state = tuple(initial_state)

    # Get successors moves the robots in the initial state up, left, right and down. We check if the new position of the
    # robot is valid, for if it is not, then we narrow where our belief states are. There will be 4 successors, one for
    # each directions
    def get_successors(self, state):
        # Sets the number of robots in our state
        num_robots = int(len(state)/2)
        # Create a successor_list to add our successors to
        successor_list = []

        # All the possible directions we can go. This makes it easier to loop through
        position_changes = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for move in position_changes:
            # For the current successor state being built up
            successor = []

            # Needed so we don't add the same robot belief location
            in_successor = set()

            # Loop through each robot, add new locations if not already in successor. This is precisely the way our
            # tuple will grow shorter. There will be a high chance that one robot will move to a location where another
            # robot already exists, which means, beliefs decrease
            for robot_belief in range(num_robots):
                # Grab the locations of the robot_belief, we will possibly be editing it
                next_belief_x = state[robot_belief * 2]
                next_belief_y = state[robot_belief * 2 + 1]

                # Check if the new location will be a wall or edge. If it is, then don't change. If not, then change!
                if self.maze.is_floor(next_belief_x + move[0], next_belief_y + move[1]):
                    next_belief_x += move[0]
                    next_belief_y += move[1]

                # Our next belief
                next_belief = (next_belief_x, next_belief_y)

                # Lastly, check if our new belief is already a belief. If not, add it to our beliefs and succesor state
                if next_belief not in in_successor:
                    in_successor.add(next_belief)
                    successor.append(next_belief_x)
                    successor.append(next_belief_y)

            # After this one move, add the successor to the successor_list if len is greater than 0 (we have a state)
            if len(successor) != 0:
                successor_list.append(tuple(successor))

        # After all moves, return our successor list
        return successor_list

    # A* needs a is_goal function to check when to stop. In this case, we need a singular robot, or a state that has
    # just an x and y.
    def is_goal(self, state):
        return len(state) == 2

    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
