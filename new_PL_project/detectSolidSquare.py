matrix = [[1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 0, 1],
          [0, 0, 1, 0, 0, 0, 1],
          [0, 0, 1, 1, 1, 1, 1]]


def max_size(mat, ZERO=0):
    """Find the largest square of ZERO's in the matrix `mat`."""
    nrows, ncols = len(mat), (len(mat[0]) if mat else 0)
    if not (nrows and ncols): return 0 # empty matrix or rows
    counts = [[0]*ncols for _ in xrange(nrows)]
    for i in reversed(xrange(nrows)):     # for each row
        assert len(mat[i]) == ncols # matrix must be square
        for j in reversed(xrange(ncols)): # for each element in the row
            if mat[i][j] != ZERO:
                counts[i][j] = (1 + min(
                    counts[i][j+1],  # east
                    counts[i+1][j],  # south
                    counts[i+1][j+1] # south-east
                    )) if i < (nrows - 1) and j < (ncols - 1) else 1 # edges
    print max(c for rows in counts for c in rows)
    return max(c for rows in counts for c in rows)

max_size(matrix,0)