import numpy as np
import json

path = 'C:/Users/39235/Desktop/CodeRepo/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, 'r')]
time_zone=[tz for tz in records+]
