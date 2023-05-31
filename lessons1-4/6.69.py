def cut_rectangle(height, width):
    squares = []
    while height != 0 and width != 0:
        square_side = min(height, width)
        squares.append(square_side)
        height, width = max(height, width) - square_side, square_side
    return squares

assert cut_rectangle(425, 131) == [131, 131, 131, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]