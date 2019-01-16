import string

def gsplit(str, sep=string.whitespace):
    word = ''
    for char in str:
        if char in sep:
            if word:
                yield word
                word = ''
        else:
            word += char

    yield word

def find_first_dupe(txt):
    uniques = set()

    words_generator = gsplit(txt)

    for word in words_generator:
        
        # WARNING: not handling trailing punctuation e.g. times,
        # further tweaks needed here
        if word in uniques:
            return word

        uniques.add(word)


if __name__ == "__main__":
    
    txt = 'it was the best of times, it was the worst of times'

    dupe = find_first_dupe(txt)

    print(dupe)
    
