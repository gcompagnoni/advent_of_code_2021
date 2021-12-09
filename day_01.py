with open("Inputs/input_01.txt", "r") as infile:
    depths = [int(x) for x in infile.readlines()]

diffs = [(depths[i + 1] - depths[i]) for i in range(len(depths) - 1)]
increases = [x for x in diffs if x > 0]

print("Answer to the first part: \n", len(increases))

# Note that comparing A+B+C with B+C+D is the same as comparing A and D
diffs_3 = [(depths[i + 3] - depths[i]) for i in range(len(depths) - 3)]
increases_3 = [x for x in diffs_3 if x > 0]
print("Answer to the second part: \n", len(increases_3))
