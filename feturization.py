"""Some featurization code."""

from __future__ import division

from pprint import pprint
import sys

VOWELS = 'aeiou'
HOME_ROW = 'asdfghjkl'


LP = 'left_pinky'
LR = 'left_ring'
LM = 'left_middle'
LI = 'left_index'
RI = 'right_index'
RM = 'right_middle'
RR = 'right_ring'
RP = 'right_pinky'

KEY_TO_FINGER = dict(a=LP, b=LI, c=LI, d=LM, e=LM, f=LI, g=LI, h=RI, i=RM,
                     j=RI, k=RM, l=RR, m=RI, n=RI, o=RR, p=RP, q=LP, r=LI,
                     s=LR, t=LI, u=RI, v=LI, w=LR, x=LR, y=RI, z=LP)

def length(word):
    return len(word)


def num_vowels(word):
    """Return the number of vowels in `word`.
    >>> num_vowels('pneumonic')
    4
    """
    return sum(char in VOWELS for char in word.lower())


def percent_home_row(word):
    """Return the percent of letters in `word` that are in 'asdfghjkl'.
    >>> percent_home_row('asdf')
    1.0
    >>> _floats_equal(percent_home_row('colin'), .2, .001)
    True
    """

    return sum(char in HOME_ROW for char in word.lower()) / len(word)


def num_same_finger_pairs(word):
    """Return the number of consecutive letter pairs that are typed with the
    same finger and are not the same letter.

    >>> num_same_finger_pairs('aaa')
    0
    >>> num_same_finger_pairs('qafvg')
    3
    """
    return sum(KEY_TO_FINGER[first] == KEY_TO_FINGER[second] and first != second
               for (first, second) in _pairs(word))


def featurize(word):
    return {'length': length(word),
            'num_vowels': num_vowels(word),
            '%_home_row': percent_home_row(word),
            'num_same_finger_pairs': num_same_finger_pairs(word)}


def _floats_equal(x, y, epsilon):
    return abs(x - y) < epsilon

def _pairs(xs):
    return zip(xs[:-1], xs[1:])


def main(args):
    if args[0] in ('-t', '--test'):
        import doctest
        print >> sys.stderr, doctest.testmod()
    else:
        word = args[0]
        pprint(featurize(word), indent=2)

if __name__ == '__main__':
    main(sys.argv[1:])
