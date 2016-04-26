from make_db_file import load_db, store_db
db = load_db()

print(type(db['sue']['pay']))

payFloat = float(db['sue']['pay'])
payFloat *= 1.10

db['sue']['pay'] = payFloat
db['tom']['name'] = 'Tom Tom'
store_db(db)