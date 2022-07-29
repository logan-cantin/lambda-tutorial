
def read_names():
    with open('db.txt') as f:
        data = f.read().split('\n')
    return data

def write_name(name):
    if name == '':
        return False
    with open('db.txt', 'a') as f:
        f.write(f'{name}\n')
    return True