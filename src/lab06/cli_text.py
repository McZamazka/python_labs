import argparse
from pathlib import Path
import sys

sys.path.append("/Users/zamazka/Documents/GitHub/python_labs/src/mylibbs/")
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
        # python  cli_text.py cat --input /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.csv
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
        # python  cli_text.py stats --input /Users/zamazka/Documents/GitHub/python_labs/src/data/samples/people.txt --top 5
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
