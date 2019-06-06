from find_it import find_closest
from tm2secs2tm import time2secs, secs2time, format_time

def find_nearest_time(look_for, target_data):
    what = time2secs(look_for)
    where = [time2secs(t) for t in target_data]
    res = find_closest(what,where)
    return(secs2time(res))

row_data = {}
with open('C:/Users/xuwj/PycharmProjects/untitled/head_first_test/PaceData.csv') as paces:
    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0)

    for each_line in paces:
        row = each_line.strip().split(',')
        row_lable = row.pop(0)
        inner_dict = {}
        for i in range(len(column_headings)):
            inner_dict[format_time(row[i])] = column_headings[i]

        row_data[row_lable] = inner_dict

distance_run = input('Enter the distance attempted:')
recorded_time = input('Enter the recorded time:')
predicted_distance = input('Enter the distance you want a prediction for:')

closest_time = find_nearest_time(format_time(recorded_time), row_data[distance_run])
closest_column_heading = row_data[distance_run][closest_time]

prediction = [k for k in row_data[predicted_distance].keys()
              if row_data[predicted_distance][k] == closest_column_heading]
print('The predicited time running ' + predicted_distance + ' is: '+ prediction[0] + '.')

# row_data[distance_run][recorded_time]
'''
l = find_nearest_time('59:59',['56:45','59:29','1:00:23'])
print(l)
column_heading = row_data['15k']['43:24']
print(column_heading)

prediction = [k for k in row_data['20k'].keys() if row_data['20k'][k] == column_heading]
print(prediction)

num_cols = len(column_headings)
print(num_cols, end=' -> ')
print(column_headings)

num_2mi = len(row_data["2mi"])
print(num_2mi, end=' -> ')
print(row_data['2mi'])

num_Marathon = len(row_data['Marathon'])
print(num_Marathon, end=' -> ')
print(row_data['Marathon'])
'''