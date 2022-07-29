
def read_names(test=False):
    filename = 'db.txt'
    if test:
        filename = 'hello_world/' + filename
    with open(filename) as f:
        data = f.read().split('\n')
    return data

def write_name(name, test=False):
    if name == '':
        return False
    return True