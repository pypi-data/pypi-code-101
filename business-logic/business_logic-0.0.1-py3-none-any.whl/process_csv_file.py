import csv


def get_file_name(body: str):
    file_name = body[body.find('filename=') + 10: body.find('.csv') + 4]

    return file_name


def get_file_content(body):
    my_list = list(csv.reader(body.splitlines(), delimiter=','))

    rows = []
    for row in my_list[5:-2]:
        if row[0] == '':
            row[0] = float(row[1]) * float(row[2])
        elif row[1] == '':
            row[1] = float(row[0]) / float(row[2])
        else:
            row[2] = float(row[0]) / float(row[1])
        rows.append({'s': float(row[0]),
                     'v': float(row[1]),
                     't': float(row[2])})

    return rows
