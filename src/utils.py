import difflib
from pathlib import Path


def get_lines_file(file_path):
    with open(file_path) as f:
        return f.readlines()


def get_line_to_scroll(old_lines, new_lines) -> int:
    diffs = difflib.Differ().compare(old_lines, new_lines)
    lin_num = 0
    diffing_lines = []
    for line in diffs:
        code = line[:2]
        if code in ("  ", "+ "):
            lin_num += 1
        if code == "+ ":
            diffing_lines.append(lin_num)
    if diffing_lines:
        return diffing_lines[-1]
    return lin_num


def get_file_path_from_notebook_path(notebook_path):
    notebook_path = Path(notebook_path)
    return notebook_path.parent / f"{notebook_path.stem}.py"
