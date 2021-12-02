import re

def read_template(path):
    """accepts a file path, returns contents of file"""
    with open(path) as file:
        return file.read()

def parse_template(template):
    """un-does string format()"""
    regex = r'{\w*}'
    regex_2 = r'\w{2,}'

    parts = str(re.findall(regex, template))

    return_parts = tuple(re.findall(regex_2, parts))

    stripped = re.sub(regex, '{}', template)

    return (stripped, return_parts)

def merge(one, two):
    """accepts an fstring and a list of variables, formats the string with variables"""
    return one.format(*two)

