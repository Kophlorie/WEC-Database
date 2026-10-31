import os
import json

def database_scan(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [database_scan(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


if __name__ == '__main__':
    paths = database_scan('Database/')
    print(json.dumps(paths['children'][0]['children'], indent=2))
