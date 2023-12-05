
import sys
import os
import hashlib


def calculate_md5(md5_file):
    if os.path.isfile(md5_file):
        with open(md5_file, 'rb') as fobj:
            data = fobj.read()
        m = hashlib.md5(data)
        return m.hexdigest()
    else:
        print('%s不存在或者是目录' % md5_file)
        sys.exit(1)


if __name__ == '__main__':
    try:
        md5_file = sys.argv[1]
    except IndexError:
        print('usage: %s file-name' % sys.argv[0])
    else:
        md5_value = calculate_md5(md5_file)
        print('%s \'s md5=%s' % (md5_file, md5_value))

