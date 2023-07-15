# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.


import csv
import pickle



with open('person.csv', 'r') as f:
    reader_ = csv.reader(f)
    pickle.dump(list(reader_), open('hello.pkl', 'wb'))
    with open('hello.pkl', 'rb') as pickle_in: unpickled_list = pickle.load(pickle_in)
    print(unpickled_list)
