

def compute_next(prev_row: list, window_size: int, rules: dict = {"key":"value"}) -> list:
    next_row = []
    for i in range(0, len(prev_row)+1-window_size):
        slice = prev_row[i:i+window_size]
        next_row += rules[tuple(slice)]
    return next_row

rules = {
    (0,0,0): [0],
    (0,0,1): [0],
    (0,1,0): [0],
    (0,1,1): [1],
    (1,0,0): [1,0],
    (1,0,1): [1,0],
    (1,1,0): [1,1],
    (1,1,1): [0,1]
}

seed = [0,0,1,0,0,1,1,0,1,1]

red = "🟥"
green = "🟩"

my_rows = []
my_rows.append(seed)
for i in range(30):
    my_rows.append(compute_next(my_rows[i], window_size = 3, rules = rules))

for row in my_rows:
    row_string = ''
    for dig in row:
        if dig == 0:
            row_string += red
        else:
            row_string += green

    print(row_string)