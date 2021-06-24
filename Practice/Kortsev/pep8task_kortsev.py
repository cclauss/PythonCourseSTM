import sys
import os
import hashlib
import ast
import argparse
import time # better practice then 'from time import *'


class Shuffler:  # class names should be in CamelCase
    # 1 white space between methods inside class definition
    def __init__(self):
        self.map = {}

    def rename_song(self, dir_name, output):  # dir_name instead of dirname
        mp3s = []  # 4 spaces needed instead of 5
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.get_name() + '.mp3'  # hash_name instead of hashname
            self.map[hash_name] = mp3
            os.rename(path + '/' + mp3, path + '/' + hash_name) # wrong brackets
            f = open(output, 'r') # wrong indents
            f.write(str(self.map))

    def restore_song(self, dir_name, restore_path):  # dir_name instead of dirname
        with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []  # wrong indents
        for root, directories, files in os.walk(dir_name):  # dir_name instead of dirname
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hash_name in mp3s:  # hash_name instead of hashname
            os.rename(path + '/' + hash_name, path + '/' + self.map[hashname])  # wrong bracket
        os.remove(restore_path)

    @staticmethod
    def get_name():  # here was wrong indent, methods names should be snake case, wrong method definition
        seed = time.time()
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='sub_command', help='subcommand help')
    rename_parser = sub_parsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = sub_parsers.add_parser('restore', help="command help")
    restore_parser.add_argument('dir_name')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():  # 2 blank lines between def's
    args = parse_arguments()
    shuffler = Shuffler()  # instead of Shuffler = shuffler()
    if args.subcommand == 'rename':  # fixed indent's below
        if args.output:
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
