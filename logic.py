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


def get_unique_lines(file_paths: list) -> list[str]:
    """
    Сравнивает несколько файлов построчно. Возвращает список уникальных строк.

    Args:
        file_paths: список путей к файлам.
    Returns:
        Список уникальных строк, собранный из списка файлов.
    """
    unique_lines = set()

    for i in file_paths:
        lines = read_lines(i)
        unique_lines.update(lines)
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

unique_lines = get_unique_lines(["test_data/1.txt", "test_data/2.txt"])
save_results(unique_lines, "test_data/test.txt")
