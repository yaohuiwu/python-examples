import pickle
db_file = open('people-pickle', 'rb')
db = pickle.load(db_file)

for key in db:
    print(key, "=>\n", db[key])

db_file.close()