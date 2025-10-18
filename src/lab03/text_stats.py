import sys
import os

# Добавляем родительскую директорию 'my_project' в путь поиска
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mylibbs import text


import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = re.sub(r"[\x00-\x1F\x7F]+", " ", text)
    text = text.casefold() if casefold else text
    text = re.sub(r"\s+", " ", text.strip())
    text = text.replace("ё", "е") if yo2e else text
    return text


def tokenize(text: str) -> list[str]:
    allowed_chars = "a-zA-Zа-яёА-ЯЯЁ0-9- "
    text = re.sub(f"[^{allowed_chars}]", " ", text)
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text.split()


def count_freq(tokens: list[str]) -> dict[str, int]:
    counts = {}
    for tok in tokens:
        counts[tok] = counts.get(tok, 0) + 1
    return counts


def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
    words = list(sorted(freq.items(), key=lambda x: (-x[1], x[0])))[:n]
    return words


def text_info(table: bool = True):
    text = sys.stdin.readline().strip()
    words = sorted(tokenize(normalize(text)), key=len, reverse=True)
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(set(tokenize(normalize(text))))}")
    print("Топ-5:")
    if table:
        print("слово" + " " * (len(max("Слово", max(words), key=len))-len(min("Слово", max(words), key=len))+1) + "|" + " частота")
        print("-" * (len(max("Слово", max(words), key=len))+1+len("|" + " частота")))
        for w in count_freq(tokenize(normalize(text))):
            word = w.ljust(len(max("Слово", max(words), key=len))+1)
            print(f"{word}| {count_freq(tokenize(normalize(text))).get(w)}")
    else:
        for w in count_freq(tokenize(normalize(text))):
            print(f"{w}:{count_freq(tokenize(normalize(text))).get(w)}")

text_info(True)




