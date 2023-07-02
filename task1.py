#  Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import base64

def read_pcl(file_pcl):
    objects = []
    with (open(file_pcl, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
data = 'utput.pickle'
print(read_pcl(data))


with open('a.csv', 'a', encoding='utf8') as csv_file:
    wr = csv.writer(csv_file, delimiter='|')
    pickle_bytes = pickle.dumps(obj)            # unsafe to write
    b64_bytes = base64.b64encode(pickle_bytes)  # safe to write but still bytes
    b64_str = b64_bytes.decode('utf8')          # safe and in utf8
    wr.writerow(['col1', 'col2', b64_str])


# the file contains
# col1|col2|gANdcQAu

with open('a.csv', 'r') as csv_file:
    for line in csv_file:
        line = line.strip('\n')
        b64_str = line.split('|')[2]                    # take the pickled obj
        obj = pickle.loads(base64.b64decode(b64_str))   # retrieve


# res = pickle.loads('output.pickle')
# print(f'{res=}')


