import pickle, glob

for file_name in glob.glob("*.pkl"):
    with open(file_name, 'rb') as rec_file:
        record = pickle.load(rec_file)
        print(file_name, "=>\n", record)

with open('sue.pkl', 'rb') as sue_file:
    sue = pickle.load(sue_file)
    print("sue's name:", sue['name'])
