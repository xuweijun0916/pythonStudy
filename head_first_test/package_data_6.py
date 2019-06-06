def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

class AthleteList(list):
    def __init__(self,a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]

'''
class Athlete():
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,list_of_times):
        self.times.extend(list_of_times)
'''
'''
def get_coach_data(filename):
    try:
        with open(filename) as fi:
            data = fi.readline()
        temple = data.strip().split(',')
        return(AthleteList(temple.pop(0),temple.pop(0),temple))
    except IOError as ioerr:
        print('file error:' + str(ioerr))
        return None
#sarah = get_coach_data("sarah.txt")
#print(sarah.name+"'s fastest times are:"+ str(sarah.top3()))

vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())
'''