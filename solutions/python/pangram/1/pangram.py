def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_chars = set(sentence.lower())
    return alphabet.issubset(sentence_chars)
