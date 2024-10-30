import re

def tokenize(text):
    pattern = r"""(?x)
                  (?:[A-Za-z]\.){2,}           # Abbreviations like U.S.A.
                | (?:\w+(?:-\w+)+)             # Hyphenated words like ice-cream
                | \b\w+'\w+\b                  # Contractions like can't, it's, isn't
                | \b\w+\b                      # Standalone words
                | [\.,!?;:]                    # Punctuation
                | [^ \t\n]+                    # Any remaining non-whitespace characters
                """
  
    tokens = re.findall(pattern, text)
    processed_tokens = []
    for token in tokens:
        if re.match(r"\b\w+n't\b", token):     
            processed_tokens.append(token[:-3])
            processed_tokens.append("n't")
        elif re.match(r"\b\w+'\w+\b", token):   
            processed_tokens.append(token.split("'")[0])
            processed_tokens.append("'" + token.split("'")[1])
        else:
            processed_tokens.append(token)
    
    return processed_tokens

text = "I can't believe it's already October! U.S.A. has ice-cream and isn't it great?"
tokens = tokenize(text)
print(tokens)
