import glob
import os

MB = 1024 * 1024

for i in glob.iglob(f'assets/**/sharedassets*.assets', recursive=True):
    fileSize = os.path.getsize(i)

    if fileSize > MB:
        q = fileSize // MB
        r = fileSize % MB
        n = 0

        with open(i, 'rb') as f:
            d = f.read()

        while(n < q):
            with open(f'{i}.split{n}', 'wb') as f:
                f.write(d[MB * n:MB * (n + 1)])
            n += 1

        if r > 0:
            with open(f'{i}.split{n}', 'wb') as f:
                f.write(d[MB * n:])
