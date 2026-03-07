from pathlib import Path


def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            parse_folder(el)
            print(f"this is folder {el}")
        else:
            print(f"this is file {el}")



parse_folder(Path("."))