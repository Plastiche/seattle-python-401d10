# '/usr/share/dict/words'
# The above path is the dictionary of words that your computer uses
import os
import sys


def get_words():
    """Function that reads all the words your machine is aware of and writes
    any word more than 3 characters to a new file
    """
    with open('/usr/share/dict/words', 'r') as rf:
        # The `with` keyword is useful for providing file data as context
        with open('./assets/words.txt', 'w') as wf:
            for line in rf:
                if len(line) > 3:
                    wf.write(line)

    print('words.txt created in assets folder')


def get_non_exists():
    """Function that demonstrates the usefulness of try/except/finally
    and exception handling in Python
    """
    print('I ran first')
    try:
        print('I ran second')
        with open('somefile.blarp', 'r') as f:
            print(f.read())
    except (FileNotFoundError, TypeError)as e:
        print(e)

    finally:
        print('I ran last, regardless of success or failure.')

def get_exception():
    open('somefile.blarp','r')


def say_hi():
    print('hola')


def kill_assets():
    confirm = input('You sure you want to do this?')

    if confirm != 'y':
        return

    files = os.listdir('./assets')

    for file in files:
        try:
            os.remove('./assets/' + file)
        except IOError:
            print('unable to remove', file)


def run(func_name):
    try:
        FUNCS[func_name]()
    except KeyError:
        print(func_name + ' not a recognized function')


FUNCS = {
    'words': get_words,
    'delete': kill_assets,
    'non': get_non_exists,
    'hi' : say_hi,
}

if __name__ == '__main__':
    func_name = sys.argv[1]

    run(func_name)
