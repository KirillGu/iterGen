import hashlib


def hash_line(path):
    i = hashlib.md5()

    with open(path, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            i.update(line.encode('utf-8'))
            yield i.hexdigest()


gen = hash_line('results.txt')

for item in gen:
    print(item)
