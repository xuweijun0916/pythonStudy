import os
if os.path.exists('sketch.txt'):
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
                # help(each_line.split)
                print(role,end=' ')
                print('said:',end=' ')
                print(line_spoken, end='')
        except:
            pass

    data.close()
else:
    print('The data file is missing!')