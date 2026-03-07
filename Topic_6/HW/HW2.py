def get_cats_info(path):
    """
    Reads a file with cat information and returns a list of dictionaries.

    Args:
        path (str): Path to the text file with cat data.

    Returns:
        list: A list of dictionaries with keys "id", "name", "age".
    """
    cats = []

    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")
                if not line or len(parts) != 3:
                    continue

                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
    except PermissionError:
        print(f"Помилка: немає прав на доступ до файлу — '{path}'")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")

    return cats


if __name__ == "__main__":
    # Example usage
    cats_info = get_cats_info("cats_file.txt")
    for cat in cats_info:
        print(cat)