import re
import csv


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    dicts = [[] for _ in range(len(files))]
    headers = [
        "Название ОС", "Изготовитель системы", "Код продукта", "Тип системы"
    ]

    for i, f in enumerate(files):
        with open(f'data/{f}', encoding='cp1251') as fr:
            f_content = fr.read().encode('utf-8').decode('utf-8')
            for entity in re.findall(r'((Изготовитель ОС|Название ОС|Код продукта|Тип системы):([^\n]+))', f_content):
                dicts[i].append(entity[2].strip())
            dicts[i] = dict(zip(headers, dicts[i]))

    return (headers, dicts)

def write_to_csv(filename):
    headers, data = get_data()
    with open(filename, 'w') as fr:
        fr_csv = csv.DictWriter(fr, fieldnames=headers)
        fr_csv.writeheader()
        fr_csv.writerows(data)


if(__name__ == '__main__'):
    write_to_csv('data/report.csv')
    print('Data saved to: data/report.csv')
