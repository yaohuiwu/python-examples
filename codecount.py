import sys

def codecount(dir, ext):
   print "dir", dir, " extensions", ext


if __name__ == 'main':
    dir='.'
    exts=['.java']
    if len(sys.argv) > 2:
        dir = sys.argv[1]
    if len(sys.argv) > 3:
        exts=sys.argv[2].split()
