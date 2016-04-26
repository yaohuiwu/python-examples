dbFileName = 'people-file'
END_DB = 'enddb.'
END_REC = 'endrec.'
REC_SEP = '=>'


def store_db(db, db_file_name=dbFileName):
    db_file = open(db_file_name, 'w')
    for key in db:
        print(key, file=db_file)
        for (name, value) in db[key].items():
            print(name + REC_SEP + repr(value), file=db_file)
        print(END_REC, file=db_file)
    print(END_DB, file=db_file)
    db_file.close()


def load_db(db_file_name=dbFileName):
    db_file = open(db_file_name, 'r')
    import sys
    sys.stdin = db_file
    db = {}
    key = input()
    while key != END_DB:
        rec = {}
        field = input()
        while field != END_REC:
            name, value = field.split(REC_SEP)
            rec[name] = value
            field = input()
        db[key] = rec
        key = input()
    db_file.close()
    return db

if __name__ == '__main__':
    from initdata import  db
    store_db(db)
