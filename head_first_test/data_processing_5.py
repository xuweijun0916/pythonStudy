'''
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')
'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.'+ secs)

def get_coach_data(filename):
    try:
        with open(filename) as fi:
            data = fi.readline()
        temple = data.strip().split(',')
        return({'name':temple.pop(0),
                'dob' :temple.pop(0),
                'times':str(sorted(set([sanitize(t) for t in temple]))[0:3])})
    except IOError as ioerr:
        print('file error:' + str(ioerr))
        return None
sarah = get_coach_data("sarah.txt")
print(sarah['name']+"'s fastest times are:"+ sarah['times'])
#print(get_coach_data("james.txt",))


#sarah = get_coach_data('sarah.txt')
#(sarah_name, sarah_dob) = sarah.pop(0),sarah.pop(0)
#print(sarah_name + "'s fastest timea are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

#sarah_info = {'sarah_name':sarah.pop(0),'sarah_dob':sarah.pop(0),'sarah_fastest_time':sorted(set([sanitize(t) for t in sarah]))[0:3]}
#print(sarah_info)
'''
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])

james_new = []
julie_new = []
mikey_new = []
sarah_new = []

for each_time in james:
    new_time = sanitize(each_time)
    james_new.append(new_time)

for each_time in julie:
    new_time = sanitize(each_time)
    julie_new.append(new_time)

for each_time in mikey:
    new_time = sanitize(each_time)
    mikey_new.append(new_time)

for each_time in sarah:
    new_time = sanitize(each_time)
    sarah_new.append(new_time)
    
print(sorted(james_new))
print(sorted(julie_new))
print(sorted(mikey_new))
print(sorted(sarah_new))

james = sorted([sanitize(each_time) for each_time in james])
unique_james = []
for t in james:
    if t not in unique_james:
        unique_james.append(t)

print(sorted(unique_james[0:3]))


julie = sorted([sanitize(t) for t in julie])
unique_julie = []
for t in julie:
    if t not in unique_julie:
        unique_julie.append(t)
print(unique_julie[0:3])

mikey = sorted([sanitize(t) for t in mikey])
unique_mikey = []
for t in mikey:
    if t not in unique_mikey:
        unique_mikey.append(t)
print(unique_mikey[0:3])

sarah = sorted([sanitize(t) for t in sarah])
unique_sarah = []
for t in sarah:
    if t not in unique_sarah:
        unique_sarah.append(t)
print(unique_sarah[0:3])
'''

