def cut_by_piece(S, piece, n_max ):
    L_piece = len(piece)
    L_S = len( S )

    found = []

    for ith in range( L_S ) :
        k = S.find(piece )
        if k == -1:
            found.append( len(S))
            return found

        found.append( k )
        S = S[k+L_piece:]

    return found
def find_all(S, piece, n_max):
    res = cut_by_piece( S, piece, n_max)
    return res


if __name__=='__main__':
    S_given = '1234XXX56XXX7890123XXX98765'
    result = find_all( S_given, 'XXX', 100)
    print( result)


