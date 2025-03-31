import random


def touch(a, b, position, n_moves):
    current = position

    for k in range( n_moves ):
        current += random.choice([-1, 1])
        if current == a or current == b:
            return current

    return current

def show_result( a, b, trials, a_touches, b_touches ):
    a_prob = a_touches/trials
    b_prob = b_touches/trials

    print('+' + '-'*5 + '+' + '-'*19 + '+' + '-'*13 + '+')
    print('|' + ' end ' + '|' + f'trials={trials:12d}' + '|' + ' probability ' + '|')
    print('+' + '-'*5 + '+' + '-'*19 + '+' + '-'*13 + '+')
    print('|' + f'{a:5d}' + '|' + f'{a_touches:19d}' + '|' + f'{a_prob:13.4f}' + '|')
    print('|' + f'{b:5d}' + '|' + f'{b_touches:19d}' + '|' + f'{a_prob:13.4f}' + '|')
    print('+' + '-'*5 + '+' + '-'*19 + '+' + '-'*13 + '+')

if __name__ == '__main__':
    a = eval(input('a = '))
    b = eval(input('b = '))
    initial = eval(input('initial position = '))
    n_steps = eval(input('maximum steps = '))
    m_trials = eval(input('how many trials = '))

    a_touch = 0
    b_touch = 0

    for trial in range(m_trials):
        final = touch(a, b, initial, n_steps)
        if final == a:
            a_touch += 1

        if final == b:
            b_touch += 1

    show_result(a, b, m_trials, a_touch, b_touch)


