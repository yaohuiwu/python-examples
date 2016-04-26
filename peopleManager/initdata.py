#!/usr/bin/env python

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 46, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = {'bob': bob, 'sue': sue, 'tom': tom}

print("tom['age']:", type(tom['age']))
print("db['tom']['age']:", type(db['tom']['age']))

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])
