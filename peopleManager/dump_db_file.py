from make_db_file import load_db
db = load_db()
for key in db:
    print(key, '=>', db[key])
print(db['sue']['name'])