import pickle
# db_file = open('people-pickle', 'rb')
# db = pickle.load(db_file)
# db_file.close()
FILE_SUE = 'sue.pkl'
FILE_TOM = 'tom.pkl'

sue_file = open(FILE_SUE, 'rb')
sue = pickle.load(sue_file)
sue_file.close()

tom_file = open(FILE_TOM, 'rb')
tom = pickle.load(tom_file)
sue['pay'] *= 1.10
tom['name'] = "Tom Tom"

sue_file = open(FILE_SUE, 'wb')
pickle.dump(sue, sue_file)
sue_file.close()

tom_file = open(FILE_TOM, 'wb')
pickle.dump(tom, tom_file)
tom_file.close()
