<h1>Прграммирование и алгоритмизация (Лабараторные)</h1>

<h2>Лабараторная №5:</h2>

**Задание A:**
```python
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """

    with open(json_path, encoding="utf-8") as f:
        try:
            people = json.load(f)  # считывает файл в формате json и возвращает объекты
        except ValueError as e:
            raise ValueError("Файл не должен быть пустым")

    keys = list(people[0].keys())
    list_object = set(keys)

    for objects in people[1:]:
        list_object.update(objects)
    alb = sorted(list_object - set(keys))
    fieldnames = keys + alb

    p = Path(csv_path)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in people:
            r = {key: r.get(key, "") for key in fieldnames}
            writer.writerow(r)
json_to_csv("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.json", "/Users/zamazka/Documents/GitHub/python_labs/src/data/out/people_from_json.csv")

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """

    with open(csv_path, encoding="utf-8") as f:
        try:
            people = csv.DictReader(f)
            to_json = list(people)
        except ValueError as e:
            raise ValueError("Ошибка чтения")


    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(to_json, f, ensure_ascii=False, indent=2)

csv_to_json("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv", "/Users/zamazka/Documents/GitHub/python_labs/src/data/out/people_from_csv.json")
```

![exe1_1_1!](/images/lab05/exe1_1.png)
![exe1_1_1!](/images/lab05/exe1_2.png)
![exe1_1_1!](/images/lab05/exe1_3.png)
![exe1_1_1!](/images/lab05/exe1_4.png)


**Задание B:**
```python
import csv

from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, encoding="utf-8", newline="") as f:
        try:
            reader = csv.reader(f)
            for row in reader:
                ws.append(row)
        except ValueError as e:
            raise ValueError("Ошибка чтения")

    for column in ws.columns:
        min_len = 8
        column_letter = column[0].column_letter   #сохраняем содержимое ячейки column[0] с помощью функции column_letter

        for cell in column:
            try:
                if len(str(cell.value)) > min_len:
                    min_len = len(str(cell.value))
            except:
                pass

        col_width = min_len + 2
        ws.column_dimensions[column_letter].width = col_width

    try:
        wb.save(xlsx_path)
    except FileExistsError as e:
        raise FileNotFoundError("Ошибка пути")

csv_to_xlsx("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv", "/Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.xlsx")
```

![exe1_1_1!](/images/lab05/exe1_2.png)
![exe1_1_1!](/images/lab05/exe2.png)

<h2>Лабараторная №6:</h2>

**Задание A:**
```python
import argparse
from pathlib import Path
import sys
sys.path.append('/Users/zamazka/Documents/GitHub/python_labs/src/mylibbs/')
from text import *


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        #python  cli_text.py cat --input /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.readlines()
            try:
                for index, line in enumerate(text, 1):
                    if args.n:
                        print(f"{index}: {line}")
                    else:
                        print(f"{line}")
            except ValueError:
                print("Error")

    elif args.command == "stats":
        #python  cli_text.py stats --input /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.txt --top 5
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.readlines()
            line_objects = {}
            try:
                for line in text:
                    line = line.split()
                    for i in line:
                        line_objects[i] = line_objects.get(i, 0) + 1
                top_objects = top_n(line_objects, args.top)
                for word, count in top_objects:
                    print(f"{word}: {count}")
            except ValueError:
                print("Error")
if __name__ == "__main__":
    main()
```

![exe1_1_1!](/images/lab06/exe2_1.png)
![exe1_1_1!](/images/lab06/exe2_2.png)
![exe1_1_1!](/images/lab05/exe1_1.png)
![exe1_1_1!](/images/lab05/exe1_2.png)
![exe1_1_1!](/images/lab05/exe1_3.png)
![exe1_1_1!](/images/lab05/exe1_4.png)

**Задание B:**
```python
import argparse
import sys
sys.path.append('/Users/zamazka/Documents/GitHub/python_labs/src/lab05')
sys.path.append('/Users/zamazka/Documents/GitHub/python_labs/src/lab05/')
from csv_xlsx import *
from json_csv import *


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()
    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

#python cli_convert.py json2csv --in /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.json --out /Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.csv
#python cli_convert.py csv2json --in /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv --out /Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.json
#python cli_convert.py csv_to_xlsx --in /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv --out /Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.xlsx
    main()
```

![exe1_1_1!](/images/lab06/exe1_1.png)
![exe1_1_1!](/images/lab06/exe1_2.png)
![exe1_1_1!](/images/lab06/exe1_3.png)
![exe1_1_1!](/images/lab06/exe1_4.png)
![exe1_1_1!](/images/lab06/exe1_5.png)