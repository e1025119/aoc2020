from aocd import get_data
import math

data = get_data(day=13, year=2020).split('\n')
data[1] = min(((math.ceil(int(data[0])/int(x))*int(x)-int(data[0])),int(x)) for x in data[1].split(',') if x != 'x')

print(data[1][0]*data[1][1])
