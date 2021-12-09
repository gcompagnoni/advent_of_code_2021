with open("Inputs/input_02.txt", "r") as infile:
    commands = [(lambda c: (c[0], int(c[1])))(x.split()) for x in infile.readlines()]

pos = sum([c[1] for c in commands if c[0] == "forward"])
# we assume all instructions are valid i.e. they would never cause depth to become negative
depth = sum([c[1] for c in commands if c[0] == "down"]) - sum([c[1] for c in commands if c[0] == "up"])

print("Answer to the first part: \n", pos * depth)

import numpy as np

aim = np.cumsum([0 if c[0] == "forward" else c[1] if c[0] == "down" else -c[1] for c in commands])
forward_orders = np.array([c[1] if c[0] == "forward" else 0 for c in commands])
new_depth = (forward_orders * aim).sum()
# computation for horizontal position pos has not changed

print("Answer to the second part: \n", pos * new_depth)
