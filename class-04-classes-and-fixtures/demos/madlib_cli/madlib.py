

import re


def welcome():
    print('Welcome to the Jungle')


def read_file(path):
    with open(path) as f:
        return f.read()


def get_keys(format_string):
    """
    """
    key_list = list()
    end = 0

    repetitions = format_string.count('{')
    for i in range(repetitions):
        start = format_string.find('{', end) + 1
        end = format_string.find('}', start)
        key = format_string[start:end]
        key_list.append(key)

    return key_list


def remove_keys(format_string):
    """
    """
    regex = r"\{.*?\}"
    output = re.sub(regex, '{}', format_string)
    return output

def parse(raw):
    prompts = get_keys(raw)
    stripped = remove_keys(raw)
    return prompts, stripped

def parse_old(raw):
    prompts = []
    stripped = ''
    prompt = ''
    mid_prompt = False

    for ch in raw:

        if ch == '{':
            mid_prompt = True
            stripped += ch

        elif ch == '}':
            prompts.append(prompt)
            prompt = ''
            mid_prompt = False
            stripped += ch

        elif mid_prompt:
            prompt += ch

        else:
            stripped += ch


    return prompts, stripped


def add_response(prompt, responses):
    response = input(f'Enter a {prompt}: ')

    responses.append(response)


def get_responses(prompts):
    responses = []

    for prompt in prompts:
        add_response(prompt, responses)

    return responses


def write_file(path, contents):
    with open(path, 'w') as f:
        f.write(contents)


def tell_story(raw):
    welcome()

    prompts, stripped = parse(raw)

    responses = get_responses(prompts)

    story = stripped.format(*responses) # turn into 'Adjective','Adjective', 'Noun' as opposed to list

    return story


if __name__ == '__main__':
    raw = read_file('./madlib_raw.txt')

    story = tell_story(raw)

    write_file('./madlib_completed.txt', story)


