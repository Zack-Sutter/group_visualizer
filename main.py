from visualizer import GroupVisualizer


def identity_seed(index):
    if index == 0:
        return 0
    return 1


binary_rules = {
    (0, 0, 0): [1],
    (0, 0, 1): [0],
    (0, 1, 0): [0],
    (0, 1, 1): [1],
    (1, 0, 0): [0],
    (1, 0, 1): [0],
    (1, 1, 0): [0],
    (1, 1, 1): [1],
}

color_map = {
    0: (0, 0, 0),
    1: (255, 255, 255),
}

# very pleasing example
chaos_vis = GroupVisualizer(binary_rules, identity_seed, color_map)
img = chaos_vis.generate(width=1000, height=800)
img.show()


# mod example

# def mod_2_seed(index):
#     return index % 2
#
# mod_rules = {
#     (0, 0, 0): [0],
#     (0, 0, 1): [0],
#     (0, 1, 0): [1],
#     (0, 1, 1): [0],
#     (1, 0, 0): [1],
#     (1, 0, 1): [0],
#     (1, 1, 0): [0],
#     (1, 1, 1): [0],
# }
# mod_vis = GroupVisualizer(mod_rules, mod_2_seed, color_map)
# img = mod_vis.generate(width=100, height=80)
# img.show()