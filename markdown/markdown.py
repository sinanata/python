import mistune
import re

def parse(markdown):
    lines = markdown.splitlines()
    output = ''
    for i in lines:
        output += mistune.markdown(i)

    output = re.sub(r'\n', '', output)
    output = re.sub(r'</ul><ul>', '', output)
    output = re.sub(r'</ol><ol>', '', output)
    return output