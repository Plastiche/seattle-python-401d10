from textwrap import dedent

WIDTH = 89

menu = {
    'Appetizers' : {
      'Wings':0,
        'Cookies':0,
        'Spring Rolls':0
    },
    'Entrees': {
        'Salmon':0,
        'Steak':0,
        'Meat Tornado':0,
        'A Literal Garden':0,

    },
    'Desserts': {
        'Ice Cream':0,
        'Cake':0,
        'Pie':0,
    },
    'Drinks': {
        'Coffee':0,
        'Tea':0,
        'Blood of the Innocent':0,
    }

}

def padEdges(str, width, ch =' '):
    str_len = len(str)

    ragged_pad = ''

    if width % 2 != str_len % 2:
        ragged_pad = ch

    return (ch * (((width - str_len)) // 2)) + str + (ch * ((width - str_len) // 2)) + ragged_pad


def greeting():
    line_1 = '** ' * (WIDTH // 3)
    line_2 = 'Welcome to the Snakes Cafe'
    line_3 = 'Please see our menu below'
    line_4 = 'To quit at any time type "quit"'


    print(dedent(f'''
        {'*' * WIDTH}
        {'**' + padEdges(line_2, WIDTH - 4) + '**'}
        {'**' + padEdges(line_3, WIDTH - 4) + '**'}
        {'**' + padEdges('', WIDTH - 4) + '**'}
        {'**' + padEdges(line_4, WIDTH - 4) + '**'}
        {'*' * WIDTH}
    '''))


def ask():
    print(dedent(f'''
    {'*' * WIDTH}
    {'**' + padEdges('What would you like to order?', WIDTH - 4) + '**'}
    {'*' * WIDTH}
    '''))


def print_menu():
    for course in menu:
        print(course)
        print('-' * len(course))
        for item in menu[course]:
            print(item)
        print('\n')


def process_order(order):

    found = False

    for course in menu:

        if order in menu[course]:
            menu[course][order] += 1
            print(f'You have {menu[course][order]} {order}')
            found = True
            break

    if not found:
        print('disgusting')

if __name__ == '__main__':
    greeting()
    print_menu()
    ask()

    order = None

    while order != 'quit':
        order = input()
        process_order(order)
