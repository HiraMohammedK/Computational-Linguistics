# -*- coding: utf-8 -*-
"""FSA-english-plural-nouns.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aWVowp2IBWUv8RUwmAPdyb8s6KQS4VTP
"""

def is_plural_noun_accepted(word):
    vowels = 'aeiou'

    if word.endswith('ys'):
        if len(word) > 2 and word[-3] in vowels:
            return True
        else:
            return False

    if word.endswith('ies'):
        if len(word) > 3 and word[-4] in vowels:
            return False
        else:
            return True

    return False

# Test cases
test_words = ['boys', 'toys', 'ponies', 'skies', 'puppies', 'boies', 'toies', 'ponys', 'carries', 'daisies']
results = {word: is_plural_noun_accepted(word) for word in test_words}

print(results)