#02강 More on Dictionary
#my_dict_more.py

def show_iterable(iterable, headline ):
    print(str(headline)+ '=' )

    key_iterator = iter(dct.keys())
    while True :
        try:
            print('{:>20s}'.format( str(next(key_iterator))))
        except StopIteration: break
dct = dict( [ (1, 'first'), ('a', ord('a')), ((1,2), 3.14)]) # ord : 문자에 대응하는 아스키 넘버를 반환   ex: .txt

print( '(1)', dct)

print( '(2) keys() -->', dct.keys())
print( '(3) values() ->', dct.values())
print( '(4) items() -->', dct.items() )

show_iterable(dct.keys(), type(dct.keys()))

value = dct.pop('apple', 'no-apple')
print("(5) pop 'apple' -->", value, 'dct =', dct)

value = dct.pop('a', 0)
print("(6) pop 'a' -->", value, 'dct =', dct)


#어느요일에 달력 날짜가 시작되는지 or 행을 몇줄로 할지.
# 바둑 두는 프로그램도 만들수 있다.


import tableau as tb

if __name__ == '__main__':
    table =