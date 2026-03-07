"""
hw03.py — Візуалізація структури директорії з кольоровим виведенням.

Використання:
    python hw03.py /шлях/до/директорії
"""

import sys
from pathlib import Path

from colorama import Fore, Style, init

# Ініціалізація colorama (autoreset=True скидає стиль після кожного print)
init(autoreset=True)


def visualize_directory(directory: Path, indent: int = 0) -> None:
    """
    Рекурсивно обходить директорію та виводить її вміст з кольоровим форматуванням.

    Аргументи:
        directory: об'єкт Path, що вказує на поточну директорію.
        indent:    рівень відступу для вкладених елементів.
    """
    # Отримуємо вміст директорії і сортуємо: спочатку директорії, потім файли
    try:
        entries = sorted(directory.iterdir())
    except PermissionError:
        prefix = "  " * indent
        print(f"{prefix}{Fore.RED}[Доступ заборонено]{Style.RESET_ALL}")
        return

    for entry in entries:
        prefix = "  " * indent

        if entry.is_dir():
            # Директорії — яскраво-синій, жирний
            print(f"{prefix}{Fore.CYAN}{Style.BRIGHT}{entry.name}/")
            # Рекурсивний виклик для піддиректорії
            visualize_directory(entry, indent + 1)

        elif entry.is_file():
            # Файли — зелений
            print(f"{prefix}{Fore.GREEN}{entry.name}")

        else:
            # Символічні посилання або інші об'єкти — жовтий
            print(f"{prefix}{Fore.YELLOW}{entry.name} (посилання або інший тип)")


def main() -> None:
    """Точка входу: перевірка аргументів та запуск візуалізації."""

    # 1. Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print(
            f"{Fore.RED}Помилка:{Style.RESET_ALL} "
            "Вкажіть шлях до директорії як аргумент.\n"
            f"Приклад: {Fore.YELLOW}python hw03.py /шлях/до/директорії"
        )
        sys.exit(1)

    target = Path(sys.argv[1])

    # 2. Перевірка існування шляху
    if not target.exists():
        print(
            f"{Fore.RED}Помилка:{Style.RESET_ALL} "
            f"Шлях '{target}' не існує."
        )
        sys.exit(1)

    # 3. Перевірка, що шлях веде до директорії
    if not target.is_dir():
        print(
            f"{Fore.RED}Помилка:{Style.RESET_ALL} "
            f"'{target}' не є директорією."
        )
        sys.exit(1)

    visualize_directory(target)

if __name__ == "__main__":
    main()