# [] : list mutable
# () : tuple immutable 하나를 바꾸고 싶어도 list처럼 한 개만 바꾸지 못 한다.
# {} : dictionary / key : value
# {} : set

import funs as FS
#from funs import table
#FS.table(3,5)

#print( dir( FS ) )
#funs.table(3,5)

#print( funs.addition(10, 20) )
exec( open('funs.py', 'r').read() )


