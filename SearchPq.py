# CS76 Problem Assignment 2 10/1/2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaborators: Discussed strategies with James Fleming, Mack Reiferson

# Import statements
from heapq import heappush, heappop


# This class wraps up an array as a priority queue using the heapq implementation of priority queues. It has a
# constructor, add, remove, pop, contains, and length as useful functions for the
class SearchPq:

    # Constructor for my custom queue. Will have a pq and a entry_finder dictionary
    def __init__(self):
        self.pq = []
        self.dictionary = {}

    # Adds to our pq
    def add(self, node):
        # Adds a new task or updates based on priority and if we find a better cost
        if node.state in self.dictionary:
            if node.priority() <= (self.dictionary[node.state])[0]:
                self.remove(node.state)
        entry = [node.priority(), node, "present"]
        self.dictionary[node.state] = entry
        heappush(self.pq, entry)

    # Uses the dictionary to mark a state as removed or none.
    def remove(self, state):
        # Mark an existing task as removed
        entry = self.dictionary.pop(state)
        entry[-1] = None

    def pop(self):
        # Remove and return lowest priority node. Check if not removed first!
        while self.pq:
            priority, node, present = heappop(self.pq)
            if present is not None and node.state in self.dictionary:
                del self.dictionary[node.state]
                return node

    def contains(self, node):
        # checks if something is in the frontier
        return node.state in self.dictionary

    def length(self):
        return len(self.pq)
