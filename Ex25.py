def break_into_words(sentence):
    "This will break a sentence into words"
    words = sentence.split()
    return words

def first_word(words):
    "This will return first word"
    first_word = words[0]
    return first_word

def last_word(words):
    "this will return the last word"
    last_word = words[-1]
    return last_word

def sort_words(words):
    "sorts the words"
    return sorted(words)


def sort_sentence(sentence):
    "this will break a sentence into words and then sorts the words"
    words = break_into_words(sentence)
    return sorted(words)

def print_first_last_words(sentence):
    "this will break a sentence into words and prints the first and last words"
    words = break_into_words(sentence)
    print first_word(words)
    print last_word(words)


def print_first_last_words_sorted(sentence):
    "this will rpint the first and last word of a sorted sentence"
    words = break_into_words(sentence)
    sorted_words = sort_words(words)
    print first_word(sorted_words)
    print last_word(sorted_words)

