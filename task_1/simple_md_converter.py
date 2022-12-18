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

    md_contents = f"""+ [{title}](#{md_link})

## {title}

{description}

```python
{source_code.lstrip()}
    ```"""

    return md_contents


def convert_data(data):
    header, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(header)
    result_md = prepare_md_format(title, description, source_code)
    return result_md


def main(input_file, output_file):
    contents = read_data(input_file)
    result = convert_data(contents)
    write_data(result, output_file)


if __name__ == "__main__":
    python_file = "../practice_2/diagonalsum.py"
    md_file = "matrix.md"
    main(python_file, md_file)
