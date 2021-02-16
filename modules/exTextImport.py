import utils as uT
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that read, writes and/or stores text locally')
    parser.add_argument('folder',
                        help='The path to the folder to process')
    parser.add_argument('file',
                        help='The file to output to')
    parser.add_argument('list', nargs='*',
                        help='The list of files to have its first line read')

    args = parser.parse_args()
    print('Folder:', args.folder)
    print('File:', args.file)
    print('List', args.list)

print("\nFile names from folder:")
print(uT.get_file_names(args.folder))
print("\nall files from directory")
print(uT.get_all_file_names(args.folder))
print("\nFirst line of given list")
uT.print_line_one(args.list)
print("\nEmails from list")
uT.print_emails(args.list)
print("\nmd files list")
print(uT.write_headlines(args.list))
