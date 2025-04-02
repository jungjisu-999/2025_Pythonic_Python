#String: Pattern Matching Methods_Lecture 2

import re
S = '/usr/home:myname'

mysplit1 = re.split('[/]', S)
# mysplit1_1 = re.split(' [/] ', S)
print( '(split-1)', mysplit1 )
# print( '(split-1)', mysplit1_1 )
#질문

mysplit2 = re.split('[:]', S)
print( '(split-2)', mysplit2 )
mysplit3 = re.split('[/:]', S)
print( '(split-3)', mysplit3 )

mymatch1 = re.match('(.*)[/:]', S)
print( '(match-1)', mymatch1.groups())
mymatch2 = re.match('[/:](.*)', S)
print( '(match-2)', mymatch2.groups())
mymatch3 = re.match('(.*)[/:](.*)', S)
print( '(match-3)', mymatch3.groups())
mymatch4 = re.match('[/:](.*)[/:]', S)
print( '(match-4)', mymatch4.groups())
mymatch5 = re.match('[/:](.*)[/:](.*)[/:](.*)', S)
print( '(match-5)', mymatch5.groups())
mymatch6 = re.match('(.*)[/:](,*)[/:](.*)[/:](.*)', S)  #질문
print( '(match-6)', mymatch6.groups())