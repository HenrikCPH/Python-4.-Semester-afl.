import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that read, writes and/or stores text locally')
    parser.add_argument('folder',
                        help='The path to the folder to process')
    parser.add_argument('file',
                        help='The file to output to')

    args = parser.parse_args()
    print('Folder:', args.folder)
    print('File:', args.file)

    def get_file_names(folderpath, out=args.file):
        """ takes a path to a folder and writes all filenames in the folder to a specified output file"""

    def get_all_file_names(folderpath, out=args.file):
        """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

    def print_line_one(file_names):
        """takes a list of filenames and print the first line of each"""

    def print_emails(file_names):
        """takes a list of filenames and print each line that contains an email (just look for @)"""

    def write_headlines(md_files, out=args.file):
        """takes a list of md files and writes all headlines (lines starting with #) to a file"""
