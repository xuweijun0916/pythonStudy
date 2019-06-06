import pickle

new_man = []
try:
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)

except IOError as err:
    print('file error: ' + str(err))

except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

#nester.print_lol(new_man)
print(new_man[0])
print(new_man[-1])