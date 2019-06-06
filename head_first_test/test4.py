import pickle
man = []
other = []
try:
    data = open('sketch.txt')
    '''
    print(data.readline(), end='')
    print(data.readline(), end='')
    data.seek(0)
    '''

    for each_line in data:
        try:
            #if each_line.find(':') != -1:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            # help(each_line.split)
           # print(role,end=' ')
            #print('said:',end=' ')
            #print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing!')
'''
try:
    with open('its.txt','w') as data:
        print("it's...",file=data)
        
except IOError as err:
    print('File error: ' + str(err))
'''';'

try:
    with open("man_data.txt","wb") as man_file:
        #nester.print_lol(man, True,1, fn=man_file)
        pickle.dump(man,man_file)

    with open("other_data.txt","wb") as other_file:
        #nester.print_lol(other, True,1,fn=other_file)
        pickle.dump(other,other_file)


except IOError as err:
    print("file error:" + str(err))

except pickle.DickleError as perr:
    print('Dickling error:' + str(perr))


print(man)
print(other)