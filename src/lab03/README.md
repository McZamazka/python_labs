<h1>Прграммирование и алгоритмизация (Лабараторные)</h1>

<h2>Лабараторная №3:</h2>

**Задание A:**
**Пункт №1**
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = re.sub(r"[\x00-\x1F\x7F]+", " ", text)
    text = text.casefold() if casefold else text
    text = re.sub(r"\s+", " ", text.strip())
    text = text.replace("ё", "е") if yo2e else text
    return text
```

![exe1_1_1!](/images/lab03/exe01.png)
----------------------------------------------------
**Пункт №2**
```python
def tokenize(text: str) -> list[str]:
    allowed_chars = 'a-zA-Zа-яёА-ЯЯЁ0-9- '
    text = re.sub(f'[^{allowed_chars}]', ' ', text)
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text.split()
```

![exe1_1_1!](/images/lab03/exe02.png)
----------------------------------------------------
**Пункт №3-4**
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    counts = {}
    for tok in tokens:
        counts[tok] = counts.get(tok, 0) + 1
    return counts

def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
    words = list(sorted(freq.items(), key = lambda x: (-x[1], x[0])))[:n]
    return words
```



![exe1_1_1!](/images/lab03/exe03.png)

--------------------------------------------------------------------
**Задание B:**
```python
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

text_info("Привет мир, Привет/ Hellow rolds, good fhadsg jdsjsdj ufsdya")
```

![exe1_1_1!](/images/lab03/exe04.png)

-------------------------------------------