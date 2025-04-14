#02강 Dictionary(2/5) ex
def test_1():
    L1 = ['a', 'b', 'c']
    L2 = [1,2,3,4]
    L3 = [ 'apple', 'bababas', 'carrot']

    z123 = zip(L1, L2, L3)
    print( 'z123 = ', z123 )

    # ( ) --> 튜플
    L123 = list(z123)
    print('L123 =', L123 )
    x = list( zip ( *L123) ) # zip을 풀어쓴다.
    print( 'x = ', x)
    L1r = list( x[0] )
    print('L1r =', L1r)

def mysum( *x):
    x_sum = 0
    for member in x:
        x_sum += member

    return x_sum
if __name__=='__main__':
    #test_1()
    print( mysum(1,2.3))
    print( mysum(1,2.3,7,8,9))

    L = [0.1, 0.2, 0.3]
    print(mysum( *L ))
    # 변수 이름으로 쓸수 있는 string

    'xyz'.isidentifier() # 교수님처럼 ture가 나오지 않음



