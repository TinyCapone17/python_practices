INPUT_CODE_DELIMITER = "# ---end----"


def read_data(input_file):
    with open(input_file, "r") as f:
        contents = f.read()
    return contents


def write_data(data, output_file):
    with open(output_file, "w") as f:
        f.write(data)


def prepare_md_titles(data):
    title, description = None, None

    for line in data.split("\n"):
        if line.startswith("# title"):
            title = line.replace("# title ", "")
        elif line.startswith("# description"):
            description = line.replace("# description ", "")

    return title, description


def prepare_md_format(title, description, source_code):
    md_link = "-".join(title.lower().split())

    link = f"+ [{title}](#{md_link})"

    md_contents = f"""
## {title}

{description}

```python
{source_code.lstrip()}
```
"""

    return link, md_contents


def convert_data(data):
    header, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(header)
    link, result_md = prepare_md_format(title, description, source_code)
    return link, result_md

def add_to_output(link, result, md_file):
    md_file_lines = md_file.split("\n")
    links, results = [], []
    for line in md_file_lines:
        if line.startswith("+"):
            links.append(line)
        else:
            results.append(line)

    links.append(link)
    results.append(result)

    return "\n".join(links) + "\n" + "\n".join(results)


def main(input_file, output_file):
    contents = read_data(input_file)
    try:
        md_file = read_data(output_file)
    except FileNotFoundError:
        md_file = ""
    link, result = convert_data(contents)
    final_result = add_to_output(link, result, md_file)
    write_data(final_result, output_file)


if __name__ == "__main__":
    # python_file = "../practice_2/diagonalsum.py"
    # python_file = "../practice_2/concatsort.py"
    # python_file = "../practice_2/sortedsquares.py"
    # python_file = "../practice_2/compresschars.py"

    md_file = "scripts.md"
    main(python_file, md_file)
