import sys
import os
import hashlib
import ast
import argparse
from time import time  # import only needed function


class Shuffler:  # class names should use CapWords

    def __init__(self):
        self.map = {}

    def rename(self, dir_name, output):
        mp3s = []  # indent 4 spaces
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.generateName() + '.mp3'  # variable name should be separated with underscores
            self.map[hash_name] = mp3
            os.rename(path + '/' + mp3, path + '/' + hash_name)
        f = open(output, 'r')
        f.write(str(self.map))

    def restore(self, dir_name, restore_path):
        with open(dir_name, '+') as f:  # indent 4 spaces. use directory arg instead filename
            self.map = ast.literal_eval(f.read())
        mp3s = []
        for root, directories, files in os.walk(dir_name):  # use dir_name arg
            for file in files:
                if file[-3:] == '.mp3':  # indent 4 spaces
                    mp3s.append({root, file})
        for path, hash_name in mp3s:
            os.rename(path + '/' + hash_name, path + '/' + self.map[hash_name])
        os.remove(restore_path)

    def generate_name(self, seed=time()):  # indent 4 spaces, function names should be lowercase, with words
        # separate with underscores
        return hashlib.md5(str(seed).encode('utf-8')).hexdigest()  # indent 4 spaces, string to bytes


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dir_name')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():  # 2 blank lines to separate classes and functions
    args = parse_arguments()
    shuffler = Shuffler()  # variable names should be lowercase
    # use blank lines to to indicate logical sections
    if args.subcommand == 'rename':
        if args.output:  # indent 4 spaces
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
