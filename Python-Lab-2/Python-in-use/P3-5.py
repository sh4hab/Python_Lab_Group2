import csv

r= csv.reader(open('data.csv'))
lines = list(r)
for i in range(len(lines)):
	lines[i][0] = ' '
writer = csv.writer(open('data.csv' , 'w'))
writer.writerows(lines)

