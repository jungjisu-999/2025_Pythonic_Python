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
if __name__=='__main__':
    matrix = [[1,2,3], [10,20], [100,200,300,400]]
    a_ij = get_entry(matrix, 3, 2)
    print( a_ij )

    show_matrix( matrix, 'show this matrix =')
    n = 3
    m = [[1/(1+j+i) for i in range( n ) ] for j in range(n)]
    show_matrix( m, 'm=')

    G = ( sum(row) for row in m)
    print(G)

    try:
        print(next(G))
        print(next(G))
        print(next(G))
        print(next(G))
    except StopIteration:
        print('Exceed the end of generator')

        # commit 안함
        #다음 시간때는 numpy package(1/3)부분부터 시작할거다.
        # 행렬 점수 계산 코드 이해 xxx 다시 보기















# #List is able to describe a matrix
# M = [ [1, 2, 3], [4, 5], [7] ]
# show_matrix( M, '(1) M -->')
# print('(2) M[0] -->', M[0])
# print('(3) M[0][2] -->', M[0][2])
#
# #List is mutable
# M[1] = [40,50,60]
# show_matrix( M, '(4) M -->')
#
# col_1 = [ get_entry(M,i,1) for i in range(len(M))]
# print('(5) 1st column of M -->', col_1)
