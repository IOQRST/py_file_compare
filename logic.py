def read_lines(file_path: str) -> list[str]:
    """
    Читает строки из файла, убирая переносы строк и пустые строки.

    Args:
        file_path: Путь к файлу.
    Returns:
        Список строк для одного файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except (FileNotFoundError, IOError) as e:
        print(f"Ошибка чтения файла: {e}")
        return []


def get_unique_lines(file1_path: str, file2_path: str) -> list[str]:
    """
    Сравнивает два списка строк из файлов. Возвращает список уникальных строк из двух списков.

    Args:
        file1_path: Путь к файлу 1.
        file2_path: Путь к файлу 2.
    Returns:
        Список уникальных строк, собранный из двух файлов.
    """
    lines1 = read_lines(file1_path)
    lines2 = read_lines(file2_path)

    unique_lines = set()
    unique_lines.update(lines1)
    unique_lines.update(lines2)
    if not unique_lines:
        print("Файлы пустые или не содержат данных")
    return sorted(unique_lines)


def save_results(strings: list[str], output_path: str) -> None:
    """
    Сохраняет список строк в файл.

    Args:
       strings: Список строк для записи.
       output_path: Путь к выходному файлу.
    """
    if not strings:
        print("Нет данных для записи")
        return

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(strings))
    except (IOError, PermissionError) as e:
        print(f"Ошибка записи файла: {e}")

# unique_lines = get_unique_lines("1.txt", "2.txt")
unique_lines = get_unique_lines("notexistentfile.txt", "test_data/2.txt")
save_results(unique_lines, "test_data/test.txt")
