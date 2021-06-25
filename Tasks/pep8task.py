import argparse  # optimize import
import ast
import hashlib
import os
import sys
import time


# Шаблоны импортов (from import *) следует избегать,
# так как они делают неясным то, какие имена присутствуют в
# глобальном пространстве имён


# отступы поправлены с помощью Alt+Ctrl+L  в пайчарм


class Shuffler:  # Class names should normally use the CapWords convention

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []

        for root, directories, files in os.walk(dirname):  # исправлен отступ
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.generate_name() + '.mp3'  # исправлено название hash_name для читабельности
            # generate_name() не передаем seed - убрала его из метода
            self.map[hash_name] = mp3
            os.rename(path + '/' + mp3, path + '/' + hash_name)  # лишние скобки
            f = open(output, 'r')
            f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:  # переменная filename не определена
            self.map = ast.literal_eval(f.read())
        mp3s = []

        for root, directories, files in os.walk(dirname):  # исправлен отступ
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hash_name in mp3s:  # переименованна переменна
            os.rename(path + '/' + hash_name, path + '/' + self.map[hash_name])  # убраны лишние скобки
            os.remove(restore_path)

    def generate_name(self):  # не  нравится конструкция  seed=time() и функция time не определена
        #  переименовано имя функции
        seed = time.time()
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    shuffler = Shuffler()  # Имя класса с большой буквы, объект класса с маленькой
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
