import collections
import re

def word_count(string):
    return collections.Counter(get_words(string))

def get_words(string):
    return re.findall('[^_\W]+', string.lower())
