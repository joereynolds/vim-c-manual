"""
Parse the C reference manual and convert it into
a vim-help format
"""
import re

MANUAL_PATH = './manual/creference'

def write_chapters():
    manual = get_file_contents(MANUAL_PATH)

    chapter_header_pattern = r'^\d+.+ The \w+ function$'
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
    file_contents = [line for line in open(file_path)]
    return ''.join(file_contents)

def write_chapter_to_file(chapter_title, chapter_contents):
    function_name = chapter_title.split()[2]
    chapter = open('../doc/' + function_name + '.txt', 'w')
    write_vim_help_hyperlinks(chapter, function_name)

    for line in chapter_contents.split('\n'):
        # These are headers in the file
        if 'Synopsis' in line or 'Description' in line or 'Returns' in line:
            chapter.write('\n')
            chapter.write('=' * 78 + '\n')
        chapter.write(line + '\n')

    write_vim_help_format(chapter)
    chapter.close()

def write_vim_help_hyperlinks(chapter, link):
    chapter.write('*' + link + '.txt*\n')
    chapter.write('*' + link + '*\n\n')

def write_vim_help_format(chapter):
    chapter.write('\nvim:tw=78:ts=8:ft=help:norl:')

def main():
    write_chapters()

main()
