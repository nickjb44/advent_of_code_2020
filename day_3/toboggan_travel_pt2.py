import math

def get_n_trees(forest_file,right, down):
    """
    This function will read in the file and check for tree vs open for each visited cell
    If it is a tree it will add to the running total of visited trees
    If it is open it will move on
    It takes in a custom right and left parameter to determine movements
    """
    n_trees = 0
    col = 0
    with open(forest_file) as forest:
        for i, level in enumerate(forest):
            if (i % down) == 0:
                if level[col] == "#":
                    n_trees += 1
                col = (col + right) % (len(level) -1)
    return n_trees

def get_product_of_trees(file, movement_instructions):
    """
    this takes the path to a file and a list of dictionaries for right and down instructions
    """
    trees_found = [get_n_trees(file, movement_instruction["right"], movement_instruction["down"]) for movement_instruction in movement_instructions]
    return math.prod(trees_found)


movements = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2}
]


print(get_product_of_trees("example.txt", movements))
print(get_product_of_trees("forest_path.txt", movements))
