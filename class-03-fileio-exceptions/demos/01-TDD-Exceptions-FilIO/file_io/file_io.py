
def read_file(path):
    """
    Read a file at a given path and return it's text contents
    """

    if('forbidden' in path):
        raise Exception('Forbidden')

    with open(path, 'r') as f:
        return f.read()

def read_file_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

def write_file(path, contents):
    with open(path, 'w') as f:
        f.write(contents)


def read_file_binary(path):
    with open(path, 'rb') as f:
        return f.read()


















# def read_file(path):

#     if('forbidden' in path):
#         raise Exception('Forbidden')
#         return

#     print('read file')

#     with open(path, 'r') as f:
#         return f.read()


# def read_file_lines(path):
#     with open(path, 'r') as f:
#         return f.readlines()




