from initdata import bob, sue, tom
import pickle

for (name, record) in [('bob', bob), ('sue', sue), ('tom', tom)]:
    rec_file = open(name + '.pkl', 'wb')
    pickle.dump(record, rec_file)
    rec_file.close()