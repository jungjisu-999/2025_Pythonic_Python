#List / mutable

def get_entry( mat, i_row, j_col) :
    try:
        row_pick = mat[i_row]
        return row_pick[j_col] if j_col < len(row_pick) else 0.0
    except IndexError:
        return 0.0

def show_matrix( mat, words ):
    size_row = len(mat)
    size_col = max( [len(row) for row in mat])

    print(words)
    for i in range(size_row):
        entries = [ '{:12.4f}'.format(get_entry(mat, i, j))
                    for j in range(size_col)]
        print( ' '.join(entries) )

#List is able to describe a matrix
M = [ [1, 2, 3], [4, 5], [7] ]
show_matrix( M, '(1) M -->')
print('(2) M[0] -->', M[0])
print('(3) M[0][2] -->', M[0][2])

#List is mutable
M[1] = [40,50,60]
show_matrix( M, '(4) M -->')

col_1 = [ get_entry(M,i,1) for i in range(len(M))]
print('(5) 1st column of M -->', col_1)
