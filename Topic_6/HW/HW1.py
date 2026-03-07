def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            salaries = []
            for line in file:
                line = line.strip()
                parts = line.split(",")
                if not line or len(parts) != 2:
                    continue
                _, salary_str = parts
                salaries.append(int(salary_str.strip()))

        if not salaries:
            print("Файл не містить даних про зарплати.")
            return (0, 0)

        total = sum(salaries)
        average = total // len(salaries)
        return (total, average)

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return (0, 0)
    except PermissionError:
        print(f"Помилка: немає прав на доступ до файлу — '{path}'")
        return (0, 0)
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        return (0, 0)


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    if total != 0 and average != 0:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
