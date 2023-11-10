# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = Path('data/txt2md/outline.md')
    # TU CÓDIGO AQUÍ
    with open(text_path, "r") as file:
        lines = file.readlines()
    
    with open(md_path, "w") as md_file:
        for line in lines:
            spaces = 0
            while line.startswith("\t"):
                spaces += 1
                line = line[1:]
            md_line = "#" * spaces + " " + line
            md_file.write(md_line)
            
    expected_md_path = Path('data/txt2md/.expected')
    
    return filecmp.cmp(md_path, expected_md_path, shallow=False)


if __name__ == '__main__':
    path_outline = Path('data/txt2md/outline.txt')
    markdown = run(path_outline)
    print(markdown)