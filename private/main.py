"""
Parse the C reference manual and convert it into
a vim-help format
"""

import re

def write_chapters():
    manual = get_file_contents('./manual/creference')

    chapter_header_pattern= r'^\d+.+ The \w+ function$'
    chapter_headers = re.findall(chapter_header_pattern, manual, re.M)

    chapters = []
    for i, header in enumerate(chapter_headers):

        # Crappy hack around index errors
        try:
            chapter_contents = manual[manual.index(header): manual.index(chapter_headers[i+1])]
            chapters.append(chapter_contents)
            write_chapter_to_file(header, chapter_contents)
        except IndexError:
            continue

    return chapters

def get_file_contents(file_path):
    """Return the file contents as a string"""
    file_to_read = open(file_path)
    file_contents = [line for line in file_to_read]
    return ''.join(file_contents)

def write_chapter_to_file(chapter_title, chapter_contents):

    manual = get_file_contents('./manual/creference')
    function_name = chapter_title.split()[2]
    chapter = open('../doc/' + function_name + '.txt', 'w')
    chapter.write('*' + function_name + '.txt*\n' )
    chapter.write('*' + function_name + '*\n')
    chapter.write(chapter_contents)
    chapter.write('\n\nvim:tw=78:ts=8:ft=help:norl:')
    chapter.close()

def main():
    write_chapters()

main()
