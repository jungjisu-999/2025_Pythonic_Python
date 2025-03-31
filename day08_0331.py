S = ' Straw.Berry is good\n '

print(' (1) print(S)')
print('['+S+']')
print( '(2) print( repr(S) )')
print('[' + repr(S)+ ']')

#String: formatting Methods(3/5)

S0 = 'It is very nice to learn PYthon.'
print('S0 =', S0)
S1 = 'It %s very %s to learn %s.' % ('is', 'nice','Python')
print('S1 =', S1)

S2 = 'It {} very {} to learn {}.'.format('is','nice','Python')
print('S2 =', S2)
S3 = 'It {0} very {1} to arn {2}.'.format('is','nice', 'Python')
print('S3 =', S3)
S4 = 'It {2} very {1} to learn {0}.'.format('is', 'nice','Python')
print('S4 =', S4)

try:
    S_err = 'It {0} very {1} to learn {4}.'.format('is', 'nice', 'Python')
    print('S_err=', S_err)
except IndexError as e:
    print( e )


