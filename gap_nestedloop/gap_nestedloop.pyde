size(500, 500)


def oned(n_squares, square_size, gap_square):
    """Out the squares in rows and columns. The gap square of each row is black 
    and all others are white"""
    # draw a row of squares where the gap square is black
    for x in range(n_squares):
        if x != gap_square:
            fill(255)
        else:
            fill(0)
        square_x = x * square_size
        # create multiple rows
        for y in range(n_squares):
            square_y = y * square_size
            rect(square_x, square_y, square_size, square_size)

# create a 10x10 grid of squares with side lengths of 50 pixels.
# the 5th square of each line if black
oned(10, 50, 5)
