import os
import csv
import json
import pickle


class ClassCsv:

    def write_csv_file(self, name_csv_file, data):
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'w', newline='', encoding='utf-8') as csv_f:
            write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
            write_csv.writerows(data)

    def print_csv_file(self, name_csv_file):
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'r', newline='', encoding='utf-8') as csv_file:
            csv_f = csv.reader(csv_file)
            for i in csv_f:
                print(i)

    def append_in_csv_file(self, name_csv_file, data):
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'a', newline='', encoding='utf-8') as csv_f:
            write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
            write_csv.writerows(data)

    def delete_csv_file(self, path_file):
        os.remove(os.walk(path_file))


class ClassJson:

    def write_json_file(self, name_json_file, data):
        with open('json_csv_pickle_files/' + name_json_file + '.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, separators=(',', ':'))

    def print_json_file(self, name_json_file):
        with open('json_csv_pickle_files/' + name_json_file + '.json', 'r', encoding='utf-8') as json_file:
            print(json.load(json_file))

    def append_in_json_file(self, name_json_file, data):
        with open('json_csv_pickle_files/' + name_json_file + '.json', 'a', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, separators=(',', ':'))

    def delete_json_file(self, path_file):
        os.remove(os.walk(path_file))


class ClassPickle:
    def __init__(self):
        pass

    def write_pickle_file(self, name_pickle_file, data):
        with open('json_csv_pickle_files/' + name_pickle_file + '.bin', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)

    def print_pickle_file(self, name_pickle_file):
        with open('json_csv_pickle_files/' + name_pickle_file + '.bin', 'rb') as pickle_file:
            print(pickle.load(pickle_file))

    def append_in_pickle_file(self, name_pickle_file, data):
        with open('json_csv_pickle_files/' + name_pickle_file + '.bin', 'ab') as pickle_file:
            pickle.dump(data, pickle_file)

    def delete_pickle_file(self, path_file):
        os.remove(os.walk(path_file))