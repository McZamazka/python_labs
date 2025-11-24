import argparse
import sys

sys.path.append("/Users/zamazka/Documents/GitHub/python_labs/src/lab05")
sys.path.append("/Users/zamazka/Documents/GitHub/python_labs/src/lab05/")
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

    # python cli_convert.py json2csv --in /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.json --out /Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.csv
    # python cli_convert.py csv2json --in /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv --out /Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.json
    # python cli_convert.py csv_to_xlsx --in /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv --out /Users/zamazka/Documents/GitHub/python_labs/src/data/out/people.xlsx
    main()
