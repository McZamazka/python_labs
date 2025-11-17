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