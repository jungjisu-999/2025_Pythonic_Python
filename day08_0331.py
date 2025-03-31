def length( s ):
    count = 0
    for _ in s:
        count += 1
    return count

def insert( s, at, piece ):
    over = at - length( s )
    n_spaces = over if over > 0 else 0
    s_aug = s + ' ' * n_spaces
    return s_aug[:at] + piece + s_aug[at:]

def remove( s, at, n_remove ):
    front_part = s[:at]
    end_part = s[at + n_remove:]
    return front_part + end_part

def dump( s, at, piece ):
    s_removed = remove( s, at, length(piece))
    return insert( s_removed, at, piece )

if __name__=='__main__':
    print( 'the length of [apple] -->', length('apple'))
    print( 'the length of [How are you?] -->', length('How are you?'))

    string = input('input a string = ')

    print( 'insert XXX at=0 -->', repr(insert(string, 0, 'XXX')))
    print( 'insert XXX at=3 -->', repr(insert(string, 3, 'XXX')))
    print( 'insert XXX at=7 -->', repr(insert(string, 7, 'XXX')))
    print( 'insert XXX at=9 -->', repr(insert(string, 9, 'XXX')))
    print( 'insert XXX at=10 -->', repr(insert(string, 10, 'XXX')))
    print( 'insert XXX at=12 -->', repr(insert(string, 12, 'XXX')))

    print( 'remove 4 items at 0 -->', repr(remove(string, 0, 4)))
    print( 'remove 4 items at 2 -->', repr(remove(string, 2, 4)))
    print( 'remove 4 items at 6 -->', repr(remove(string, 6,4)))
    print( 'remove 4 items at 8 -->', repr(remove(string, 8, 4)))
    print( 'remove 4 items at 9 -->', repr(remove(string, 9, 4)))
    print( 'remove 4 items at 12 -->', repr(remove(string, 12, 4)))

    print( 'dump XXX at=0 -->', repr(dump(string, 0, 'XXX')))
    print('dump XXX at=3 -->', repr(dump(string, 3, 'XXX')))
    print('dump XXX at=7 -->', repr(dump(string, 7, 'XXX')))
    print('dump XXX at=9 -->', repr(dump(string, 9, 'XXX')))
    print('dump XXX at=10 -->', repr(dump(string, 10, 'XXX')))
    print('dump XXX at=12 -->', repr(dump(string, 12, 'XXX')))





