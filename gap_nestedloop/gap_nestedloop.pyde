size(600, 600)


def oned(n_squares, square_size, gap_square):
    for x in range(n_squares):
        if x != gap_square:
            fill(255)
        else:
            fill(0)
        square_x = x * square_size
        for y in range(n_squares):
            square_y = y * square_size
            rect(square_x, square_y, square_size, square_size)

oned(10, 50, 5)
