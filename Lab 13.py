# main.py
import sys
from pathlib import Path
from file_utils import read_text_file, safe_write_text_file
from csv_utils import read_csv, filter_rows, write_csv
from json_utils import read_json, write_json, validate_config
from exceptions_demo import demo as exceptions_demo_demo
from context_manager_demo import demo as context_demo

SAMPLE_DIR = Path("sample_data")
SAMPLE_DIR.mkdir(exist_ok=True)


def prepare_sample_files():
    # create sample CSV
    people_csv = SAMPLE_DIR / "people.csv"
    if not people_csv.exists():
        rows = [
            {"name": "Alice", "age": "30", "city": "Almaty"},
            {"name": "Bob", "age": "22", "city": "Astana"},
            {"name": "Carol", "age": "27", "city": "Almaty"},
        ]
        write_csv(str(people_csv), rows, fieldnames=["name", "age", "city"])
    # create sample JSON
    cfg = SAMPLE_DIR / "config.json"
    if not cfg.exists():
        config = {"app_name": "Lab14", "version": "1.0", "debug": True}
        write_json(str(cfg), config)


def demo_csv_operations():
    csv_path = SAMPLE_DIR / "people.csv"
    rows = read_csv(str(csv_path))
    print("All rows from CSV:", rows)
    almaty = filter_rows(rows, lambda r: r.get("city") == "Almaty")
    print("Filtered (city == Almaty):", almaty)


def demo_json_operations():
    cfg_path = SAMPLE_DIR / "config.json"
    cfg = read_json(str(cfg_path))
    print("Config loaded:", cfg)
    # basic validation
    try:
        validate_config(cfg, {"app_name": str, "version": str})
        print("Config validated OK")
    except Exception as e:
        print("Config validation failed:", e)


def demo_file_operations():
    txt = SAMPLE_DIR / "notes.txt"
    safe_write_text_file(txt, "This is a safe write.\nSecond line.")
    print("Read back text file:")
    print(read_text_file(txt))


def menu():
    print("=== Lab 14 Demo Menu ===")
    print("1) CSV operations")
    print("2) JSON operations")
    print("3) File safe write/read")
    print("4) Exceptions demo")
    print("5) Context manager demo")
    print("0) Exit")
    choice = input("Choose: ").strip()
    return choice


def main():
    prepare_sample_files()
    while True:
        c = menu()
        if c == "1":
            demo_csv_operations()
        elif c == "2":
            demo_json_operations()
        elif c == "3":
            demo_file_operations()
        elif c == "4":
            exceptions_demo_demo()
        elif c == "5":
            context_demo()
        elif c == "0":
            print("Bye")
            sys.exit(0)
        else:
            print("Unknown choice")


if __name__ == "__main__":
    main()
