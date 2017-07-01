"""
Parse the C reference manual and convert it into
a vim-help format
"""

import re

def get_chapters():
    """Returns all chapters from the C reference manual"""
    pass

def get_file_contents(file_path):
    """Return the file contents as a string"""
    file_to_read = open(file_path)
    file_contents = [line for line in file_to_read]
    return ''.join(file_contents)

def main():
    manual = get_file_contents('../manual/creference')

    function_pattern = r'the \w+ function .*'
    result = re.findall(function_pattern, manual, re.M)
    print(result)
    print(manual)


main()




