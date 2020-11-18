from string import punctuation

EXCLUDE_CHARS = set(punctuation).union(set('’'))
def simple_tokeniser(text):
    return text.split()