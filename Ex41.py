from urllib import urlopen
#from sys import argv
import sys
import random

words_url = 'https://learnpythonthehardway.org/words.txt'
words = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class names %%% that is-a %%%.",
    "class %%%(object):\n\tdef _init_(self, ***)":
        "class %%% has-a _init_ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function names *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}
#print open_words_url.read()
#print open_words_url.readline()

open_words_url = urlopen(words_url)
for i in open_words_url.readlines():
    #print i
    words.append(i.strip())

print words

phrase_first = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    phrase_first = True

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(words, snippet.count("%%%"))]
    # print class_names
    # print snippet.count("***")
    other_names = random.sample(words, snippet.count("***"))
    # print other_names
    results = []
    param_names = []
    # print snippet.count("@@@")
    for i in range(0, snippet.count("@@@")):
        # print i
        param_count = random.randint(1,3)
        # print "param_count value is", param_count
        param_names.append(', '.join(random.sample(words, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        print result
        for word in class_names:
            result = result.replace("%%%", word, 1)
        print other_names
        for word in other_names:
            result = result.replace("***", word, 1)
        print param_names
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = PHRASES.keys()
        print snippets
        random.shuffle(snippets)
        print snippets
        for snippet in snippets:
            phrase = PHRASES[snippet]
            print snippet, phrase
            question, answer = convert(snippet, phrase)
            if phrase_first:
                question, answer = answer, question
            print question

            raw_input("> ")

            print "ANSWER: %s\n\n" %answer
except EOFError:
    print "\nBye"






