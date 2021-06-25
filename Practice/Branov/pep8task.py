import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dir_name, output):
        mp3s = []
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.generate_name() + '.mp3'
            self.map[hash_name] = mp3
            os.rename(path + '/' + mp3, path + '/' + hash_name)
            f = open(output, 'r')
            f.write(str(self.map))

    def restore(self, dir_name, restore_path):
        with open(file_name, '+') as f:  # откуда должен появиться file_name?
            self.map = ast.literal_eval(f.read())
        mp3s = []
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hash_name in mp3s:
            os.rename(path + '/' + hash_name, path + '/' + self.map[hash_name])
            os.remove(restore_path)

    @staticmethod
    def generate_name(seed=time()):
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dir_name')
    restore_parser.add_argument('restore_map')
    return parser.parse_args()


def main():
    args = parse_arguments()
    shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


if __name__ == '__main__':
    main()
