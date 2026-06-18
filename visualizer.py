from collections.abc import Callable

from PIL import Image


class GroupVisualizer:
    def __init__(
        self,
        rules: dict[tuple, list],
        seed_fn: Callable[[int], int],
        color_map: dict[int, tuple[int, int, int]],
        padding_color: tuple[int, int, int] = (0, 0, 0),
    ):
        self.rules = rules
        self.seed_fn = seed_fn
        self.color_map = color_map
        self.padding_color = padding_color
        self._window_size = len(next(iter(rules)))

    def _compute_next(self, prev_row: list) -> list:
        next_row = []
        for i in range(len(prev_row) + 1 - self._window_size):
            window = prev_row[i : i + self._window_size]
            next_row += self.rules[tuple(window)]
        return next_row

    def _propagate(self, seed: list, num_iters: int) -> list[list]:
        matrix = [seed]
        for i in range(num_iters):
            next_row = self._compute_next(matrix[i])
            if not next_row:
                break
            matrix.append(next_row)
        return matrix

    def _build_seed(self, width: int, height: int) -> list:
        seed_length = width + 2 * height - 2
        return [self.seed_fn(i) for i in range(-seed_length // 2, seed_length // 2)]

    def generate(self, width: int, height: int) -> Image.Image:
        """
        Generate a cellular automata image.
        
        Args:
            width: The width of the image (pixels).
            height: The height of the image (pixels).
        Returns:
            An image of the cellular automata (PIL.Image.Image).
        """
        seed = self._build_seed(width, height)
        matrix = self._propagate(seed, height - 1)
        return self._render(matrix, width, height)

    def _render(self, matrix: list[list], width: int, height: int) -> Image.Image:
        if not matrix:
            return Image.new("RGB", (width, height), self.padding_color)

        full_width = max(i + len(row) for i, row in enumerate(matrix))
        x_start = (full_width - width) // 2

        img = Image.new("RGB", (width, height), self.padding_color)
        pixels = img.load()

        for y in range(height):
            if y >= len(matrix):
                break
            row = matrix[y]
            for x in range(width):
                logical_x = x_start + x
                j = logical_x - y
                if 0 <= j < len(row):
                    pixels[x, y] = self.color_map[row[j]]

        return img
