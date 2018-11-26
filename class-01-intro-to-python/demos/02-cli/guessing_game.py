from textwrap import dedent
import sys


WIDTH = 60
BANK = [
    {
        'question': 'How old do you think I am?\n',
        'answer': '35',
        'status': False,
    },
    {
        'question': 'What state was I born in?\n',
        'answer': 'washington',
        'status': False,
    },
]


def welcome():
    """Function for greeting a user when the CLI starts.
    """
    ln_one = 'Welcome to my Guessing Game'
    ln_two = 'Answer the following questions about me'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}
        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
        {'*' * WIDTH}
    '''))


def ask_question(question):
    return input(question)


def check_input(user_in, answer):
    if user_in.lower() == 'quit':
        exit()

    if user_in.lower() == answer:
        return True

    return False

def feedback(status):
    if status is True:
        print(dedent('''Congrats. You are correct.'''))
        return

    print(dedent('''Sorry. You got it wrong.'''))


def exit():
    print(dedent('Thank you for playing my game'))
    sys.exit()


def run():
    welcome()
    # Set up a loop that iterates through the BANK and asks questions until answers are correct
    for item in BANK:
        while item['status'] is False:
            # ask the user a question
            user_input = ask_question(item['question'])
            # check the answer
            status = check_input(user_input, item['answer'])
            # provide feeldback
            feedback(status)

            if status is True:
                item['status'] = status



if __name__ == '__main__':
    run()
