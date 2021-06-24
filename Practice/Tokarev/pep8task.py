import sys
import os
import hashlib
import ast
import argparse
from time import * # зачем указывать дополнительчто что берем все?


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output): #dirname и output не используется+правильно dir_name
        mp3s = [] # локальная, а не используется тут (если for сделать со сдвигом, то норм)

    for root, directories, files in os.walk(dirname): #dirname правильно dir_name, +for внутри def и должен быть со сдвигом на 4
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s: # for внутри def и должен быть со сдвигом на 4
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname)) #не верное кол-во скобок
        f = open(output, 'r')
        f.write(str(self.map))

    def restore(self, dirname, restore_path): #dirname и restore_path не используется+правильно dir_name
        with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = [] # локальная, а не используется тут (если for сделать со сдвигом, то норм)

    for root, directories, files in os.walk(dirname): # for внутри def и должен быть со сдвигом на 4
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append({root, file})
    for path, hashname in mp3s: # for внутри def и должен быть со сдвигом на 4
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # не верное кол-во скобок
        os.remove(restore_path)
# Имена функций должны быть в нижнем регистре, а слова должны быть разделены подчеркиванием по мере необходимости для облегчения чтения.
    def generateName(self, seed=time()):# правильно generate_name
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
    Shuffler = shuffler() #Shuffler-правильно shuffler
    if args.subcommand == 'rename':
        if args.output:
            Shuffler.rename(args.dirname, 'restore.info')
        else:
            Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
