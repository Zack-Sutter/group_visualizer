

def compute_next(prev_row: list, window_size, rules: dict) -> list:
    # compute next row according to rules
    next_row = []
    for i in range(0, len(prev_row)+1-window_size):
        slice = prev_row[i:i+window_size]
        next_row += rules[tuple(slice)]
    return next_row

def generate_image(matrix, color_map):
    for row in matrix:
        row_string = ''
        for dig in row:
            row_string += color_map[dig]

        print(row_string)
    return

def propagate(seed: list, rules: dict, num_iters = 10):
    # create the matrix by iteratively applying the rules to each row.
    matrix = [seed]
    window_size = len(next(iter(rules)))
    for i in range(num_iters):
        next_row = compute_next(matrix[i], window_size, rules)
        if not next_row:
            # not enough elements to apply a rule on: END
            break
        matrix.append(next_row)
    return matrix

# example set
binary_set = {
        "rules":{
        (0,0,0): [0],
        (0,0,1): [0],
        (0,1,0): [0],
        (0,1,1): [1],
        (1,0,0): [1,0],
        (1,0,1): [1,0],
        (1,1,0): [1,1],
        (1,1,1): [0,1]
    },
    "seed": [0,0,1,0,0,1,1,1],
    "color_map": {
        0: "🟥",
        1: "🟩"
    }
}


bin_matrix = propagate(binary_set["seed"], binary_set["rules"], num_iters = 30)
generate_image(bin_matrix, binary_set["color_map"])