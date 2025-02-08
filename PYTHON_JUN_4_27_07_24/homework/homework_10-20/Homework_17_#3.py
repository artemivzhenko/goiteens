import re
from collections import Counter

def count_sentences(text):
    """
    Підраховує кількість речень у тексті.
    """
    sentences = re.split(r'[.!?]+', text)

    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def most_frequent_word(text):
    """
    Знаходить найбільш часто вживане слово у тексті.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]
    return most_common_word

def longest_word(text):
    """
    Знаходить найдовше слово у тексті.
    """
    words = re.findall(r'\b\w+\b', text)
    longest = max(words, key=len)
    return longest
