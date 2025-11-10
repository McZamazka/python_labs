from pathlib import Path
import sys
sys.path.append('/Users/zamazka/Documents/GitHub/python_labs/src/mylibbs/')
from text import *

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError
    try:
        text = p.read_text(encoding=encoding)
        text = normalize(text)
        return text
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError() from e

txt = read_text("/Users/zamazka/Documents/GitHub/python_labs/src/data/input.txt")
print(txt)

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=",")
        if header is not None:
            w.writerow(header)
        if len(rows) != 0:
            try:
                max_len = max(len(s) for s in rows)
            except ValueError:
                raise ValueError("Ошибка записи")
            if all(len(s) == max_len for s in rows):
                for r in rows:
                    w.writerow(r)
            else:
                raise ValueError("Длина строк не одинаковая")
        else:
            w.writerows(rows)

write_csv([("word","count"),("test",3)], "/Users/zamazka/Documents/GitHub/python_labs/src/data/report.csv")
