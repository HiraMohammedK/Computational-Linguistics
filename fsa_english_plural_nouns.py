def is_plural_noun_accepted_fst(word):
    vowels = 'aeiou'
    state = 'START'
    
    if state == 'START' and word.endswith('ys'):
        state = 'YS_CHECK'
        if len(word) > 2 and word[-3] in vowels:
            state = 'ACCEPTED'
        else:
            state = 'REJECTED'
    elif state == 'START' and word.endswith('ies'):
        state = 'IES_CHECK'
        if len(word) > 3 and word[-4] in vowels:
            state = 'REJECTED'
        else:
            state = 'ACCEPTED'
    
    if state == 'ACCEPTED':
        return True
    else:
        return False

test_words = ['boys', 'toys', 'ponies', 'skies', 'puppies', 'boies', 'toies', 'ponys', 'carries', 'daisies']
results = {word: is_plural_noun_accepted_fst(word) for word in test_words}

print(results)
