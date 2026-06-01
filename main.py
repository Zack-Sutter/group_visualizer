

def compute_next(prev_row: list, window_size: int, rules: dict = {"key":"value"}) -> list:
    next_row = []
    for i in range(0, len(prev_row)+1-window_size):
        slice = prev_row[i:i+window_size]
        next_row += slice
    return next_row


seed = [1,2,3,4,5,2]

my_rows = []
my_rows.append(seed)
for i in range(2):
    my_rows.append(compute_next(my_rows[i], 3))

for row in my_rows:
    print(row)