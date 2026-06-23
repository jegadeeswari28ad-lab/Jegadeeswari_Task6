import re
import nltk
from nltk.corpus import brown
from collections import Counter, defaultdict
from difflib import get_close_matches

# Download dataset
nltk.download('brown', quiet=True)

# =========================
# LOAD & PREPROCESS DATA
# =========================

words = [
    word.lower()
    for word in brown.words()
    if word.isalpha()
]

sentences = brown.sents()

word_freq = Counter(words)
vocab = list(word_freq.keys())

# =========================
# BUILD BIGRAM MODEL
# =========================

bigrams = defaultdict(Counter)

for sentence in sentences:

    sentence = [
        w.lower()
        for w in sentence
        if w.isalpha()
    ]

    for i in range(len(sentence) - 1):
        current_word = sentence[i]
        next_word = sentence[i + 1]

        bigrams[current_word][next_word] += 1


# =========================
# AUTOCOMPLETE
# =========================

def autocomplete(word, top_n=5):

    word = word.lower()

    if word not in bigrams:
        return []

    predictions = bigrams[word].most_common(top_n)

    return [
        f"{next_word} ({count})"
        for next_word, count in predictions
    ]


# =========================
# SENTENCE AUTOCOMPLETE
# =========================

def sentence_autocomplete(text, top_n=5):

    tokens = text.lower().split()

    if len(tokens) == 0:
        return []

    last_word = tokens[-1]

    return autocomplete(last_word, top_n)


# =========================
# AUTOCORRECT
# =========================

def autocorrect(word, top_n=5):

    word = word.lower()

    matches = get_close_matches(
        word,
        vocab,
        n=20,
        cutoff=0.7
    )

    matches = sorted(
        matches,
        key=lambda x: word_freq[x],
        reverse=True
    )

    return matches[:top_n]


# =========================
# ANALYTICS
# =========================

def top_words(n=20):

    return word_freq.most_common(n)


def vocabulary_size():

    return len(vocab)


def total_words():

    return len(words)