def read_template(path):
    with open(path) as file:
        return file.read()

def parse_template(template): 
    pass

def merge(one, two):
    return one.format(*two)