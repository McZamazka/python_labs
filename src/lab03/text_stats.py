import sys
sys.path.append('/Users/zamazka/Documents/GitHub/python_labs/src/mylibbs/')
from text import *


def text_info(text: str, table: bool = True):
    tokens = tokenize(normalize(text))
    top_words = top_n(count_freq(tokens), 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")

    if table:
        top_words_only = [word for word, count in top_words]
        max_word_length = max(len("слово"), *[len(word) for word in top_words_only])

        print("слово" + " " * (max_word_length - len("слово") + 1) + "|" + " частота")
        print("-" * (max_word_length + 1 + len("| частота")))
        for word, count in top_words:
            word_padded = word.ljust(max_word_length + 1)
            print(f"{word_padded}| {count}")
    else:
        for word, count in top_words:
            print(f"{word}: {count}")





