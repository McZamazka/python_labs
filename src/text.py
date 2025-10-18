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

print(count_freq(["a","b","a","c","b","a"]))
print(top_n(count_freq(["a","b","a","c","b","a"])))