import yaml
from random import randint


def write_to_yaml(file, data):
    with open(file, 'w+') as f:
        yaml.safe_dump(data, f, allow_unicode=True, default_flow_style=False)

def read_from_yaml(file):
    with open(file, 'r') as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    data = {
        'this_is_list': [randint(0, _**2) for _ in range(1, 10)],
        'this_is_integer': randint(0, 10),
        'this_is_dict': {f'{a}лось': a**2 for a in range(1, 5)}
    }

    print('Writing to yaml...')
    write_to_yaml('data/result.yaml', data)

    print('Reading from yaml...')
    result = read_from_yaml('data/result.yaml')

    print('Result equals to source? ', result == data)
