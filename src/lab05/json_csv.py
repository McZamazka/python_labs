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

