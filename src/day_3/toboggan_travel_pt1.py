def get_n_trees(forest_file):
    """
    This function will read in the file and check for tree vs open for each visited cell
    If it is a tree it will add to the running total of visited trees
    If it is open it will move on
    The movement pattern is to go three to the right each line in a wrapped fashion (modulus)
    """
    n_trees = 0
    col = 0
    with open(forest_file) as forest:
        for level in forest:
            if level[col] == "#":
                n_trees += 1
            col = (col + 3) % (len(level) -1)
    return n_trees

print(get_n_trees("example.txt"))
print(get_n_trees("forest_path.txt"))
