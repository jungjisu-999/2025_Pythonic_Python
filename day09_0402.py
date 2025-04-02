#String: Pattern Matching Methods_Lecture 2

S = 'Saint 24 John 07 makes me cloud 9.'
tbl = str.maketrans('mSao', 'eJot', '0123456789')
SS = S.translate( tbl )
print(SS)

# isspace(), isdigit(), isnumeric()
