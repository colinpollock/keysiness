"""Command line interface for timing how long it takes a user to type words. """

try:
    import simplejson as json
except ImportError:
    import json
import random
import sys
import time


DATA_FILENAME = 'data.json'


def load_data():
    """Return a (list, dict) pair. The list is words yet to be done and the
    dict maps from completed words to time taken to do them.
    """

    try:
        fh = open(DATA_FILENAME, 'r')
    except IOError:
        print >> sys.stderr, '* * * File "data.json" must already exist * * *'
        raise

    else:
        return tuple(json.load(fh))


def store_data(incomplete, completed):
    """Store a pair (incomplete, completed) in `DATA_FILENAME`."""

    with open(DATA_FILENAME, 'w') as out:
        json.dump([incomplete, completed], out, indent=3)
    


def time_word_typing(word):
    """Return the time it takes for the user to type the word in. Return None
    if the user misspells the word.
    """

    t0 = time.time()
    typed = raw_input("\n%s\n" % (word))
    if typed.strip() == word:
        return time.time() - t0
    else:
        return None



def main(args):
    incomplete, completed = load_data()
    random.shuffle(incomplete)
    word = None

    print "When you see the word, type it and hit enter..."
    
    try:
        while incomplete:
            word = incomplete.pop() 

            time_taken = time_word_typing(word)
            if time_taken is None:
                incomplete.append(word)
                random.shuffle(incomplete)
            else:
                completed[word] = time_taken

            word = None
            

    except EOFError:
        if word is not None:
            incomplete.append(word)
    
    finally:
        store_data(incomplete, completed)
        print
        return



if __name__ == '__main__':
    main(sys.argv[1:])
