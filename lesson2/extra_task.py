import csv, json, yaml
from pathlib import Path


def write_to_yaml(file, data):
    with open(file, 'w+') as f:
        yaml.safe_dump(data, f, allow_unicode=True, default_flow_style=False)

def read_from_yaml(file):
    f = Path(file)

    if f.exists():
        with open(file, 'r') as f:
            return yaml.safe_load(f)
    else:
        print(f'File {file} not exists')

def read_from_csv(file):
    f = Path(file)

    if f.exists():
        with open(file) as fr:
            csv_reader = csv.DictReader(fr)
            data = []

            for row in csv_reader:
                data.append(dict(row))

            return data
    else:
        print(f'File {file} not exists')

def write_to_json(file, data):
    with open(file, 'w+') as fr:
        json.dump(data, fr, indent=2)

def read_from_json(file):
    f = Path(file)

    if f.exists():
        with open(file) as fr:
            return json.load(fr)
    else:
        print(f'File {file} not exists')


if __name__ == '__main__':
    print('Reading from CSV...')
    data = read_from_csv('data/report.csv')

    print('Writing to JSON...')
    write_to_json('data/report.json', data)

    print('Reading from JSON...')
    data_json = read_from_json('data/report.json')

    print('CSV data is equal to JSON?', data == data_json)
    print()

    print('Writing to YAML...')
    write_to_yaml('data/report.yml', data)

    print('Reading from YAML...')
    data_yaml = read_from_yaml('data/report.yml')

    print('CSV data is equal to YAML?', data == data_yaml)
    print()

    print('Writing JSON to YAML...')
    write_to_yaml('data/report_json.yml', data_json)

    print('Reading from YAML...')
    data_json_yaml = read_from_yaml('data/report_json.yml')

    print('JSON data is equal to YAML?', data_json == data_json_yaml)
