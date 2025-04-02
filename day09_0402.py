#String: Pattern Matching Methods_Lecture 2

def enum_str( head, s):
    nch = len(s)
    gap = len( str(nch))

    arrow_up = '\u2191' #unicode of up-arrow
    s0 = ' '.join([ ch.rjust(gap) for ch in s ])
    s1 = (arrow_up.rjust(gap) + ' ')*nch
    s2 = ' '.join([ str(k).rjust(gap) for k in range(nch) ])

    print(head+s0)
    print(' '*len(head)+s1)
    print(' '*len(head)+s2)

S = '0123456789abcdef'

enum_str( 'S --> ', S)
enum_str( 'S[:10] --> ', S[:10])
print('(1) S[2:13:2] -->', repr( S[2:13:2]))
print('(2) S[5::-1] -->', repr( S[2:13:2]))
print('(3) S[:5:-1] -->', repr( S[2:13:2]))
print('(4) S[::-1] -->', repr( S[2:13:2]))


#거꾸로 만들때 slicing 성질을 이용해서 reverse로 만들수가 있다.

S = 'apple'
aa = S[::-1]
print(aa)

#list mutable/ member : everything

