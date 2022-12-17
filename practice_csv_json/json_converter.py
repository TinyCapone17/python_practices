def read_data(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    return content


def write_data(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)


def read_data_to_list(file_name):
    with open(file_name, "r") as f:
        content = f.readlines()
    return content


def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_record(title, row):
    values = row.strip().split(',')
    record = dict(zip(title, values))

    def try_convert_value(val):
        try:
            res = int(val)
        except ValueError:
            try:
                res = float(val)
            except ValueError:
                return val
        return res

    pretty_rows = [
        f"""\t\t"{key}": "{value}",\n"""
        if not isinstance(try_convert_value(value), (int, float))
        else f"""\t\t"{key}": {try_convert_value(value)},\n"""
        for key, value in record.items()
    ]
    last_row = pretty_rows.pop(-1)
    last_row = last_row[:-2] + "\n"
    pretty_result = "\t{\n" + "".join(pretty_rows) + last_row + "\t},\n"
    return pretty_result


def convert_csv_to_json(data):
    title, data = prepare_data(data)

    # result = []
    # for row in data:
    #    result.append(convert_row_to_pretty_json(title, row))
    pretty_results = [convert_row_to_pretty_record(title, row) for row in data]
    last_result = pretty_results.pop(-1)
    last_result = last_result[:-2] + "\n"
    result = "[\n" + "".join(pretty_results) + last_result + "]\n"
    return result


def main():
    data = read_data_to_list("input.csv")
    result = convert_csv_to_json(data)
    write_data("output.json", result)


if __name__ == "__main__":
    main()
